#module 2 lab if else while
#author - jbc
#last updated 220250122
#this program will allow the user to enter a students informaiton and adivse whether the student made the deans list or honor roll.

#get student informaiton
Lname = input("Please enter the student's last name or 'ZZZ' to quit: ")

#create loop and determine if the student is on the dean's list
while Lname != "ZZZ":
    Fname = input("Please enter the student's first name: ")
    gpa = float(input("Please enter the student's GPA: "))
    if gpa >= 3.5:
        print("Student has made the Deans list!")
    elif gpa >= 3.25:
        print("Student has made the Honor Roll!")

#request new student or quit
    Lname = input("Please enter the student's last name or 'ZZZ' to quit: ")
    
    

