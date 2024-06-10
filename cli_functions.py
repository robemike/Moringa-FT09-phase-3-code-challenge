from models.article import Article
from models.author import Author

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
            print(f"The author of the article (ID: {article_id}) is: {author}")
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

def authors_aticles():
    pass

def magazines_articles():
    pass

def magazines_contributors():
    pass


