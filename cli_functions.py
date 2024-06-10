from models.article import Article

def exit_program():
    print("Exiting the Program.")
    exit()

def list_articles():
    articles = Article.get_all()
    for article in articles:
        print(article)

def author_of_an_article():

    pass

def magazine_of_an_article():
    pass

def authors_articles():
    pass

def authors_aticles():
    pass

def magazines_articles():
    pass

def magazines_contributors():
    pass


