# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Working with Data Structures

"""
import random as rand

#global constants
N_STUDENTS = 10 #number of rows
N_SUBJECTS = 4  #number of columns



def create_and_display_ten_records_with_lists():
    """
    store result of 100 students in 4 subjects in a 2D list
    numbers are generated randomly
    
  
    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    
    student_marks = [ [None] * N_SUBJECTS for i in range(N_STUDENTS) ]
    
    #store marks (randomly generated)
    for i in range(N_STUDENTS):
        for j in range(N_SUBJECTS):
            student_marks[i][j] = rand.randint(0,100)
            
    #display marks
    for i in range(N_STUDENTS):
        print ("student id = ", i, end = ": ")
        for j in range(N_SUBJECTS):
            print(student_marks[i][j], " ", end = "")
        print("")
            
def create_and_display_ten_records_with_dict():
    """
    store result of 100 students in 4 subjects in a dictionary
    numbers are generated randomly
    
  
    Parameters
    ----------
    None

    Returns
    -------
    None
    """   
    student_marks = {}
    
    #store marks (randomly generated)
    for i in ('alex','ben','claire'):
        student_marks[i] = []
        for j in range(N_SUBJECTS):
            student_marks[i].append(rand.randint(0,100))
            
    #display marks
    for key in student_marks:
        print ("student id = ", key, end = ": ")
        for j in range(N_SUBJECTS):
            print(student_marks[key][j], " ", end = "")
        print("")
     
        
#main
print("output from create_and_display_ten_records_with_lists")
create_and_display_ten_records_with_lists()

print("output from create_and_display_ten_records_with_dicts")
create_and_display_ten_records_with_dict()


