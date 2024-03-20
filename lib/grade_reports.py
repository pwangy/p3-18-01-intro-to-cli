#!/usr/bin/env python3

# cd to /lib
#$ chmod +x grade_reports.py
## ^^ makes the script inside grade_reports.py executable


## the class should also contain code to validate incoming input. t.ex: raise an error if grade isinstance is an empty string. check for a name followd by a single letter (regEx), etc
class GradeReporter:
    def __init__(self, grade):
        self.value = grade

# returns a final value for the CLI workflow
def create_grade_report(student_grades):
    with open('reports/grade_report.txt', 'w') as gr:
        for grade in student_grades:
            gr.write(grade + '\n')


### include code in this block which includes user input and calls to classes and functions
if __name__ == '__main__':
    grade = input(f'Student name, grade:')
    grade_object = GradeReporter(grade)
    print(create_grade_report(grade_object))
