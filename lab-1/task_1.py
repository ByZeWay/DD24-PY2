import doctest

class Furniture:
    def __init__(self, material: str, dimensions: tuple):
        """
        Конструктор для класса Furniture.

        :param material: Материал мебели. Должен быть строкой и не пустым.
        :param dimensions: Размеры мебели в формате (длина, ширина, высота).
                           Каждый параметр должен быть положительным числом.
        :raises TypeError: Если material не строка или dimensions не кортеж.
        :raises ValueError: Если material пустой или dimensions размеры не положительные.

        Пример:
        >>> furniture = Furniture("Дерево", (2.0, 1.5, 0.8))
        """
        if not isinstance(material, str):
            raise TypeError
        if not material:
            raise ValueError("Материал не может быть пустым.")
        self.material = material

        if not isinstance(dimensions, tuple):
            raise TypeError
        if any(d <= 0 for d in dimensions):
            raise ValueError("Все размеры должны быть положительными числами.")
        self.dimensions = dimensions

    def move(self, new_location: str) -> None:
        """
        Переместить мебель в новое место.

        :param new_location: Новое местоположение мебели.
        :return: None

        Примеры:
        >>> furniture = Furniture("Дерево", (2.0, 1.5, 0.8))
        >>> furniture.move("Гостиная")
        """
        ...

    def assemble(self) -> None:
        """
        Собрать мебель.

        :return: None

        Примеры:
        >>> furniture = Furniture("Дерево", (2.0, 1.5, 0.8))
        >>> furniture.assemble()
        """
        ...


class Tree:
    def __init__(self, species: str, age: int):
        """
        Конструктор для класса Tree.

        :param species: Вид дерева. Должен быть строкой и не пустым.
        :param age: Возраст дерева в годах. Должен быть положительным целым числом.
        :raises TypeError: Если species не строка или age не число.
        :raises ValueError: Если species пустой или если age не положительное.

        Пример:
        >>> tree = Tree("Дуб", 10)
        """
        if not isinstance(species, str):
            raise TypeError
        if not species:
            raise ValueError("Вид дерева не может быть пустым.")
        self.species = species

        if not isinstance(age, int):
            raise TypeError
        if age <= 0:
            raise ValueError("Возраст дерева должен быть положительным целым числом.")
        self.age = age

    def grow(self) -> None:
        """
        Увеличить возраст дерева на один год.

        :return: None

        Примеры:
        >>> tree = Tree("Дуб", 10)
        >>> tree.grow()
        """
        ...

    def shed_leaves(self) -> None:
        """
        Сбросить листья дерева.

        :return: None

        Примеры:
        >>> tree = Tree("Дуб", 10)
        >>> tree.shed_leaves()
        """
        ...


class SocialMedia:
    def __init__(self, name: str, users_count: int):
        """
        Конструктор для класса SocialMedia.

        :param name: Название социальной сети. Должен быть строкой и не пустым.
        :param users_count: Количество пользователей. Должно быть неотрицательным целым числом.
        :raises TypeError: Если name не строка или users_count не число.
        :raises ValueError: Если name пустой или users_count отрицательный.

        Пример:
        >>> social_media = SocialMedia("Facebook", 1000000)
        """
        if not isinstance(name, str):
            raise TypeError
        if not name:
            raise ValueError("Название социальной сети не может быть пустым.")
        self.name = name

        if not isinstance(users_count, int):
            raise TypeError
        if users_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        self.users_count = users_count

    def post_update(self, content: str) -> None:
        """
        Опубликовать обновление.

        :param content: Содержимое обновления.
        :return: None

        Примеры:
        >>> social_media = SocialMedia("Facebook", 1000000)
        >>> social_media.post_update("Hello World!")
        """
        ...

    def add_user(self) -> None:
        """
        Добавить нового пользователя.

        :return: None

        Примеры:
        >>> social_media = SocialMedia("Facebook", 1000000)
        >>> social_media.add_user()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
