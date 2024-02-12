if __name__ == "__main__":
    class Store:
        """
        Класс Магазин.
        """

        def __init__(self, name: str) -> None:
            """
            Создание и подготовка к работе объекта "Магазин".

            :param name: Название магазина

            Примеры:
            >>> store = Store('Wb')  # инициализация экземпляра класса
            """
            self.name = name

        def __str__(self) -> str:
            """
            Магический метод __str__(self).

            :return: Строка

            Примеры:
            >>> store = Store('Wb')  # инициализация экземпляра класса
            >>> print(store)
            """
            return f'Класс {self.__class__.__name__}'

        def __repr__(self) -> str:
            """
            Магический метод __repr__(self).

            :return: Строка

            Примеры:
            >>> store = Store('Wb')  # инициализация экземпляра класса
            >>> print(repr(store))
            """
            return f'{self.__class__.__name__}(name={self.name!r})'

        def payment(self) -> None:
            """
            Метод хранит разрешенные типы оплаты покупок.

            Примеры:
            >>> store = Store('Wb')  # инициализация экземпляра класса
            >>> store.payment()
            """
            ...

        def products(self) -> None:
            """
            Метод хранит список товаров магазина.

            Примеры:
            >>> store = Store('Wb')  # инициализация экземпляра класса
            >>> store.products()
            """
            ...


    class OnlineStore(Store):
        """
        Класс Онлайн магазин.
        """

        def payment(self) -> None:
            """
            Метод хранит разрешенные типы оплаты покупок.

            Возможен только безналичный способ оплаты.

            Примеры:
            >>> on_store = OnlineStore('Wb')  # инициализация экземпляра класса
            >>> on_store.products()
            """
            ...
