import sqlite3
from prettytable import from_db_cursor
from datetime import datetime, date, time

""" Подключаемся к SQL """

conn = sqlite3.connect("orders.db")
cur = conn.cursor()

""" Создаем базу данных """

cur.execute("""CREATE TABLE IF NOT EXISTS notes(
    date DATETIME,
    title TEXT,
    note TEXT);
""")
conn.commit()


def input_user():
    global command
    command = input("\033[34mПожалуйста, введите команду: \033[0m")


""" Функция которая возвращает пользователю итог ввода команды """


def command_user():
    if command.lower() == "добавить":
        add_notes()
    elif command.lower() == "заметки":
        show_user_items()
    elif command.lower() == "помоги":
        help_user()
    elif command.lower() == "выйти":
        print("\033[36m\033[1mЗакрываюсь...\033[0m")
    elif command.lower() == "удалить":
        notes_del()
    elif command.lower() == "редактировать":
        edit_notes()
    else:
        print("Вы ввели не правильную команду...\n"
              "Для справки и вывода основных команд используйте команду: >>> помоги ")


""" Данная функция сохраняет ввод
    от пользователя в базу данных """


def add_notes():
    date = datetime.now()
    title = str(input("\033[34mВведите тему: \033[0m"))
    text = str(input("\033[34mВведите текст заметки: \033[0m"))
    com_orders = (date, title, text)
    cur.execute("INSERT INTO notes VALUES(?, ?, ?);", com_orders)
    conn.commit()
    print(f"Готово! Заметка с именем - \033[32m{title}\033[0m сохранена!")


""" Возвращает полный список названия заметок с их текством """


def show_user_items():
    cur.execute("SELECT * FROM notes;")
    my_table = from_db_cursor(cur)
    print(my_table)


""" Возвращает список всех доступных команд """


def help_user():
    print("Команды: \n"
          "добавить - Для добавления новой заметки\n"
          "заметки - Для вывода всех заметок и их текста\n"
          "удалить - Для удаления заметки\n"
          "редактировать - Для редактирования текста заметки\n"
          "назад - Для выхода из редактиравания или удаления\n"
          "выйти - Хочу выйти")


""" Функция удаления заметки """


def notes_del():
    title_item = str(input("\033[34mКакую заметку вы хотите удалить? \033[0m"))
    if title_item == "назад":
        print("\033[35mХорошо, возвращаюсь обратно...\033[0m")
    else:
        cur.execute(f"SELECT title FROM notes WHERE title = '{title_item}'")
        if cur.fetchone() is None:
            print("\033[31mУ вас нет такой заметки\033[0m")
            notes_del()
        else:
            cur.execute(f"DELETE FROM notes WHERE title = '{title_item}'")
            conn.commit()
            print(f"Заметка - \033[31m{title_item}\033[0m была удалена")


""" Функция редактирования заметки """


def edit_notes():
    notes_item = str(input("\033[34mКакую заметку вы хотите редактировать? \033[0m"))
    if notes_item == "назад":
        print("\033[35mХорошо, возвращаюсь обратно...\033[0m")
    else:
        cur.execute(f"SELECT title FROM notes WHERE title = '{notes_item}'")
        if cur.fetchone() is None:
            print("\033[31mУ вас нет такой заметки\033[0m")
            edit_notes()
        else:
            edit_note = str(input("\033[34mВведите текст: \033[0m"))
            cur.execute(f"UPDATE notes SET note = '{edit_note}' WHERE title = '{notes_item}'")
            conn.commit()
            print(f"Заметка \033[33m{notes_item}\033[0m была изменена")

x = True

while x:
    input_user()
    command_user()
    if command == "выйти":
        break
