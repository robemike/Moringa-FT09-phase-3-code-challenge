from database.connection import get_db_connection
from .article import Article
# from .author import Author

conn = get_db_connection()
cursor = conn.cursor()

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.name} >'

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id_value):
        if not isinstance(id_value, int):
            ValueError(
                "ID must be of type integer."
            )
        self._id = id_value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_value):
        if not isinstance(name_value, str) and 2 <= len(name_value) <= 16:
            raise ValueError ("Name must be a non-empty sting.")
        self._name = name_value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category_value):
        if not isinstance(category_value, str) and len(category_value) == 0:
            raise ValueError ("Category must be a non-empty sting.")
        self._category = category_value
        
    def articles(self):
        sql = """
            SELECT articles.id, articles.title, articles.content, articles.author_id
            FROM articles
            INNER JOIN magazines 
            ON magazines.id = articles.magazine_id
            WHERE magazines.id = ?
        """
        cursor.execute(sql, (self.id,))
        rows = cursor.fetchall()
        articles = []
        for row in rows:
            article_id, title, content, author_id = row
            articles.append(Article(article_id, title, content, author_id, self.id))
        return articles
    
    def contributors(self):
        from .author import Author
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            SELECT authors.id, authors.name
            FROM authors
            INNER JOIN articles 
            ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
        """
        cursor.execute(sql, (self.id,))
        rows = cursor.fetchall()
        authors = []
        for row in rows:
            author_id, author_name = row
            authors.append(Author(author_id, author_name))
        return authors