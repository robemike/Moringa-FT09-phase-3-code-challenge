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
        return f'<Article {self.title}: Content: {self.content}, Author: {self.author_id}, Magazine: {self.magazine_id}>'
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id_value):
        if not isinstance(id_value, int):
            raise ValueError(
                "ID must be of type integer."
            )
        self._id = id_value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title_value):
        if hasattr(self, "title"):
            AttributeError("Title not changeable.")
        else:
            if not isinstance(title_value, str) and 5 <= len(title_value) <= 50:
                raise ValueError ("Title must be a non-empty sting.")
            self._title = title_value

    @property
    def author(self):
        from author import Author 
        sql = """
        SELECT authors.name
        FROM authors 
        INNER JOIN articles
        ON articles.author_id = authors.id
        WHERE articles.id = ? 
        """
        cursor.execute(sql, (self.author_id,))
        row = cursor.fetchone()
        return Author(row[1]) if row else None
    
    @property
    def magazine(self):
        from models.magazine import Magazine
        sql = """
            SELECT magazines.name
            FROM magazines
            INNER JOIN articles 
            ON magazines.id = articles.magazine_id
            WHERE article.id = ? 
        """
        cursor.execute(sql, (self.magazine_id,))
        row = cursor.fetchone()
        return Magazine(row[1]) if row else None
        
    def save(self):
        if self.id is None:
            sql = """
                INSERT INTO articles (title, content, author_id, magazine_id)
                VALUES (?,?,?,?)
            """
            cursor.execute(sql, (self.title, self.content, self.author_id, self.magazine_id))
            conn.commit()
            self.id = cursor.lastrowid
        else:
            sql = """
                UPDATE articles
                SET title =?, content =?, author_id =?, magazine_id =?
                WHERE id =?
            """
            cursor.execute(sql, (self.title, self.content, self.author_id, self.magazine_id, self.id))
            conn.commit()

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