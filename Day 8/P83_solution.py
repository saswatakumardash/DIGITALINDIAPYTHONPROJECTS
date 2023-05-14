# helper library functions
import pandas as pd
import sys, os, getpass

sys.path.insert(0, "..")  # add to search path to enable discovery of our module
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.misc import NaN, FIRST, SECOND, THIRD, FOURTH, SIXTH,\
    Event, InvalidInputException, create_empty_dataframe, clear, wait
from P83_helper import login_header, home_header, add_students_header, \
    update_records_header, display_records_header, multiple_records_header


class StudentGradingSystem(object):

    max_marks = [20, 100, 100, 50]          # for Quiz, Exam, Assignment, Project in order
    weightage = [0.15, 0.40, 0.20, 0.25]

    # database schema for storing student records
    column_names = ['Roll_No', 'Quiz', 'Exam', 'Assignment', 'Project', 'GPA', 'Grade']
    data_types = [str, float, float, float, float, float, str]   
    records_file_name = "results.csv"
    database = create_empty_dataframe(columns=column_names, dtypes=data_types)

    @classmethod
    def login(cls):
        cls.print_header(login_header)
        user_id = input("Enter user id: ")  # for student, it is roll no
        while user_id == "" or len(user_id) > 16:
            print("Please enter a valid UserID - non-blank and utmost 16 characters long.\n")
            user_id = input("Enter user id: ")  # for student, it is roll no
        pass_code = getpass.getpass(prompt="Enter pass code (can be blank): ")  # for a simple use-case it plays no role
        return switch_user_class.get(user_id, Student)(user_id, cls)  # call appropriate Class initializer

    @classmethod
    def validate_student_roll_no(cls, roll_no, database=None):
        """Raise an exception if roll_no not found in database."""

        if database is None:    database = cls.database  # default
        if database.loc[database['Roll_No'] == roll_no].empty:
            raise InvalidInputException("\nStudent doesn't exist in our records. Try adding them.")

    @classmethod
    def validate_and_parse_marks(cls, raw_input):
        """Validate and parse input marks."""
        
        try:    quiz, exam, assignment, project = [float(x) for x in raw_input]
        except: raise InvalidInputException("\nInvalid Input.")
        err_msg = ""
        if   quiz < 0:                          err_msg = "{} < 0".format(quiz)
        elif quiz > cls.max_marks[FIRST]:       err_msg = "{} > 20".format(quiz)
        elif exam < 0:                          err_msg = "{} < 0".format(exam)
        elif exam > cls.max_marks[SECOND]:      err_msg = "{} > 100".format(exam)
        elif assignment < 0:                    err_msg = "{} < 0".format(assignment)
        elif assignment > cls.max_marks[THIRD]: err_msg = "{} > 100".format(assignment)
        elif project < 0:                       err_msg = "{} < 0".format(project)
        elif project > cls.max_marks[FOURTH]:   err_msg = "{} > 50".format(project)
        if err_msg != "":  raise InvalidInputException("\nERROR: Invalid Marks " + err_msg)
        return quiz, exam, assignment, project

    @classmethod
    def create_student_row(cls, roll_no=NaN, quiz=NaN, exam=NaN, \
        assignment=NaN, project=NaN, gpa=NaN, grade=NaN):
        """Return a new Series (student row) based on input values."""
        return pd.Series([roll_no, quiz, exam, assignment, project, gpa, grade], index=cls.column_names)

    @classmethod
    def read_database_file(cls, input_file_name):
        """Read student records from a database file."""

        input_file_path = os.path.join(os.path.dirname(__file__), input_file_name)
        types_dict = dict()  # for reading appropriate types of entries from file
        for column_name, data_type in zip(cls.column_names, cls.data_types):
            types_dict[column_name] = data_type
        return pd.read_csv(input_file_path, dtype=types_dict)

    @classmethod
    def add_students_from_file(cls, user_id, header=add_students_header):
        """Add students records read from a database file."""

        cls.print_header(header, user_id)
        try:
            input_file_name = input(" _____________\n| Upload File |\n'''''''''''''''\n\nEnter filename: ")
            input_database = cls.read_database_file(input_file_name)
            cls.database = pd.concat((input_database, cls.database)).drop_duplicates('Roll_No')  # priority to input
            cls.database = cls.database.sort_values('Roll_No')
            cls.database.reset_index(drop=True, inplace=True)
            print("\nUpdated student records successfully.")
        except: print("\nError reading specified file.")
        wait()

    @classmethod
    def read_marks_from_file(cls, user_id):
        """Update student records read from a database file."""
        cls.add_students_from_file(user_id, update_records_header)

    @classmethod
    def add_students_manually(cls, user_id):
        """Add student records from user input."""

        cls.print_header(add_students_header, user_id)
        print(" ______________\n| Manual Entry |\n''''''''''''''''\n\nEnter -1 to return")
        while True:
            roll_no = input("\nEnter Roll No: ")
            if roll_no == "-1": break
            try:
                cls.validate_student_roll_no(roll_no)  # raises an exception if not found
                print("Student already exists.")  # comes here if roll no valid
            except:  # if not found in database, only then make an entry
                try:
                    if roll_no == "":   raise InvalidInputException("Roll No can't be empty.")
                    cls.database = cls.database.append(cls.create_student_row(roll_no=roll_no), ignore_index=True)
                    print("Roll number {} added.".format(roll_no))
                except Exception as e:
                    print(e)

    @classmethod
    def read_marks_manually(cls, user_id):
        """Update student records from user input."""

        while True:
            cls.print_header(update_records_header, user_id)
            roll_no = input(" ______________\n| Manual Entry |\n''''''''''''''''\n\nEnter -1 to stop\n\nEnter Roll No: ")
            if roll_no == "-1": break
            try:
                cls.validate_student_roll_no(roll_no)
                msg = "Enter {} Marks: "
                categories = ["Quiz", "Exam", "Assignment", "Project"]
                input_msg_prompts = [msg.format(x) for x in categories]
                raw_input = [input(x) for x in input_msg_prompts]
                quiz, exam, assignment, project = cls.validate_and_parse_marks(raw_input)
                student_row = cls.create_student_row(roll_no=roll_no, quiz=quiz, exam=exam, assignment=assignment, project=project)
                # find locations (rows) where roll_no exists (which will be one unique row) and set values for keys
                cls.database.loc[cls.database['Roll_No'] == roll_no, student_row.keys()] = student_row.values
                print("\nMarks for " + roll_no + " updated successfully.")
            except Exception as e:
                print(e)
            wait()

    @classmethod
    def display_single_record(cls, roll_no=None, user_id=None):
        """Display a student record read from records file."""
        
        cls.print_header(display_records_header, user_id)
        if roll_no is None:
            roll_no = input(" _______________\n| Single Record |\n'''''''''''''''''\n\nEnter Roll No: ")
        try:
            database = cls.read_database_file(cls.records_file_name)
            cls.validate_student_roll_no(roll_no, database)
            print("")
            print(database.loc[database['Roll_No'] == roll_no])
        except:
            print("\nRecord is not generated yet.")
        wait()

    @classmethod
    def display_multiple_records(cls, user_id):
        """Display all student records read from records file."""

        cls.print_header(multiple_records_header, user_id)
        try:
            database = cls.read_database_file(cls.records_file_name)
            start, size = 0, database.shape[FIRST]  # no of rows
            while True:
                end = min(start + 10, size)  # if in case start + 10 > size
                cls.print_header(multiple_records_header, user_id)
                if database.empty:  print("\nRecords are not generated yet")
                else:
                    print("Showing entries {} to {} of {}\n".format(start + 1, end, size))
                    print(database[start:end])  # display at most 10 records at a time
                choice = input("\nEnter Choice: ").lower()
                if choice == "n":  # next 10 entries
                    if start + 10 < size:  start += 10
                    else:
                        print("\nWe are at the end of records table.")
                        wait()
                elif choice == "p":  # previous 10 entries
                    if start - 10 >= 0:  start -= 10
                    else:
                        print("\nWe are at the beginning of records table.")
                        wait()
                elif choice == "b": break
                elif choice == "l": cls.logout()
                else:   cls.invalid_entry()
        except Exception as e:
            if isinstance(e, Event) or isinstance(e, InvalidInputException):
                raise e
            print("Records are not generated yet.")
            wait()

    @staticmethod
    def print_header(header, user_id=None):
        clear()
        if user_id is not None:
            print(header.format("Logged in as " + user_id))
        else:  # for login page
            print(header)

    @staticmethod
    def assign_grade(gpa):
        if   gpa == 10:               grade = "O"
        elif gpa >= 9 and gpa < 10:   grade = "A"
        elif gpa >= 8 and gpa < 9:    grade = "B"
        elif gpa >= 6.5 and gpa < 8:  grade = "C"
        elif gpa >= 5 and gpa < 6.5:  grade = "D"
        else:                         grade = "F"
        return grade

    @staticmethod
    def logout():
        clear()
        raise Event("\nSuccessfully Logged Out.\n")

    @staticmethod
    def invalid_entry():
        print("Invalid Choice: Please choose from among [] above.")
        wait()

