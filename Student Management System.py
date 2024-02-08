import os
import platform

students = []

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def display_menu():
    print("""
 --------------------------------------------------
|==================================================|
|====== Welcome To Student Management System ======|
|==================================================|
 --------------------------------------------------

 Enter :

 1 <= View Student's List
 2 <= Add New Student
 3 <= Search Student
 4 <= Remove Student
 5 <= Save Student List to File
 6 <= Load Student List from File
 7 <= Show Statistics
 8 <= Exit
         """)

def view_students():
    if students:
        print("\nList Students\n")
        for idx, student in enumerate(students, start=1):
            print(f"{idx}. {student}")
    else:
        print("\nNo students in the database.")

def add_student():
    while True:
        new_student = input("\nEnter new student's name (or press Enter to exit): ").strip()
        if not new_student:
            break
        if any(char.isdigit() for char in new_student):
            print("\nStudent name cannot contain numbers.")
        elif new_student.lower() in [s.lower() for s in students]:
            print(f"\nStudent '{new_student}' already exists in the database.")
        else:
            students.append(new_student)
            print(f"\n=> New student '{new_student}' successfully added.")
            view_students()

def search_student():
    search_query = input("Enter student's name to search: ").strip()
    if search_query:
        found = [student for student in students if student.lower() == search_query.lower()]
        if found:
            print(f"\n=> Record found for '{found[0]}'")
        else:
            print(f"\n=> No record found for '{search_query}'")
    else:
        print("\nSearch query cannot be empty.")

def remove_student():
    remove_query = input("Enter student name to remove: ").strip()
    if remove_query:
        found = [student for student in students if student.lower() == remove_query.lower()]
        if found:
            confirmation = input(f"Are you sure you want to delete '{found[0]}'? (Y/N): ").strip().lower()
            if confirmation == 'y':
                students.remove(found[0])
                print(f"\n=> Student '{found[0]}' successfully deleted.")
                view_students()
            else:
                print("\nDeletion canceled.")
        else:
            print(f"\nNo record found for '{remove_query}'")
    else:
        print("\nStudent name cannot be empty.")

def save_students_to_file():
    file_name = input("Enter file name to save students (e.g., students.txt): ").strip()
    if file_name:
        try:
            with open(file_name, 'w') as file:
                for student in students:
                    file.write(student + '\n')
            print(f"\nStudent list successfully saved to '{file_name}'.")
        except Exception as e:
            print(f"\nError occurred while saving: {e}")
    else:
        print("\nFile name cannot be empty.")

def load_students_from_file():
    file_name = input("Enter file name to load students from (e.g., students.txt): ").strip()
    if file_name:
        if os.path.exists(file_name):
            try:
                with open(file_name, 'r') as file:
                    lines = file.readlines()
                    students.clear()
                    for line in lines:
                        students.append(line.strip())
                print(f"\nStudent list successfully loaded from '{file_name}'.")
                view_students()
            except Exception as e:
                print(f"\nError occurred while loading: {e}")
        else:
            print(f"\nFile '{file_name}' does not exist.")
    else:
        print("\nFile name cannot be empty.")

def show_statistics():
    total_students = len(students)
    if total_students > 0:
        print(f"\nTotal number of students: {total_students}")
        print(f"First student: {students[0]}")
        print(f"Last student: {students[-1]}")
        print(f"Alphabetically sorted students: \n {'\n '.join(sorted(students))}")
    else:
        print("\nNo students in the database.")

def manage_student():
    while True:
        display_menu()
        try:
            user_input = int(input("\nSelect an option from above: "))
            if user_input == 1:
                view_students()
            elif user_input == 2:
                add_student()
            elif user_input == 3:
                search_student()
            elif user_input == 4:
                remove_student()
            elif user_input == 5:
                save_students_to_file()
            elif user_input == 6:
                load_students_from_file()
            elif user_input == 7:
                show_statistics()
            elif user_input == 8:
                print("\nGoodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("\nIt's not a number. Please try again.")

# Run the student management system
manage_student()
