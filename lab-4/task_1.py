class Vehicle:
    """ Базовый класс для всех транспортных средств. """

    def __init__(self, name: str, model: str, year: int):
        """
        Инициализация транспортного средства.

        :param name: марка транспортного средства
        :param model: модель транспортного средства
        :param year: год выпуска
        """
        self.__name = name  # Приватный атрибут для инкапсуляции
        self.__model = model  # Приватный атрибут для инкапсуляции
        self.year = year

    def __str__(self) -> str:
        """Возвращает строковое представление транспортного средства."""
        return f"{self.__name} {self.__model}, {self.year}"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление транспортного средства."""
        return f"Vehicle(name='{self.__name}', model='{self.__model}', year={self.year})"

    def get_name(self) -> str:
        """Возвращает марку транспортного средства."""
        return self.__name

    def get_model(self) -> str:
        """Возвращает модель транспортного средства."""
        return self.__model

    def get_honk(self) -> str:
        """Издает звук гудка транспортного средства."""
        return f"{self.__name} издает звук \"БИИИП!\""


class Car(Vehicle):
    """ Класс для легковых автомобилей. """

    def __init__(self, name: str, model: str, year: int, doors: int):
        """
        Инициализация легкового автомобиля.

        :param name: марка легкового автомобиля
        :param model: модель легкового автомобиля
        :param year: год выпуска
        :param doors: количество дверей
        """
        super().__init__(name, model, year)  # Вызов конструктора базового класса
        self.doors = doors

    def __str__(self) -> str:
        """Возвращает строковое представление легкового автомобиля."""
        return f"{super().__str__()} с {self.doors} дверями"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление легкового автомобиля."""
        return f"Car(name='{self.get_name()}', model='{self.get_model()}', year={self.year}, doors={self.doors})"

    def get_honk(self) -> str:
        """Издает звук гудка легкового автомобиля. Метод перегружен поведения легкового автомобиля."""
        return f"{self.__str__()} издает звук \"Бип-Бип!\""


class Truck(Vehicle):
    """ Класс для грузовых автомобилей. """

    def __init__(self, name: str, model: str, year: int, capacity: float):
        """
        Инициализация грузового автомобиля.

        :param name: марка грузового автомобиля
        :param model: модель грузового автомобиля
        :param year: год выпуска
        :param capacity: грузоподъемность в тоннах
        """
        super().__init__(name, model, year)  # Вызов конструктора базового класса
        self.__capacity = capacity  # Приватный атрибут для инкапсуляции

    def __str__(self) -> str:
        """Возвращает строковое представление грузового автомобиля."""
        return f"{super().__str__()} с грузоподъемностью {self.__capacity} тонн"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление грузового автомобиля."""
        return f"Truck(name='{self.get_name()}', model='{self.get_model()}', year={self.year}, capacity={self.__capacity})"

    def load(self, weight: float) -> str:
        """Загружает груз в автомобиль.

        :param weight: вес груза в тоннах
        :return: сообщение о загрузке
        :raises ValueError: если вес груза превышает грузоподъемность
        """
        if weight > self.__capacity:
            raise ValueError("Превышена грузоподъемность!")
        return f"Грузоподъемность {weight} тонн."


if __name__ == "__main__":
    # Создание объектов классов
    car = Car("Toyota", "Camry", 2020, 4)
    truck = Truck("Fors", "Transit", 2019, 18)

    print(car)
    print(car.get_name())
    print(car.get_honk())

    print(truck)
    print(truck.get_model())
    print(truck.get_honk())
    print(truck.load(15))
