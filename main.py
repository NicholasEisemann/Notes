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
    command = input("Пожалуйста, введите команду: ")


""" Функция которая возвращает пользователю итог ввода команды """


def command_user():
    if command.lower() == "add notes":
        add_notes()
    elif command.lower() == "items":
        show_user_items()
    elif command.lower() == "help":
        help_user()
    elif command.lower() == "exit":
        print("GoodBye!")
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
    teg = str(input("Введите тему: "))
    text = str(input("Введите текст заметки: "))
    com_orders = (teg, text)
    cur.execute("INSERT INTO notes VALUES(?, ?);", com_orders)
    conn.commit()
    print(f"Готово! Заметка с именем - {teg} сохранена!")


""" Возвращает полный список названия заметок с их текством """


def show_user_items():
    for value in cur.execute("SELECT * FROM notes;"):
        print(value)


""" Возвращает список всех доступных команд """


def help_user():
    print("Command: \n"
          "add notes - Для добавления новой заметки\n"
          "items - Для вывода всех заметок и их текста\n"
          "del - Для удаления заметки\n"
          "edit - Для редактирования текста заметки\n"
          "exit - Хочу выйти")


""" Функция удаления заметки """


def notes_del():
    key_item = str(input("Какую заметку вы хотите удалить? "))
    if key_item == "not del":
        print("Хорошо, возвращаюсь обратно...")
    else:
        cur.execute(f"SELECT teg FROM notes WHERE teg = '{key_item}'")
        if cur.fetchone() is None:
            print("У вас нет такой заметки")
            notes_del()
        else:
            cur.execute(f"DELETE FROM notes WHERE teg = '{key_item}'")
            conn.commit()
            print(f"Заметка - {key_item} была удалена")


""" Функция редактирования заметки """


def edit_notes():
    notes_item = str(input("Какую заметку вы хотите редактировать? "))
    if notes_item == "not edit":
        print("Хорошо, возвращаюсь обратно...")
    cur.execute(f"SELECT teg FROM notes WHERE teg = '{notes_item}'")
    if cur.fetchone() is None:
        print("У вас нет такой заметки")
        edit_notes()
    else:
        edit_note = str(input("Введите текст: "))
        cur.execute(f"UPDATE notes SET note = '{edit_note}' WHERE teg = '{notes_item}'")
        conn.commit()
        print(f"Заметка {notes_item} была изменена")

x = True

while x:
    input_user()
    command_user()
    if command == "exit":
        break
