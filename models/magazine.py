# class Magazine:
#     def __init__(self, id, name, category):
#         self.id = id
#         self.name = name
#         self.category = category

#     def __repr__(self):
#         return f'<Magazine {self.name}>'

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self,name = name
        self.category = category

    def __repr__(self):
        return f"<Magazine {self.name}>"

    @property
    def id(self):
        return self.id
    
    @id.setter
    def id(self, id):
        if type(id) is int:
            self._id = id
        else:
            raise ValueError (
                "Id must be an integer."
            )
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16 and Magazine.get_by_name(name):
            self._name = name
        else:
            raise ValueError (
                "Name must be a string between 2 and 16 characters referencing the Database."
            )
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError (
                "Category must be a non-empty string referencing the database."
            )

