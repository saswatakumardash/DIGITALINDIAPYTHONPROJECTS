# Solution for P31
def main():
    # Taking input for the four assessments.
    quiz = int(input())
    exam = int(input())
    assignment = int(input())
    project = int(input())

    # Validating marks for computing GPA:
    if quiz < 0:
        print("ERROR: Invalid Marks {} < 0".format(quiz))
    elif quiz > 20:
        print("ERROR: Invalid Marks {} > 20".format(quiz))
    elif exam < 0:
        print("ERROR: Invalid Marks {} < 0".format(exam))
    elif exam > 100:
        print("ERROR: Invalid Marks {} > 100".format(exam))
    elif assignment < 0:
        print("ERROR: Invalid Marks {} < 0".format(assignment))
    elif assignment > 100:
        print("ERROR: Invalid Marks {} > 100".format(assignment))
    elif project < 0:
        print("ERROR: Invalid Marks {} < 0".format(project))
    elif project > 50:
        print("ERROR: Invalid Marks {} > 50".format(project))
    

if __name__ == "__main__":
    main()
