from database.setup import create_tables

from cli_functions import (
     exit_program,
     list_articles,
     get_author_by_article_id,
     get_magazine_by_article_id, 
     get_articles_by_author_id,
     get_magazines_by_author_id,
     get_articles_by_magazine_id,
     get_contributors_by_magazine_id,
     add_items_to_database
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
          elif choice == "2":
               get_author_by_article_id()
          elif choice == "3":
               get_magazine_by_article_id()
          elif choice == "4":
               get_articles_by_author_id()
          elif choice == "5":
               get_magazines_by_author_id()
          elif choice == "6":
               get_articles_by_magazine_id()
          elif choice == "7":
               get_contributors_by_magazine_id()
          elif choice == "8":
               add_items_to_database()
               pass
        
        

def menu():
        print("Select an option:")
        print("0. Exit the Program.")
        print("1. List all the Articles.")
        print("2. Author of an Article.")
        print("3. Magazine of a certain Article.")
        print("4. Articles of an Author.")
        print("5. Magazines associated with an author.")
        print("6. Get Articles in a Magazine.")
        print("7. Contributors of a magazine.")
        print("8. Add items to the Database.")


if __name__ == "__main__":
    main()
