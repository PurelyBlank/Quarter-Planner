from pathlib import Path

import requests
import json

class StudentProgress:

    def __init__(self):
        self.cats_and_courses = {"DEGREE": list(), 
                                 "GE Ia": list(), "GE Ib": list(), "GE II": list(), 
                                 "GE III": list(), "GE IV": list(), "GE Va": list(), 
                                 "GE Vb": list(), "GE VI": list(), "GE VII": list(), 
                                 "GE VIII": list()}
        
        self.counts_per_ge = {"GE Ia": 2, "GE Ia": 1, "GE II": 3, "GE III": 3, "GE IV": 3,
                              "GE Va": 1, "GE Vb": 2, "GE VI": 3, "GE VII": 1, "GE VIII": 1}
        
    def __str__(self):
        student_prog_str = "Categories and Courses:\n\n"

        for category, courses in self.cats_and_courses.items():
            student_prog_str += category + ': ' + ', '.join(courses) + '\n'
        
        student_prog_str += "\nCounts Per GE:\n\n"

        for ge, count in self.counts_per_ge.items():
            student_prog_str += ge + ': ' + str(count) + '\n'

        return student_prog_str


class StudentPreferences:

    def __init__(self):
        # the below attribute is a stub that will be improved upon further knowing the requirements
        self.queries = ("Num CS Classes", "Num GEs", "Unit Range", "Undesirable Class Combos", 
                        "Targeting GE Categories")
        
        self.num_queries = 5
        self.query_results = [""] * self.num_queries

    def __str__(self):
        stringpref = "Preferences:\n\n"
        
        for i in range(0, self.num_queries):
            stringpref += self.queries[i] + ": "

            if i <= 2:
                stringpref += str(self.query_results[i])

            elif i == 3:
                for result in self.query_results[i]:
                    if len(result) == 2:
                        stringpref += '(' + result[0] + ", " + result[1] + "), "

                stringpref = stringpref[:-2]
                
            else:
                stringpref += "".join(self.query_results[i])
            
            stringpref += '\n'

        return stringpref


class InputParser:

    def __init__(self, taken_query: str, pref_query: str):
        self.taken_path = Path("src/txt/taken.txt")
        self.pref_path = Path("src/txt/pref.txt")

        taken_ui_input = open(self.taken_path, mode='w')
        taken_ui_input.write(taken_query)
        taken_ui_input.close()

        pref_ui_input = open(self.pref_path, mode='w')
        pref_ui_input.write(pref_query)
        pref_ui_input.close()

    def parse_input(self):
        url = "https://api.peterportal.org/rest/v0/courses/"

        student_prog = StudentProgress()
        student_pref = StudentPreferences()

        with open(self.taken_path, mode='r', encoding='utf-8') as student_taken_file:
            for course in student_taken_file:
                course = course[:-1]
                response = requests.get(url + course)

                if (response.status_code == 200):
                    ge_list = response.json()['ge_list']

                    for ge in ge_list:
                        ge = ge.split(': ')[0]
                        student_prog.cats_and_courses[ge].append(course)

        with open(self.pref_path, mode='r', encoding='utf-8') as student_pref_file:
            curr_query_num = 1

            for answer in student_pref_file:
                if curr_query_num <= 2:
                    student_pref.query_results[curr_query_num - 1] = int(answer[:-1])

                elif curr_query_num == 3:
                    range_bounds = answer[:-1].split('-')

                    if len(range_bounds) == 2:
                        range_bounds[0] = int(range_bounds[0])
                        range_bounds[1] = int(range_bounds[1])

                        if (range_bounds[0] > range_bounds[1]):
                            temp = range_bounds[0]
                            range_bounds[0] = range_bounds[1]
                            range_bounds[1] = temp

                        student_pref.query_results[2] = range(*range_bounds)

                elif curr_query_num == 4:
                    crs_pairs = answer[:-1].split("), ")

                    for i in range(0, len(crs_pairs) - 1):
                        crs_pairs[i] += ')'

                    student_pref.query_results[3] = []
                    [student_pref.query_results[3].append(pair[1:-1].split(", ")) for pair in crs_pairs]

                else:
                    student_pref.query_results[4] = answer

                curr_query_num += 1

        return student_prog, student_pref
