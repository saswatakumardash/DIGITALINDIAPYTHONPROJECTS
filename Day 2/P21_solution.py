# Solution for P21

def main():
    # Taking input for the four assessments.

    quiz = int(input())
    exam = int(input())
    assignment = int(input())
    project = int(input())

    # Calculate the GPA

    GPA = (float(quiz)/20)*0.15 + (float(exam)/100)*0.40 + (float(assignment)/100)*0.20 + (float(project)/50)*0.25
    GPA = GPA*10 # Multiplying by 10 as we have to calculate the GPA out of 10
    GPA = round(GPA,2)

    # Printing the answer
    print(GPA)

# calling the main function
if __name__ == "__main__":
    main()