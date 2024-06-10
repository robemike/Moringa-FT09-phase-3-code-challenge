from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'
    
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
        return self.title

    @title.setter
    def title(self, title_value):
        if hasattr(self, "title"):
            AttributeError("Title not changeable.")
        else:
            if not isinstance(title_value, str) and 5 <= len(title_value) <= 50:
                raise ValueError ("Title must be a non-empty sting.")
            self.title = title_value

    @classmethod
    def author(self):
        from author import Author 
        sql = """
        SELECT authors.name 
        FROM authors 
        INNER JOIN articles
        ON articles.author_id = authors.id
        """
        
