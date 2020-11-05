import sqlite3

""" Подключаемся к SQL """

conn = sqlite3.connect("orders.db")
cur = conn.cursor()

""" Создаем базу данных """

cur.execute("""CREATE TABLE IF NOT EXISTS notes(
    teg TEXT,
    note TEXT);
""")
conn.commit()


def input_user():
    global command
    command = input("\033[34mПожалуйста, введите команду: \033[0m")


""" Функция которая возвращает пользователю итог ввода команды """


def command_user():
    if command.lower() == "add":
        add_notes()
    elif command.lower() == "items":
        show_user_items()
    elif command.lower() == "help":
        help_user()
    elif command.lower() == "exit":
        print("\033[36m\033[1mЗакрываюсь!\033[0m")
    elif command.lower() == "del":
        notes_del()
    elif command.lower() == "edit":
        edit_notes()
    else:
        print("Вы ввели не правильную команду...\n"
              "Для справки и вывода основных команд используйте команду: >>> help ")


""" Данная функция сохраняет ввод
    от пользователя в базу данных """


def add_notes():
    teg = str(input("\033[34mВведите тему: \033[0m"))
    text = str(input("\033[34mВведите текст заметки: \033[0m"))
    com_orders = (teg, text)
    cur.execute("INSERT INTO notes VALUES(?, ?);", com_orders)
    conn.commit()
    print(f"Готово! Заметка с именем - \033[32m{teg}\033[0m сохранена!")


""" Возвращает полный список названия заметок с их текством """


def show_user_items():
    for value in cur.execute("SELECT * FROM notes;"):
        print(value)


""" Возвращает список всех доступных команд """


def help_user():
    print("Command: \n"
          "add - Для добавления новой заметки\n"
          "items - Для вывода всех заметок и их текста\n"
          "del - Для удаления заметки\n"
          "edit - Для редактирования текста заметки\n"
          "exit - Хочу выйти")


""" Функция удаления заметки """


def notes_del():
    key_item = str(input("\033[34mКакую заметку вы хотите удалить? \033[0m"))
    if key_item == "not del":
        print("\033[35mХорошо, возвращаюсь обратно...\033[0m")
    else:
        cur.execute(f"SELECT teg FROM notes WHERE teg = '{key_item}'")
        if cur.fetchone() is None:
            print("\033[31mУ вас нет такой заметки\033[0m")
            notes_del()
        else:
            cur.execute(f"DELETE FROM notes WHERE teg = '{key_item}'")
            conn.commit()
            print(f"Заметка - \033[31m{key_item}\033[0m была удалена")


""" Функция редактирования заметки """


def edit_notes():
    notes_item = str(input("\033[34mКакую заметку вы хотите редактировать? \033[0m"))
    if notes_item == "not edit":
        print("\033[35mХорошо, возвращаюсь обратно...\033[0m")
    cur.execute(f"SELECT teg FROM notes WHERE teg = '{notes_item}'")
    if cur.fetchone() is None:
        print("\033[31mУ вас нет такой заметки\033[0m")
        edit_notes()
    else:
        edit_note = str(input("\033[34mВведите текст: \033[0m"))
        cur.execute(f"UPDATE notes SET note = '{edit_note}' WHERE teg = '{notes_item}'")
        conn.commit()
        print(f"Заметка \033[33m{notes_item}\033[0m была изменена")

x = True

while x:
    input_user()
    command_user()
    if command == "exit":
        break
