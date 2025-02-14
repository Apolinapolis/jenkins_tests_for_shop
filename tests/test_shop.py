import pytest

from models.models import Product, Cart


@pytest.fixture
def book():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def pen():
    return Product("pen", 20, "Black pen", 300)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, book):
        # TODO напишите проверки на метод check_quantity
        assert book.check_quantity(book.quantity) == True

    def test_product_buy(self, book):
        # TODO напишите проверки на метод buy
        assert book.buy(500) is None

    def test_product_buy_more_than_available(self, book):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            book.buy(2000)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product_str(self, cart, book):
        cart.add_product(book, '2000')
        assert cart.products[book] == 2000

    def test_cart_add_product_double(self, cart, book):
        cart.add_product(book, 2)
        cart.add_product(book, 1)
        assert cart.products[book] == 3

    def test_cart_add_product_sub_zero(self, cart, book):
        cart.add_product(book, 1)
        cart.add_product(book, -1)
        assert cart.products[book] == 1

    def test_cart_add_product_two(self, cart, book, pen):
        cart.add_product(book, 3)
        cart.add_product(pen, 1)
        assert cart.products[book] == 3 and cart.products[pen] == 1


    def test_remove_product(self, cart, book):
        cart.add_product(book, 1)
        cart.remove_product(book, 1)
        assert cart.products == {}

    def test_remove_product_str_more_than_in_the_cart(self, cart, book):
        cart.add_product(book, 1)
        cart.remove_product(book, "2")
        assert cart.products == {}

    def test_remove_product_only_one(self, cart, book, pen):
        cart.add_product(book, 1)
        cart.add_product(pen, 3)
        cart.remove_product(book, 1)
        assert book not in cart.products.keys() and pen in cart.products.keys()

    def test_remove_product_not_exist(self, cart, book):
        cart.remove_product(book, 1)
        assert cart.products == {}


    def test_clear_empty(self, cart):
        cart.clear()
        assert cart.products == {}

    def test_clear_one_product(self, cart, pen):
        cart.add_product(pen, 6)
        cart.clear()
        assert cart.products == {}

    def test_clear_two_products(self, cart, pen, book):
        cart.add_product(pen, 2)
        cart.add_product(book, 1)
        cart.clear()
        assert cart.products == {}


    def test_get_total_price(self,cart, book):
        cart.add_product(book)
        assert cart.get_total_price() == book.price

    def test_get_total_price_buy_count_two(self,cart, book):
        cart.add_product(book, 2)
        assert cart.get_total_price() == 2 * book.price

    def test_get_total_price_two_products(self,cart, book, pen):
        cart.add_product(book, 3)
        cart.add_product(pen)
        assert cart.get_total_price() == 3 * book.price + pen.price

    def test_get_total_price_after_clear(self,cart, book, pen):
        cart.add_product(pen, -1)
        cart.clear()
        assert cart.get_total_price() == 0


    def test_buy(self, cart, pen):
        cart.add_product(pen, 10)
        cart.buy()
        assert pen.quantity == 290

    def test_buy_two_products(self, cart, pen, book):
        cart.add_product(pen, 50)
        cart.add_product(book, 10)
        cart.buy()
        assert pen.quantity == 250 and book.quantity == 990

    def test_buy_empty(self, cart):
        cart.buy()
        assert cart.products == {}