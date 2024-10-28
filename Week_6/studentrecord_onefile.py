# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:00:19 2023

@author: IMartin
"""

# Student record class
# This class contains basic data for an individual student
# and contains funtionality to calculate GPA from grades
class StudentRecord:
    
    # we fist define class attributes
    name = ""                #  set default name to empty 
    student_id = None        #  set default student id to None
    course = None            #  set default course of study to None
    year = None              #  set default year of study to None
    marks = []               #  default student has no marks
    
    # now we define actions on each student record
    # these are methods (member function) for this class
    
    # constructor 
    def __init__(self, name, student_id, course, year, marks):
        self.name = name
        self.student_id = student_id
        self.course = course
        self.year = year
        self.marks = marks
        
        # Define a function for our class 
    def output(self):
        print("Name : {:30s}".format(self.name))
        print("Student id number : {:10d}".format(self.student_id))
        print("Course of study : {:s}".format(self.course))
        print("Year of study : {:4d}".format(self.year))
        print("All marks : ", end = '')
        for mark in self.marks:
            print("{:1s}".format(mark.upper()), end = " ")
        print()
        
        # Add a mark
    def add_mark(self, mark):
        if mark in 'ABCDF':
            self.marks.append(mark)
        else:
            print('Mark {} is not a valid mark.'.format(mark))
    
    # Compute average mark
    def average_mark(self):
        mark_values = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        avg_mark = 0.0
        for mark in self.marks:
            avg_mark += mark_values[mark]
        return avg_mark/len(self.marks)
    
    


student_1 = StudentRecord('John Smith', 17110002,'physics',2,['A','A','B','A','C'])
student_2 = StudentRecord('Jill Smith', 17110003,'chemistry',2,['A','A','A','A','B'])
student_1.output()
student_2.output()
print('Student {:s} has average mark {:.2f}.'.format(student_1.name, student_1.average_mark()))
print('Student {:s} has average mark {:.2f}.'.format(student_2.name, student_2.average_mark()))