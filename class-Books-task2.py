class Book:
    def __init__(self, book_title, author, year):
        self._book_title = book_title
        self._author = author
        self._year = year

    @property
    def title(self):
        return self._book_title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    def get_info(self):
        print(f'Название книги: {self.title}')
        print(f'Автор: {self.author}')
        print(f'Год издания: {self.year}')


pp = Book('Преступление и наказание', 'Достоевский Ф.М.', 1885)
pp.get_info()
