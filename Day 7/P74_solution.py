# helper library functions
import pandas as pd
import numpy as np
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

# Function to process the first 2 rows of the csv and extract the total marks and the weight of each exam
def extract_total_and_weight(marks_df):
    # Extract the rows as lists, row 0 indicates total marks in each exam and row 1 indicates weight of each exam
    total = marks_df.iloc[0].to_list()
    weight = marks_df.iloc[1].to_list()

    # This is called slicing a list. We are keeping on indexs 1 to 4 inclusive, since others are not important
    total = total[1:5]
    weight = weight[1:5]

    # Since weight represents a percentage value we divide it by 100. This simplifies calculation in the future.
    for i in range(len(weight)):
        weight[i] = weight[i] / 100

    return total, weight

# This method reads the marks from the provided dataframe, processes them and calculates the GPA and grade and returns
# an updated dataframe. It takes 3 parameters, the  dataframe, total marks in each exam and weights of each exam.
def read_marks(result_df, total, weight):

    # Here we are replacing incorrect values (like marks being less than 0 or more than maximum marks) by 0
    # numpy's where method is like an if condition applied to entier arrays or dataframe columns. The first parameter
    # is a condition, the second parameter is the value to be returned if the conditions is true, and third  parameter
    # is the value to be returned if the condition is false. You can read more about numpy's where method online, here
    # is one link https://kanoki.org/2020/01/03/how-to-work-with-numpy-where/
    result_df['Quiz'] = np.where((result_df['Quiz'] < 0) | (result_df['Quiz'] > total[0]), 0, result_df['Quiz'])
    result_df['Exam'] = np.where((result_df['Exam'] < 0) | (result_df['Exam'] > total[1]), 0, result_df['Exam'])
    result_df['Assignment'] = np.where((result_df['Assignment'] < 0) | (result_df['Assignment'] > total[2]), 0, result_df['Assignment'])
    result_df['Project'] = np.where((result_df['Project'] < 0) | (result_df['Project'] > total[3]), 0, result_df['Project'])

    # Replacing missing values with 0
    result_df['Quiz'] = result_df['Quiz'].fillna(0)
    result_df['Exam'] = result_df['Exam'].fillna(0)
    result_df['Assignment'] = result_df['Assignment'].fillna(0)
    result_df['Project'] = result_df['Project'].fillna(0)

    # Initializing the Grade column
    result_df['Grade'] = ''

    for i, row in result_df.iterrows():
        if i < 2:
            continue
        gpa = compute_gpa(row, total, weight)
        result_df.at[i, 'GPA'] = gpa  # set the GPA of the current student
        grade = assign_grade(gpa)
        result_df.at[i, 'Grade'] = grade  # set the grade of the current student
    return result_df

# This method takes a pandas row having marks of a student, total marks and weights of each exam
# and returns the gpa of the student
def compute_gpa(row, total, weight):
    gpa = 0.0
    marks = row.iloc[1:5].to_numpy().tolist()

    for i in range(0, 4):
        tmp = (float(marks[i]) / total[i] * weight[i])
        gpa += tmp
    gpa *= 10
    gpa = round(gpa, 2)
    return gpa

# This method takes the gpa of a student as input and returns the assigned grade
def assign_grade(gpa):
    grade = ''

    if gpa == 10:
        grade = "O"
    elif gpa >= 9 and gpa < 10:
        grade = "A"
    elif gpa >= 8 and gpa < 9:
        grade = "B"
    elif gpa >= 6.5 and gpa < 8:
        grade = "C"
    elif gpa >= 5 and gpa < 6.5:
        grade = "D"
    else:
        grade = "F"
    return grade


def main():
    # Take the path to the marks.csv file as input and read the file in a pandas dataframe
    marks_file = input()
    marks_df = pd.read_csv(marks_file)

    # Make a copy of the marks dataframe. We will store the results (GPA and grade) in this copy.
    result_df = marks_df.copy()

    # Extract the first 2 rows
    total, weight = extract_total_and_weight(marks_df)

    # Calculate and fill the values of GPA and grades
    result_df = read_marks(result_df, total, weight)

    # Save the results in a result.csv file in the same location as that of marks.csv
    out_path = os.path.split(marks_file)[0] + os.sep + "result.csv"
    result_df.to_csv(out_path, index=False)


# This is required to ensure that we can import your solve function without activating other parts of code
if __name__ == "__main__":
    main()
