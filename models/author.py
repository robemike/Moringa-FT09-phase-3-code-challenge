# class Author:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

#     def __repr__(self):
#         return f'<Author {self.name}>'

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Author {self.name}>"
    
    @property 
    def id_(self):
        return self._id_

    @id_.setter
    def id(self, id_):
        if type(id_) is int:
            self._id_ = id_
        else:
            raise ValueError (
                "id must be an integer/ number."
            )
        
    @property 
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and Author.get_by_name(name):
            self._name = name
        else:
            raise (
                "Name must be a non_empty string referencing the database instance."
            )