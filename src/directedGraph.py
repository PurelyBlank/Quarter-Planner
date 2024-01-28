import requests
import json

class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, start, end):
        if start in self.graph and end in self.graph:
            self.graph[start].append(end)

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex} -> {', '.join(edges)}")



    def truth(self, tree, course):
        for key,value in tree.items():
            if key == "AND":
                for i in value:
                    if type(i) == dict:
                        if not self.truth(i,course):
                            return False
                    elif type(i) == str:
                        i = i.replace(' ','')
                        if i not in course:
                            return False
                        # c=False
                        # if i in course:
                        #     c=False
                        #     continue
                    # if c:
                    #     return False

            elif key == "OR":
                c=False
                for i in value:
                    if type(i) == dict:
                        if not self.truth(i,course):
                            return False
                    elif type(i) == str:
                        i = i.replace(' ','')
                        if i in course:
                            c=True
                if not c:
                    return False

        return True


    def getPotentialFutureCourse(self, allCoursesMap):

        allCourses = []
        for x, y in allCoursesMap.items():
            allCourses += y

        potentialFutureCourses = []

        #Dhruv or us gotta make sure formatting for strings is correct
        #Dhruv came through

        currentRequirementsList = ['I&CSCI31', 'I&CSCI32', 'I&CSCI33', 'I&CSCI45C', 'I&CSCI46',
                                   'I&CSCI51', 'I&CSCI53', 'I&CSCI6B', 'I&CSCI6D', 'I&CSCI139W',
                                   'MATH2A', 'MATH2B', 'I&CSCI6N', 'MATH3A', 'STATS67', 'IN4MATX43', 
                                   'COMPSCI161']

        #get potential list of future classes
        print(allCourses)
        response = requests.get("https://api.peterportal.org/rest/v0/courses/I&CSCI33")
        print(response.json()['prerequisite_for'])

        for course in allCourses:
            print(course)
            if course in currentRequirementsList:
                response = requests.get("https://api.peterportal.org/rest/v0/courses/" + course)
                print(response.json()['prerequisite_for'])
                potentialFutureCourses += response.json()['prerequisite_for']

        print("POTENTIAL BEFORE PARSING")

        #for course in potentialFutureCourses:
            
        potentialFutureCourses = list(set(potentialFutureCourses))
        print(potentialFutureCourses)

        #remove courses user has already taken and courses they don't have prereqs for
        for course in potentialFutureCourses:

            #split and modify course
            originalCourse = course
            course = course.replace(' ', '')

            print(course)
            #if user has already taken course
            if course in allCourses and originalCourse in potentialFutureCourses:
                #print(course)
                potentialFutureCourses.remove(originalCourse)
            
            #if user has not already taken course, check if it's prereqs have been completed
            else:
                #print(course)
                response = requests.get("https://api.peterportal.org/rest/v0/courses/" + course)
                
                #print(response.json())
                # for prereq in response.json()['prerequisite_list']:
                #     if prereq not in allCourses and originalCourse in potentialFutureCourses:
                #         #print(originalCourse)
                #         #print(potentialFutureCourses)
                #         potentialFutureCourses.remove(originalCourse)

                if self.truth( json.loads(response.json()['prerequisite_tree']) , allCourses  ) == False:
                    potentialFutureCourses.remove(originalCourse)
            

        potentialFutureCourses = list(set(potentialFutureCourses))
        return potentialFutureCourses
    

    def getFinalList(self, potentialFutureCourses, numberOfCsClasses):
        finalList = []

        currentRequirementsList = ['I&CSCI31', 'I&CSCI32', 'I&CSCI33', 'I&CSCI45C', 'I&CSCI46',
                                   'I&CSCI51', 'I&CSCI53', 'I&CSCI6B', 'I&CSCI6D', 'I&CSCI139W',
                                   'MATH2A', 'MATH2B', 'I&CSCI6N', 'MATH3A', 'STATS67', 'IN4MATX43', 
                                   'COMPSCI161']

        for course in potentialFutureCourses:
            course = course.replace(' ', '')

            response = requests.get("https://api.peterportal.org/rest/v0/courses/" + course)
            d = response.json()

            if d['number'][-1].isnumeric() == False:
                x = d['number']
                while(not x[-1].isnumeric()):
                    x=x[:-1]
                num = int(x)
                finalList.append(( (ord(d['number'][-1]) / 100) + num, course) )
            else:
                finalList.append( ( float(d['number'][-1]), course) )

        newFinalList = sorted(finalList, key=lambda x: x[0])

        for x in newFinalList:
            if x[0] < 100 and x[1] not in currentRequirementsList:
                newFinalList.remove(x)

        finalList = []
        

        counter = 0
        while (counter < numberOfCsClasses and counter < len(newFinalList)):
            finalList.append( newFinalList[counter][1] )
            counter += 1

        
        print(newFinalList)
        return finalList



            


'''

CURR
ics-6d 4 2
ics-33 4 7
stats-67 4 10
sociol-1 4 10

ARCH
// same format as above

PREF
notake ...
// etc.

'''


'''
# Example usage:
graph = DirectedGraph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")

graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "A")

graph.display()
'''
