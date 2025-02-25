class Product:
    """
    Класс продукта
    """

    def __init__(self, name: str, price: float, description: str, quantity: int):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity: int) -> bool:
        return self.quantity >= quantity

    def buy(self, quantity: int):

        if self.check_quantity(quantity):
            self.quantity -= quantity
            print(f"\nТовар {self.name} приобретен. Со склада списано {quantity}, остаток {self.quantity} ")
        else:
            raise ValueError(f"Недостаточно товара: {self.name}. Доступно {self.quantity}, запрашивается {quantity}")

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    """

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products: dict[Product, int] = {}

    def add_product(self, product: Product, buy_count: int = 1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if int(buy_count) < 1:
            return

        if product in self.products:
            self.products[product] += int(buy_count)
        else:
            self.products[product] = int(buy_count)

    def remove_product(self, product: Product, remove_count: int = None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product not in self.products:
            return

        if remove_count is None or int(remove_count) >= self.products[product]:
            del self.products[product]
            return

        self.products[product] -= int(remove_count)

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total_price: float = 0
        for name, count in self.products.items():
            total_price += float(name.price * count)
        return total_price

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for key, value in self.products.items():
            key.buy(self.products[key])