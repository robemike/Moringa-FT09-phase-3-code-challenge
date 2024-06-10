from database.connection import get_db_connection 
from .article import Article

conn = get_db_connection()
cursor = conn.cursor()

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.name}>'
    
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
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, name_value):
        if hasattr(self, "name"):
            AttributeError("Name not changeable.")
        else:
            if not isinstance(name_value, str) and len(name_value) == 0:
                raise ValueError ("Name must be a non-empty sting.")
            self._name = name_value

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            SELECT *
            FROM articles
            WHERE author_id = ?
        """
        cursor.execute(sql, (self.id,))
        rows = cursor.fetchall()
        articles = []
        for row in rows:
            articles.append(Article.instance_from_db(row))
        return articles