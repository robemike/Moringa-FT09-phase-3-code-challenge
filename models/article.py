from database.connection import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

class Article:

    all = {}

    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}: Content: {self.content}, author_id: {self.author_id}, magazine_id: {self.magazine_id}>'
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        if not isinstance(id, int):
            raise ValueError(
                "ID must be of type integer."
            )
        self._id = id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, "title"):
            AttributeError("Title not changeable.")
        else:
            if not isinstance(title, str) and 5 <= len(title) <= 50:
                raise ValueError ("Title must be a non-empty sting.")
            self._title = title

    @property
    def content(self):
        return self._content
    
    @content.setter 
    def content(self, content):
        if not isinstance(content, str) and len(content) == 0:
            ValueError ("Article content must be a non-empty string.")
        self._content = content


    @property
    def author(self):
        from .author import Author 
        sql = """
        SELECT authors.id, authors.name
        FROM authors 
        INNER JOIN articles
        ON articles.author_id = authors.id
        WHERE articles.id = ? 
        """
        cursor.execute(sql, (self.author_id,))
        row = cursor.fetchone()
        if row:
            author_id, author_name = row
            return Author(author_id, author_name)
        else:
            return None
    
    @property
    def magazine(self):
        from models.magazine import Magazine
        sql = """
            SELECT magazines.id, magazines.name, magazines.category
            FROM magazines
            INNER JOIN articles 
            ON magazines.id = articles.magazine_id
            WHERE articles.id = ? 
        """
        cursor.execute(sql, (self.magazine_id,))
        row = cursor.fetchone()
        if row:
            magazine_id, magazine_name, magazine_category = row
            return Magazine(magazine_id, magazine_name, magazine_category)
        else:
            return None

    @classmethod
    def get_by_id(cls, article_id):
        """Get Article by id"""
        sql = """
            SELECT *
            FROM articles
            WHERE id = ?
        """
        cursor.execute(sql, (article_id,))
        row = cursor.fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def instance_from_db(cls, row):
        """Return an Article instance having the attribute values from the table row."""
        article = cls.all.get(row[0])
        if article:
            article.title = row[1]
            article.content = row[2]
            article.author_id = row[3]
            article.magazine_id = row[4]
        else:
            article = cls(row[0], row[1], row[2], row[3], row[4])
            article.id = row[0]
            cls.all[article.id] = article
        return article
        
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM articles
        """
        rows = cursor.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]