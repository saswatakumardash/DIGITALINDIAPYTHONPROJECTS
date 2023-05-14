######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import numpy as np
from scipy import linalg
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

########## USER CODE SECTION BEGIN #########


temp_records=dict()
final_records=dict()
total=[20,100,100,50]
weight=[0.15,0.4,0.2,0.25]


def add_student():
	roll=input()
	while roll!="-1":
		temp_records[roll]=[None,None,None]
		roll=input()



def read_marks():
    roll=input()
    if roll in temp_records:
        quiz=float(input())
        exam=float(input())
        assignment=float(input())
        project=float(input())
        if quiz < 0:
            print("ERROR: Invalid Marks {} < 0".format(quiz))
            return
        elif quiz > 20:
            print("ERROR: Invalid Marks {} > 20".format(quiz))
            return
        elif exam < 0:
            print("ERROR: Invalid Marks {} < 0".format(exam))
            return
        elif exam > 100:
            print("ERROR: Invalid Marks {} > 100".format(exam))
            return
        elif assignment < 0:
            print("ERROR: Invalid Marks {} < 0".format(assignment))
            return
        elif assignment > 100:
            print("ERROR: Invalid Marks {} > 100".format(assignment))
            return
        elif project < 0:
            print("ERROR: Invalid Marks {} < 0".format(project))
            return
        elif project > 50:
            print("ERROR: Invalid Marks {} > 50".format(project))
            return
        else:
            temp_records[roll][0]=[quiz,exam,assignment,project]
    else:
        print("ERROR: Student roll number does not exist")



def compute_gpa(roll):
    gpa=0.0
    marks=temp_records[roll][0]
    for i in range(0,4):
        gpa+=(float(marks[i])/total[i]*weight[i])
    gpa*=10
    gpa=round(gpa,2)
    temp_records[roll][1]=gpa



def assign_grade(roll):
    gpa=temp_records[roll][1]
    grade=''
    if gpa==10:
        grade="O"
    elif gpa>=9 and gpa<10:
        grade="A"
    elif gpa>=8 and gpa<9:
        grade="B"
    elif gpa>=6.5 and gpa<8:
        grade="C"
    elif gpa>=5 and gpa<6.5:
        grade="D"
    else:
        grade="F"
    temp_records[roll][2]=grade


def generate_records():
	final_records.update(temp_records)


def display_records():
	roll=input()
	if roll in final_records:
		print(final_records[roll][0])
		print(final_records[roll][1])
		print(final_records[roll][2])
	else:
		print("ERROR: Student roll number does not exist")



# This is required to ensure that we can import your solve function without activating other parts of code
def main():
    while True:
        code=int(input())
        if (code==1):
            add_student()
        elif (code==2):
            read_marks()
        elif (code==3):
            roll=input()
            if roll in temp_records:
                if temp_records[roll][0] is not None:
                    compute_gpa(roll)
                    assign_grade(roll)
                else:
                    print("ERROR: Student roll number marks information unavailable")
            else:
                print("ERROR: Student roll number does not exist")
        elif(code==4):
            generate_records()
        elif (code==5):
            display_records()
        elif (code==6):
            break
        else:
            print("ERROR: Invalid Command!")

if __name__ == "__main__":
    # Call the main function
    main()

######### USER CODE SECTION END #########
