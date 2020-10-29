notes = {"First": "This is my first note"
         }

x = True


def input_user():
    global command
    command = input("Пожалуйста, введите команду: ")


""" Функция которая возвращает пользователю итог ввода команды """


def command_user():
    if command.lower() == "add notes":
        add_notes()
    elif command.lower() == "keys":
        show_user_keys()
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
    от пользователя в словарь notes """


def add_notes():
    teg = str(input("Введите тему: "))
    text = str(input("Введите текст заметки: "))
    notes[teg] = text
    print(f"Готово! Заметка с именем - {teg} сохранена!")


""" Возвращает все ключи пользователю """


def show_user_keys():
    for y in notes.keys():
        print(y)


""" Возвращает полный список названия заметок с их текством """


def show_user_items():
    for item in notes.items():
        print(item)


""" Возвращает список всех доступных команд """


def help_user():
    print("Command: \n"
          "add notes - Для добавления новой заметки\n"
          "keys - Для просмотра полного списка ключей\n"
          "items - Для вывода всех заметок и их текста\n"
          "del - Для удаления заметки\n"
          "edit - Для редактирования текста заметки\n"
          "exit - Хочу выйти")


""" Функция удаления заметки """


def notes_del():
    key_item = str(input("Какую заметку вы хотите удалить? "))
    if key_item in notes.keys():
        del notes[key_item]
        print(f"Заметка {key_item} удалена!")
    elif key_item == "not del":
        input_user()
    else:
        print("У вас нет такой заметки")
        notes_del()


""" Функция редактирования заметки """


def edit_notes():
    notes_item = str(input("Какую заметку вы хотите редактировать? "))
    if notes_item in notes.keys():
        edit_note = str(input("Введите текст: "))
        notes[notes_item] = edit_note
        print(f"Заметка {notes_item} была изменена")


while x:
    input_user()
    command_user()
    if command == "exit":
        break
