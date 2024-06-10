from database.setup import create_tables

from cli_functions import (
     exit_program,
     list_articles
)

def main():
    # Initialize the database and create tables
    create_tables()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
             exit_program()
        elif choice == "1":
             list_articles()
        

def menu():
        print("Select an option:")
        print("0. Exit the Program.")
        print("1. List all the Articles.")


if __name__ == "__main__":
    main()
