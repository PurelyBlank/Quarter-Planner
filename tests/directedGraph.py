import requests


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

    def getPotentialFutureCourse(self, allCourses):
        potentialFutureCourses = []

        #Dhruv or us gotta make sure formatting for strings is correct

        #get potential list of future classes
        for course in allCourses:
            response = requests.get("https://api.peterportal.org/rest/v0/courses/" + course)
            potentialFutureCourses += response.json()['prerequisite_for']

        #remove courses user has already taken and courses they don't have prereqs for
        for course in potentialFutureCourses:
            if course in allCourses:
                potentialFutureCourses.remove(course)

            response = requests.get("https://api.peterportal.org/rest/v0/courses/" + course)
            for prereq in response.json()['prerequisite_list']:
                if prereq not in allCourses:
                    potentialFutureCourses.remove(course)
            

        return potentialFutureCourses
    
    def getFinalList(self, potentialFutureCourses, numberOfCsClasses):
        finalList = []

        for course in potentialFutureCourses:
            response = requests.get("https://api.peterportal.org/rest/v0/courses/" + course)
            if response['number'][-1].isnumeric() == False:
                num = int(response['number'][:-1])
                finalList.append(( (ord(response['number'][-1]) / 100) + num, course) )
            else:
                finalList.append( ( float(response['number']), course) )

        newFinalList = sorted(finalList, key=lambda x: x[0])

        finalList = []

        counter = 0
        while (counter < numberOfCsClasses):
            finalList.append(newFinalList[counter][1])
            counter += 1

        return finalList



            


response = requests.get("https://api.peterportal.org/rest/v0/courses/I&CSCI53")
print(response.json()['prerequisite_for'])

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



# Example usage:
graph = DirectedGraph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")

graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "A")

graph.display()
