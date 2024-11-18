# --------------------------------------------------------------------------- #
# Title:  Assignment 06
## Description: This Assignment 06 will collect information
# then display a message about a student's registration for
# a Python course. In this assignment we are using classes and functions.
#
# Change Log:
# 11/15/2024: Beginning script outline, adding functions,
# and rewriting the loops with functions.
# 11/16/2024: Addressing issues with function parameters, arguments
# and calls.
# 11/17/2024: Adding error handling and classes.  QC check.
#
#
# Kristie Dunkin       11/18/2024     Assignment 06
# ------------------------------------------------------------------------------- #
#
import json


# Define Constants:
FILE_NAME: str = "Enrollments.json"
MENU: str = '''
 ----Course Registration Program Menu-----
 1. Register a student for a course 
 2. Show current data 
 3. Save data to a file 
 4. Exit this program
 '''
FIRST_NAME_KEY: str = "First Name"
LAST_NAME_KEY: str = "Last Name"
COURSE_NAME_KEY: str = "Course Name"

# Define variables
menu_choice: str = ''
all_students_list: list[dict[str, str]] = [] #NOTE that this is the same as the assignment's "students".
exit_statement: str = "'Thank you. Goodbye.'" #I added this myself, not a requirement.

#Declare the class.
class FileProcessor:
    """Reads data from and writes data to JSON files for storage"""

    @staticmethod
    def output_error_messages(message:str):
        print(message)

    @staticmethod
    def read_data_from_file(file_json: str) -> list[dict]:
        """
        Opens a .json file in read mode. Reads information into memory using load.
        Note that the file must already exist.
        @rtype: object
        @param file_json: str
        @return: file
        """
        file_data: list
        try:
            with open(file_json, "r") as file:
                file_data = json.load(file)
                return file_data
        except FileNotFoundError as e:
            FileProcessor.output_error_messages("Sorry, your file was not found.")
            return [] #needed this because it was getting stuck here.
        except json.JSONDecodeError as e:
            FileProcessor.output_error_messages("There was an error decoding your file")

    @staticmethod
    def write_data_to_file(save_data: list, file_location: str):
        """
        Saves data to a .json file. using open in write mode "w" .
        Note this is using a with, which will close the file for us.
        Saved data is formated using 'indent = 2' to look like a table.
       @param save_data: list
       @param file_location: str
       """

        with open(file_location, "w") as file:
            json.dump(save_data, file, indent=2)

class IO:
    """
        A collection of functions that requests data, formats strings as
     dictionaries and outputs dictionaries to a list.
     """

    @staticmethod
    def input_student_data():
        """
        Accepts information entered by user as string and formats as a dictionary
        Appends it to a student_file as list[dict[str, str]].

        """
        while True:
            try:
                student_first_name = input("What is your first name? ").strip().title()
                if not student_first_name.isalpha():
                    raise Exception("Sorry, that was not a good first name")
                student_last_name = input("What is your last name? ").strip().title()
                if not student_last_name.isalpha():
                    raise Exception("Sorry, that was not a good last name")
                course_name = input(
                    "Please enter the name of the course: ").strip().title()  # pass
                if not course_name.isprintable():
                    raise Exception("Sorry, that was not a good course name")
                else:
                    break
            except Exception as e:
                 FileProcessor.output_error_messages("Please try again")
        student_data: dict[str, str] = {FIRST_NAME_KEY: student_first_name,
              LAST_NAME_KEY: student_last_name,
              COURSE_NAME_KEY: course_name}
        return student_data

    @staticmethod
    def output_student_courses(students_list: list):
        """
        Prints the list all_students_list, list[dict[str, str]].
        students_list: list
        """
        for student in students_list:
            print(f'{student[FIRST_NAME_KEY]} {student[LAST_NAME_KEY]} is '
                  f'signed up for {student[COURSE_NAME_KEY]}')


    """
    Provides opportunity for a student to register.
    
    """

    @staticmethod
    def input_menu_choice() -> str:
        """
        Used when menu choice is 1 to collect input
        returns the choice made.

        """
        print(MENU)
        choice: str = input(
            "Please make a choice from the menu above (1/2/3/4)  ")
        return choice

    @staticmethod
    def welcome_str_menu():
        """
       Prints a welcome statement and asks if the user would like to register for a course.

        """
        welcome_str = input(
            "Welcome! Would you like to register for a course? (Y/N)  ")
        if welcome_str.upper() == 'Y':
            return
        print(exit_statement)
        exit()


#This is where it all happens.
all_students_list = FileProcessor.read_data_from_file(FILE_NAME)
IO.welcome_str_menu()  # Provides a greeting and menu for input
while True:
    menu_choice = IO.input_menu_choice()
    if menu_choice == str(1):
        next_student_data = IO.input_student_data()
        all_students_list.append(next_student_data)
        print(all_students_list)
    elif menu_choice == str(2):
        IO.output_student_courses(all_students_list)
    elif menu_choice == str(3):
        FileProcessor.write_data_to_file(all_students_list, FILE_NAME)
        IO.output_student_courses(all_students_list)
    else:
        print(exit_statement)
        quit()
