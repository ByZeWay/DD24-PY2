class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self._pages = pages

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Количество страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        if not isinstance(duration, float):
            raise TypeError
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(duration)

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность: {self.duration} часов."




paper_book = PaperBook("название 1", "автор 1", 501)
audio_book = AudioBook("название 2", "автор 2", 10.5)

print(paper_book)
print(audio_book)
print()
print(repr(paper_book))
print(repr(audio_book))