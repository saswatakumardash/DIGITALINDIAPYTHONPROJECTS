# solution for  P42
# checking for the valididy of the marks entered 
def read_marks(quiz,exam,assignment,project):
    if quiz < 0:
        print("ERROR: Invalid Marks {} < 0".format(quiz))
        return False,None,None,None,None
    elif quiz > 20:
        print("ERROR: Invalid Marks {} > 20".format(quiz))
        return False,None,None,None,None
    elif exam < 0:
        print("ERROR: Invalid Marks {} < 0".format(exam))
        return False,None,None,None,None
    elif exam > 100:
        print("ERROR: Invalid Marks {} > 100".format(exam))
        return False,None,None,None,None
    elif assignment < 0:
        print("ERROR: Invalid Marks {} < 0".format(assignment))
        return False,None,None,None,None
    elif assignment > 100:
        print("ERROR: Invalid Marks {} > 100".format(assignment))
        return False,None,None,None,None
    elif project < 0:
        print("ERROR: Invalid Marks {} < 0".format(project))
        return False,None,None,None,None
    elif project > 50:
        print("ERROR: Invalid Marks {} > 50".format(project))
        return False,None,None,None,None
    else:
        return True,quiz,exam,assignment,project

# computing GPA of the valid marks
def compute_gpa(quiz,exam,assignment,project):
    GPA = (float(quiz)/20)*0.15 + (float(exam)/100)*0.40 + (float(assignment)/100)*0.20 + (float(project)/50)*0.25
    GPA = GPA*10 # Multiplying by 10 as we have to calculate out of 10
    GPA = round(GPA,2)
    return GPA

# assigning grade according to the GPA
def assign_grade(gpa):
    if gpa==10:
        return "O"
    elif gpa>=9 and gpa<10:
        return "A"
    elif gpa>=8 and gpa<9:
        return "B"
    elif gpa>=6.5 and gpa<8:
        return "C"
    elif gpa>=5 and gpa<6.5:
        return "D"
    else:
        return "F"


def main():
    # Take the input
    quiz = int(input())
    exam = int(input())
    assignment = int(input())
    project = int(input())
    # calling method to check the validity of the marks
    validity,quiz,exam,assignment,project=read_marks(quiz,exam,assignment,project)
    if validity==True:
        # If marks are valid , then pass the marks to below method to compute GPA
        gpa=compute_gpa(quiz,exam,assignment,project)
        # assigning grades
        grade=assign_grade(gpa)
        print("The GPA is {}, and the Grade is {}".format(gpa,grade))

if __name__ == "__main__":
    main()
    
   