class User(object):

    def __init__(self, id, grader):
        self.Id = id
        self.Grader = grader

    def display_record(self, roll_no=None):
        """Fetch and display student record(s)."""

        grader = self.Grader
        if roll_no is None:
            while True:
                grader.print_header(display_records_header, self.Id)
                choice = input("Enter Choice: ").lower()
                if choice == "s":    grader.display_single_record(user_id=self.Id)
                elif choice == "m":  grader.display_multiple_records(self.Id)
                elif choice == "b":  break
                elif choice == "l":  grader.logout()
                else:                grader.invalid_entry()
        else:
            grader.display_single_record(roll_no=roll_no, user_id=self.Id)

class Instructor(User):

    def add_students(self):
        """Add student records from file or user input."""

        grader = self.Grader
        while True:
            grader.print_header(add_students_header, self.Id)
            choice = input("Enter Choice: ").lower()
            if choice == "u":    grader.add_students_from_file(self.Id)
            elif choice == "m":  grader.add_students_manually(self.Id)
            elif choice == "b":  break
            elif choice == "l":  grader.logout()
            else:                grader.invalid_entry()

    def read_marks(self):
        """Update student records from file or user input."""

        grader = self.Grader
        while True:
            grader.print_header(update_records_header, self.Id)
            choice = input("Enter Choice: ").lower()
            if choice == "u":    grader.read_marks_from_file(self.Id)
            elif choice == "m":  grader.read_marks_manually(self.Id)
            elif choice == "b":  break
            elif choice == "l":  grader.logout()
            else:                grader.invalid_entry()

    def compute_gpa(self, assign=False):
        """Compute and update GPA/ assign Grade of student record."""

        grader = self.Grader
        grader.print_header(home_header, self.Id)
        if assign:  msg_prompt = " _____________\n| Compute GPA |\n'''''''''''''''\n\nEnter Roll No: "
        else:   msg_prompt = " ______________________________\n| Compute GPA and Assign Grade |\n''''''''''''''''''''''''''''''''\n\nEnter Roll No: "
        roll_no = input(msg_prompt)
        grader.validate_student_roll_no(roll_no)
        student_row = grader.database.loc[grader.database['Roll_No'] == roll_no].copy()
        student_row.fillna(value=0, inplace=True)
        tmp, marks = 0.0, student_row.values.tolist()[FIRST][SECOND:SIXTH]
        for i in range(4):
            tmp += (float(marks[i]) / grader.max_marks[i] * grader.weightage[i])
        student_row['GPA'] = gpa = round(tmp*10, 2)
        if assign:  student_row['Grade'] = grade = grader.assign_grade(gpa)
        else:       student_row['Grade'] = grade = NaN
        grader.database.loc[grader.database['Roll_No'] == roll_no] = student_row
        if assign:  return gpa, grade
        else:       return gpa

    def generate_records(self):
        """Dump in-memory student records to records file."""
        out_file_path = os.path.join(os.path.dirname(__file__), self.Grader.records_file_name)
        self.Grader.database.to_csv(out_file_path, index=False)

