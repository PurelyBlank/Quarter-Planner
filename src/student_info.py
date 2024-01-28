from pathlib import Path

import requests
import json

class StudentProgress:

    def __init__(self):
        self.cats_and_courses = {"degree": list(), 
                                 "GE I": list(), "GE II": list(), "GE III": list(), "GE IV": list(),
                                 "GE Va": list(), "GE Vb": list(),
                                 "GE VI": list(), "GE VII": list(), "GE VIII": list()}
        
        self.counts_per_ge = {"GE I": 2, "GE II": 3, "GE III": 3, "GE IV": 3,
                              "GE V": 3, "GE VI": 3, "GE VII": 1, "GE VIII": 1}
        
    def __str__(self):
        student_prog_str = "Categories and Courses:\n"

        for category, courses in self.cats_and_courses.items():
            student_prog_str += category + ': ' + ', '.join(courses) + '\n'
        
        student_prog_str += "\nCounts Per GE:\n"

        for ge, count in self.counts_per_ge.items():
            student_prog_str += ge + ': ' + str(count) + '\n'

        return student_prog_str


class StudentPreferences:

    def __init__(self):
        # the below attribute is a stub that will be improved upon further knowing the requirements
        self.query_results = []

    def __str__(self):
        stringpref = "Preferences:\n"
        
        for result in self.query_results:
            stringpref += result + ", "

        return stringpref[:-2]

class InputParser:

    def __init__(self, query: str):
        self.taken_path = Path("src/txt/taken.txt")
        self.pref_path = Path("src/txt/pref.txt")

        split_query = query.split('PREF\n')
        taken_query = ""
        pref_query = ""
        
        if len(split_query) == 2:
            taken_query = split_query[0]
            pref_query = split_query[1]

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
                course_info = response.json()

                ge_list = course_info['ge_list']

                for ge in ge_list:
                    ge = ge.split(': ')[0]

                    student_prog.cats_and_courses[ge].append(course)

        with open(self.pref_path, mode='r', encoding='utf-8') as student_pref_file:
            for answer in student_pref_file:
                student_pref.query_results.append(answer[:-1])

        return student_prog, student_pref
