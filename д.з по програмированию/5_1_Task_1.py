class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, name, value):
        if name == 'title' and not isinstance(value, str):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif name == 'author' and not isinstance(value, str):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif name == 'pages' and not isinstance(value, int):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif name == 'year' and not isinstance(value, int):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, name, value)

book = Book("OOP", "JK", 123, 2022)
