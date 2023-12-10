import doctest
from typing import Union


class Phone:
    """
    Класс Телефон.
    """
    def __init__(self, charge: int, brightness: int):
        """
        Создание и подготовка к работе объекта "Телефон".

        :param charge: Число заряда
        :param brightness: Яркость экрана

        Примеры:
        >>> phone = Phone(18, 50)  # инициализация экземпляра класса
        """
        if not isinstance(charge, int):
            raise TypeError("Ожидается число")
        if charge < 0:
            raise ValueError("Заряд должен быть неотрицательным числом")
        self.charge = charge

        if not isinstance(brightness, int):
            raise TypeError("Ожидается число")
        if brightness < 0:
            raise ValueError("Яркость должна быть неотрицательным числом")
        self.brightness = brightness

    def charging(self) -> bool:
        """
        Определяет, надо ли поставить телефон на зарядку.

        :return: Ставить ли на зарядку

        Примеры:
        >>> phone = Phone(18, 50)
        >>> phone.charging()
        """
        ...

    def change_brightness(self, how_much: int) -> None:
        """
        Изменяет яркость экрана телефона как в большую, так и в меньшую стороны, или оставляет яркость той же.

        :param how_much: На сколько изменить яркость
        :raise ValueError: Если яркость не лежит в интервале [0, 100], вызываем ошибку

        Примеры:
        >>> phone = Phone(18, 50)
        >>> phone.change_brightness(20)
        """
        if not isinstance(how_much, int):
            raise TypeError("Ожидается число")
        ...


class Headphones:
    """
    Класс Наушники.
    """
    def __init__(self, customer: str, volume: int):
        """
        Создание и подготовка к работе объекта "Наушники".

        :param customer: Имя владельца наушников
        :param volume: Громкость

        Примеры:
        >>> headphones = Headphones('Maria', 50)  # инициализация экземпляра класса
        """
        if not isinstance(customer, str):
            raise TypeError("Имя владельца должно быть типа str")
        self.customer = customer

        if not isinstance(volume, int):
            raise TypeError("Ожидается число")
        if volume < 0:
            raise ValueError("Громкость должна быть неотрицательным числом")
        self.volume = volume

    def warning(self) -> str:
        """
        Предупреждает о превышении безопасной громкости, если выполняется условие.

        :return: Строка с предупреждением

        Примеры:
        >>> headphones = Headphones('Maria', 50)  # инициализация экземпляра класса
        >>> headphones.warning()
        """
        ...

    def change_volume(self, how_much: int) -> None:
        """
        Изменяет громкость наушников как в большую, так и в меньшую стороны, или оставляет громкость той же.

        :param how_much: На сколько изменить громкость
        :raise ValueError: Если громкость не лежит в интервале [0, 100], вызываем ошибку

        Примеры:
        >>> headphones = Headphones('Maria', 50)  # инициализация экземпляра класса
        >>> headphones.change_volume(20)
        """
        if not isinstance(how_much, int):
            raise TypeError("Ожидается число")
        ...


class SmartWatсh:
    """
    Класс Смарт-часы.
    """
    def __init__(self, distance: Union[int, float], pulse: int):
        """
        Создание и подготовка к работе объекта "Смарт-часы".

        :param distance: Дистанция до владельца часов
        :param pulse: Пульс владельца часов

        Примеры:
        >>> smart_watсh = SmartWatсh(500, 50)  # инициализация экземпляра класса
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("Дистанция до владельца должна быть типа int или float")
        if distance < 0:
            raise ValueError("Дистанция до владельца должна быть неотрицательным числом")
        self.distance = distance

        if not isinstance(pulse, int):
            raise TypeError("Ожидается число")
        if pulse < 0:
            raise ValueError("Пульс должен быть неотрицательным числом")
        self.pulse = pulse

    def warning_low_pulse(self) -> str:
        """
        Предупреждает о низком пульсе, если выполняется условие.

        :return: Строка с предупреждением

        Примеры:
        >>> smart_watсh = SmartWatсh(500, 50)  # инициализация экземпляра класса
        >>> smart_watсh.warning_low_pulse()
        """
        ...

    def left_smart_watсh(self) -> str:
        """
        Предупреждает об оставлении часов, если выполняется условие.

        :return: Строка с предупреждением

        Примеры:
        >>> smart_watсh = SmartWatсh(500, 50)  # инициализация экземпляра класса
        >>> smart_watсh.left_smart_watсh()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
