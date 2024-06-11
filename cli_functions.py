from models.article import Article
from models.author import Author
from models.magazine import Magazine
from database.connection import get_db_connection

def exit_program():
    print("Exiting the Program.")
    exit()

def list_articles():
    articles = Article.get_all()
    for article in articles:
        print(article)

def get_author_by_article_id():
    article_id = input("Enter the Article ID: ")
    article = Article.get_by_id(article_id)
    if article:
        author = article.author
        if author:
            print(f"The author of the article [{article.title} (ID: {article_id})] is: {author}")
        else:
            print(f"No author found for the article with ID {article_id}.")
    else:
        print(f"No article found with ID {article_id}.")

def get_magazine_by_article_id():
    article_id = input("Enter the Article ID: ")
    article = Article.get_by_id(article_id)
    if article:
        magazine = article.magazine
        if magazine:
            print(f"The magazine associated with the article (ID: {article_id}) is: {magazine.name}")
        else:
            print(f"No magazine found for the article with ID {article_id}.")
    else:
        print(f"No article found with ID {article_id}.")

def get_articles_by_author_id():
    author_id = input("Enter the Author ID: ")
    author = Author(author_id, "") 
    articles = author.articles()
    if articles:
        print(f"Articles authored by Author ID {author_id}:")
        for article in articles:
            print(article)
    else:
        print(f"No articles found for Author ID {author_id}.")

def get_magazines_by_author_id():
    author_id = input("Enter the Author ID: ")
    author = Author(author_id, "")  
    magazines = author.magazines()
    if magazines:
        print(f"Magazines associated with Author ID {author_id}:")
        for magazine in magazines:
            print(magazine)
    else:
        print(f"No magazines found for Author ID {author_id}.")

def get_articles_by_magazine_id():
    magazine_id = input("Enter the Magazine ID: ")
    magazine = Magazine(magazine_id, "", "") 
    articles = magazine.articles()
    if articles:
        print(f"Articles associated with Magazine ID {magazine_id}:")
        for article in articles:
            print(article)
    else:
        print(f"No articles found for Magazine ID {magazine_id}.")

def get_contributors_by_magazine_id():
    magazine_id = input("Enter the Magazine ID: ")
    magazine = Magazine(magazine_id, "", "") 
    contributors = magazine.contributors()
    if contributors:
        print(f"Authors associated with Magazine ID {magazine_id}:")
        for contributor in contributors:
            print(contributor)
    else:
        print(f"No authors found for Magazine ID {magazine_id}.")

def add_items_to_database():
    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create an author
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    author_id = cursor.lastrowid # Use this to fetch the id of the newly created author

    # Create a magazine
    cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (magazine_name, magazine_category))
    magazine_id = cursor.lastrowid # Use this to fetch the id of the newly created magazine

    # Create an article
    cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                   (article_title, article_content, author_id, magazine_id))
    
    conn.commit()

    # Query the database for inserted records. 
    # The following fetch functionality should probably be in their respective models

    cursor.execute('SELECT * FROM magazines')
    magazines = cursor.fetchall()

    cursor.execute('SELECT * FROM authors')
    authors = cursor.fetchall()

    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()

    conn.close()

    # Display results
    print("\nMagazines:")
    for magazine in magazines:
        print(Magazine(magazine["id"], magazine["name"], magazine["category"]))

    print("\nAuthors:")
    for author in authors:
        print(Author(author["id"], author["name"]))

    print("\nArticles:")
    for article in articles:
        print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))



