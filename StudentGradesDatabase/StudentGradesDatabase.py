# entry point
def main():
    grades = {}
    while(True):
        # 1) print choices
        printChoices()
        # 2) wait for input user
        answer = raw_input('What would you like to do today? Enter a number:')
        if answer == '1':
            # 3) enterGrades
            enterGrades(grades)
        elif answer == '2':
            # 4) removeStudent
            removeStudent(grades)
        elif answer == '3':
            # 5) studentAverageGrade
            studentAverageGrade(grades)
        elif answer == '4':
            # 6) break if "Exit"
            break

# 1) print choices
def printChoices():
    print('Welcone to Student Grades Database')
    print('\n')
    print('[1] - Enter Grades')
    print('[2] - Remove Student')
    print('[3] - Student Average Grades') 
    print('[4] - Exit') 
# 3) enterGrades
def enterGrades(grades):
    # 3.1) ask the student's name
    studentName = raw_input('Enter the student\'s name:')
    # 3.2) ask a grade
    while(True):
        studentGrade = raw_input('Enter a grade:')
        if studentGrade.isdigit():
            if int(studentGrade) < 0 or int(studentGrade) > 100:
                print('Insert a number between 1 and 100, please!')
            else:
                break
        else:
            print('Insert a number, please!')
    # 3.3) insert the student (if not existing) in grades
    listGrades = []
    if grades and grades.has_key(studentName): # grades is not empty
        listGrades = grades[studentName]
    listGrades.append(int(studentGrade))
    grades[studentName] = listGrades
    # 3.4) print all the grades
    print grades

# 4) removeStudent
def removeStudent(grades):
    # 4.1) ask the student's name
    studentName = raw_input('Enter the student\'s name:')
    # 4.2) remove this student
    if grades.has_key(studentName):
        del grades[studentName]
    # 4.3) print all the grades
    print grades

# 5) studentAverageGrade
from numpy import average
def studentAverageGrade(grades):
    # 5.1) ask the student's name
    studentName = raw_input('Enter the student\'s name:')
    # 5.2) calculate the average of his/her grades
    if grades.has_key(studentName):
        print average(grades[studentName]) 

main()