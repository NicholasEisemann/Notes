import sqlite3
from prettytable import from_db_cursor
from datetime import datetime, date, time

""" connecting to SQL """

conn = sqlite3.connect("orders.db")
cur = conn.cursor()

""" creating database """

cur.execute("""CREATE TABLE IF NOT EXISTS notes(
    date DATETIME,
    title TEXT,
    note TEXT);
""")
conn.commit()


def input_user():
    global command
    command = input("\033[34mPlease, input command: \033[0m")


""" A function that returns the result of the command input to the user  """


def command_user():
    if command.lower() == "add":
        add_notes()
    elif command.lower() == "items":
        show_user_items()
    elif command.lower() == "help":
        help_user()
    elif command.lower() == "exit":
        print("\033[36m\033[1mGoodBye!\033[0m")
    elif command.lower() == "del":
        notes_del()
    elif command.lower() == "edit":
        edit_notes()
    else:
        print("You input not correct command...\n"
              "To display all commands, use input: >>> help ")


""" This function saves the input
     from user in database """


def add_notes():
    date = datetime.now()
    title = str(input("\033[34mInput title: \033[0m"))
    text = str(input("\033[34mIntup text note: \033[0m"))
    com_orders = (date, title, text)
    cur.execute("INSERT INTO notes VALUES(?, ?, ?);", com_orders)
    conn.commit()
    print(f"Done! Title note - \033[32m{title}\033[0m saved!")


""" Returns a complete list of notes """


def show_user_items():
    cur.execute("SELECT * FROM notes;")
    my_table = from_db_cursor(cur)
    print(my_table)

""" Returns a list of all available commands """


def help_user():
    print("Command: \n"
          "add - For adding new note\n"
          "items - Returns a complete list of notes\n"
          "del - For delete note\n"
          "edit - For edit text\n"
          "exit - For turn off app")


""" delete note """


def notes_del():
    title_item = str(input("\033[34mWhich note do you want to delete? \033[0m"))
    if title_item == "not del":
        print("\033[35mOkay, going back...\033[0m")
    else:
        cur.execute(f"SELECT title FROM notes WHERE title = '{title_item}'")
        if cur.fetchone() is None:
            print("\033[31mYou don't have this note\033[0m")
            notes_del()
        else:
            cur.execute(f"DELETE FROM notes WHERE title = '{title_item}'")
            conn.commit()
            print(f"Note - \033[31m{title_item}\033[0m has been deleted")


""" Note editing function """


def edit_notes():
    notes_item = str(input("\033[34mWhich note do you want to edit? \033[0m"))
    if notes_item == "not edit":
        print("\033[35mOkay, going back...\033[0m")
    else:
        cur.execute(f"SELECT title FROM notes WHERE title = '{notes_item}'")
        if cur.fetchone() is None:
            print("\033[31mYou don't have this note\033[0m")
            edit_notes()
        else:
            edit_note = str(input("\033[34mInput text: \033[0m"))
            cur.execute(f"UPDATE notes SET note = '{edit_note}' WHERE title = '{notes_item}'")
            conn.commit()
            print(f"Note \033[33m{notes_item}\033[0m has been edited")

x = True

while x:
    input_user()
    command_user()
    if command == "exit":
        break
