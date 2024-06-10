class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.name}>'

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