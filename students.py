# +1. Вход по логину и паролю.
# +2. Выдать соотв. меню.
# +3. Ф-ция - генератор тестов
# +4. Ф-ция сохранения данных
# +5. Подгрузка отметок при запуске
# +6. Показать среднюю оценку по школе
# +7. Показать среднюю оценку по ученику
# +8. Показать оценки ученику

from random import randint
from datetime import datetime
import xlsxwriter
import pandas as pd

STUDENTS_MARKS_FILE = "marks.xlsx"
ADMIN_ACCESS = "ADMIN_ACCESS"
STUDENT_ACCESS = "STUDENT_ACCESS"
INVALID_ACCESS = "INVALID_ACCESS"

auth_data = {
    "admin": ("12345", ADMIN_ACCESS),
    "мария": ("12345", STUDENT_ACCESS),
    "иван": ("12345", STUDENT_ACCESS),
    "георгий": ("12345", STUDENT_ACCESS),
}

MENU = {
    ADMIN_ACCESS: {
        1: "Показать среднюю оценку по школе",
        2: "Показать среднюю оценку по ученику",
        0: "Выйти",
    },
    STUDENT_ACCESS: {1: "Пройти тест", 2: "Посмотреть оценки", 0: "Выйти и сохранить"},
}

students = {}


def check_is_registered():
    login = input("Введите логин: ").lower()
    password = input("Введите пароль: ")
    if login in auth_data:
        valid_password = auth_data[login][0]
        if password == valid_password:
            return auth_data[login][1], login
        else:
            return INVALID_ACCESS, login
    else:
        return INVALID_ACCESS, login


def show_menu(access_role, login):
    while True:
        current_menu = MENU[access_role]
        print(current_menu)
        chosen_menu = int(input("Выберите пункт меню: "))
        if access_role == ADMIN_ACCESS and chosen_menu == 0:
            print("До свидания")
            return
        elif access_role == STUDENT_ACCESS and chosen_menu == 0:
            print("Выход и сохранение")
            save_data()
            return
        elif access_role == ADMIN_ACCESS and chosen_menu == 1:
            show_avg_school()
        elif access_role == ADMIN_ACCESS and chosen_menu == 2:
            show_avg_student()
        elif access_role == STUDENT_ACCESS and chosen_menu == 1:
            start_tests(login)
        elif access_role == STUDENT_ACCESS and chosen_menu == 2:
            show_marks(login)
        else:
            print("Такого пункта нет")


def generate_test():
    number1 = randint(1, 10)
    sign = ("+", "-", "*")[randint(0, 2)]
    number2 = randint(1, 10)
    question = f"{number1} {sign} {number2}"
    answer = eval(question)
    return question, answer


def start_tests(login):
    mark = 0
    for i in range(5):
        try:
            question, answer = generate_test()
            print(f"Реши задачу: {question}")
            user_answer = int(input("Ответ: "))
            if answer == user_answer:
                mark += 2
        except Exception as e:
            print("Ты ввел ерунду и потерял попытку получить балл")

    if login in students:
        students[login].append((datetime.now(), mark))
    else:
        students[login] = [(datetime.now(), mark)]


def save_data():
    workbook = xlsxwriter.Workbook(STUDENTS_MARKS_FILE)
    bold = workbook.add_format({"bold": True})
    for student, marks in students.items():
        worksheet = workbook.add_worksheet(student)
        worksheet.write("A1", "Дата", bold)
        worksheet.write("B1", "Отметка", bold)
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
            map(lambda el: (datetime.strptime(
                el[0], "%Y-%m-%d %H:%M"), el[1]), marks)
        )


def show_avg_school():
    to_print = "Средний балл всех учеников:\n"
    counter = 1
    by_school_marks_sum = 0
    by_school_marks_count = 0
    for name, marks in students.items():
        marks = [mark[1] for mark in marks]
        to_print += f"{counter}. {name}: {sum(marks) / len(marks)}\n"
        by_school_marks_sum += sum(marks)
        by_school_marks_count += len(marks)
        counter += 1

    to_print += f"Средний по школе {round(by_school_marks_sum / by_school_marks_count, 2)}, всего {by_school_marks_count} отметок"
    print(to_print)


def show_avg_student():
    student_name = input("Введите имя ученика: ").lower()
    if student_name in students.keys():
        to_print = f"Все отметки ученика {student_name}:\n"
        marks = []
        for counter, mark in enumerate(students[student_name]):
            to_print += f"{counter + 1}. {mark[1]} -> {mark[0]}\n"
            marks.append(mark[1])
        print(to_print)
        print(f"Средний бал: {round(sum(marks) / len(marks), 2)}")
    else:
        print(f"Студента с именем {student_name} не существует")


def show_marks(login):
    to_print = f"Все отметки ученика {login}:\n"
    marks = []
    for counter, mark in enumerate(students[login]):
        to_print += f"{counter + 1}. {mark[1]} -> {mark[0]}\n"
        marks.append(mark[1])
    print(to_print)
    print(f"Средний бал: {round(sum(marks) / len(marks), 2)}")


def run_program():
    load_students()
    access_role, login = check_is_registered()
    show_menu(access_role, login)


run_program()