class Ta(Instructor):
    # can't simply override - as in that case the method per se would still accessible
    read_marks = property()  # a way to disable access to read_marks

class Student(User):
    # by directly extending User, any access to other methods is prevented
    def display_record(self):  # override so that they can only see their own record
        super().display_record(self.Id)  # for student, user_id is roll no

switch_user_class = {"admin": Instructor, "tutor": Ta}

def main():
    clear()
    grader = StudentGradingSystem
    try:    grader.database = grader.read_database_file(grader.records_file_name)
    except: print("\nCouldn't load database records, unable to find proper records file.")
    wait()
    user = grader.login()
    while True:
        grader.print_header(home_header, user.Id)
        choice = input("Enter Choice: ").lower()
        try:
            if choice == "a":  # Add Students
                user.add_students()
            elif choice == "c":  # Compute GPA
                gpa = user.compute_gpa()
                print("\nGPA updated to {}".format(gpa))
                wait()
            elif choice == "n":  # Compute GPA and Assign Grade
                gpa, grade = user.compute_gpa(assign=True)
                print("\nGPA updated to {}\nGrade updated to {}".format(gpa, grade))
                wait()
            elif choice == "u":  # Update Records
                user.read_marks()
            elif choice == "g":  # Generate Records
                grader.print_header(home_header, user.Id)
                user.generate_records()
                print("\n\nSuccesfully generated student records.")
                wait()
            elif choice == "d":
                user.display_record()
            elif choice == "l":  # Exit
                grader.logout()
            else:
                grader.invalid_entry()
        except Exception as e:
            if isinstance(e, InvalidInputException):
                print(e)
            elif isinstance(e, Event):
                print(e)
                break
            else:
                print("\nAccess Denied: You're not authorized to perform this operation.")
            wait()

if __name__ == "__main__":
    main()
