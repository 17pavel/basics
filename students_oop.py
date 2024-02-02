from random import randint
from datetime import datetime
import xlsxwriter
import pandas as pd

STUDENTS_MARKS_FILE = "marks.xlsx"
ADMIN_ACCESS = "ADMIN_ACCESS"
STUDENT_ACCESS = "STUDENT_ACCESS"
INVALID_ACCESS = "INVALID_ACCESS"


class Authentication:
    def __init__(self, auth_data):
        self.auth_data = auth_data

    def check_is_registered(self):
        login = input("Введите логин: ").lower()
        password = input("Введите пароль: ")
        if login in self.auth_data:
            valid_password = self.auth_data[login][0]
            if password == valid_password:
                return self.auth_data[login][1], login
            else:
                return INVALID_ACCESS, login
        else:
            return INVALID_ACCESS, login


class Menu:
    def __init__(self, access_role, login):
        self.access_role = access_role
        self.login = login
        self.menu_options = {
            ADMIN_ACCESS: {
                1: self.show_avg_school,
                2: self.show_avg_student,
                0: self.exit_program,
            },
            STUDENT_ACCESS: {
                1: self.start_tests,
                2: self.show_marks,
                0: self.exit_program_and_save,
            },
        }

    def show_menu(self):
        while True:
            current_menu = self.menu_options[self.access_role]
            print(current_menu)
            chosen_menu = int(input("Choose a menu option: "))
            if chosen_menu in current_menu:
                current_menu[chosen_menu]()
            else:
                print("Invalid menu option")

    def exit_program(self):
        print("Goodbye")

    def exit_program_and_save(self):
        print("Exiting and saving data")
        save_data()

    def show_avg_school(self):
        to_print = "Average marks for all students:\n"
        counter = 1
        by_school_marks_sum = 0
        by_school_marks_count = 0
        for name, marks in students.items():
            marks = [mark[1] for mark in marks]
            to_print += f"{counter}. {name}: {sum(marks) / len(marks)}\n"
            by_school_marks_sum += sum(marks)
            by_school_marks_count += len(marks)
            counter += 1
        to_print += f"Average for the school: {round(by_school_marks_sum / by_school_marks_count, 2)}, total marks: {by_school_marks_count}"
        print(to_print)

    def show_avg_student(self):
        student_name = input("Enter student name: ").lower()
        if student_name in students.keys():
            to_print = f"All marks for student {student_name}:\n"
            marks = []
            for counter, mark in enumerate(students[student_name]):
                to_print += f"{counter + 1}. {mark[1]} -> {mark[0]}\n"
                marks.append(mark[1])
            print(to_print)
            print(f"Average mark: {round(sum(marks) / len(marks), 2)}")
        else:
            print(f"No student with the name {student_name} exists")

    def start_tests(self):
        mark = 0
        for i in range(5):
            try:
                question, answer = generate_test()
                print(f"Solve the question: {question}")
                user_answer = int(input("Answer: "))
                if answer == user_answer:
                    mark += 2
            except Exception as e:
                print("You entered an invalid answer and lost a chance to earn a mark")
        if self.login in students:
            students[self.login].append((datetime.now(), mark))
        else:
            students[self.login] = [(datetime.now(), mark)]

    def show_marks(self):
        to_print = f"All marks for student {self.login}:\n"
        marks = []
        for counter, mark in enumerate(students[self.login]):
            to_print += f"{counter + 1}. {mark[1]} -> {mark[0]}\n"
            marks.append(mark[1])
        print(to_print)
        print(f"Average mark: {round(sum(marks) / len(marks), 2)}")


def generate_test():
    number1 = randint(1, 10)
    sign = ("+", "-", "*")[randint(0, 2)]
    number2 = randint(1, 10)
    question = f"{number1} {sign} {number2}"
    answer = eval(question)
    return question, answer


def save_data():
    workbook = xlsxwriter.Workbook(STUDENTS_MARKS_FILE)
    bold = workbook.add_format({"bold": True})
    for student, marks in students.items():
        worksheet = workbook.add_worksheet(student)
        worksheet.write("A1", "Date", bold)
        worksheet.write("B1", "Mark", bold)
        line = 2
        for mark in marks:
            worksheet.write(f"A{line}", str(mark[0])[:16])
            worksheet.write(f"B{line}", mark[1])
            line += 1
    workbook.close()


def load_students():
    data = pd.ExcelFile(STUDENTS_MARKS_FILE)
    for sheet in data.sheet_names:
        df = pd.read_excel(data, sheet)
        marks = df.values.tolist()
        students[sheet] = list(
            map(lambda el: (datetime.strptime(el[0], "%Y-%m-%d %H:%M"), el[1]), marks)
        )


def run_program():
    load_students()
    auth = Authentication(auth_data)
    access_role, login = auth.check_is_registered()
    if access_role == INVALID_ACCESS:
        print("Invalid login or password")
    else:
        menu = Menu(access_role, login)
        menu.show_menu()


students = {}
auth_data = {
    "admin": ("12345", ADMIN_ACCESS),
    "мария": ("12345", STUDENT_ACCESS),
    "иван": ("12345", STUDENT_ACCESS),
    "георгий": ("12345", STUDENT_ACCESS),
}

run_program()
