from FileHandler import FileHandler
from exceptions import ProductNotFoundError
from product import Product


class ShoppingList:
    """
    Klasa przechowująca  listę zakupów

    Atrybuty:
    products[]: lista produktów

    Metody:
    add_product(self, product): Dodaje produkt do listy.
    remove_product(self, name): Usuwa produkt z listy.
    edit_product(self, product_name, **kwargs): Edytuje produkt na liście.
    mark_product_as_bought(self, name): Oznacza produkt jako kupiony.
    filter_products(self, **kwargs): Filtruje produkty na podstawie podanych kryteriów.
    display(self): Wyświetla wszystkie produkty na liście.
    save_to_file(self, filename): Zapisuje listę zakupów do pliku.
    load_from_file(self, filename): Wczytuje listę zakupów z pliku.
    get_statistics(self): Zwraca statystyki dotyczące zakupów.
    """

    def __init__(self):
        self.products = []

    def add_product(self, product):
        """
        Dodaje produkt do listy.

        :param product:
        :type product: Product
        """
        self.products.append(product)

    def remove_product(self, name):
        """
        Usuwa produkt z listy.
        :param name:
        :type name: str
        :raises ProductNotFoundError: jeżeli produkt o danej nazwie nie istnieje
        """
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                return
        raise ProductNotFoundError(f"Produkt '{name}' nie został znaleziony.")

    def edit_product(self, newName, **kwargs):
        """
        Edutuje produkt
        :param newName: nazwa produktu do edytowania
        :type newName: str
        :param kwargs: nowe wartości produktu
        :type kwargs: dict
        :raises ProductNotFoundError: gdy produkt nie istnieje
        """
        for product in self.products:
            if product.name == newName:
                product.edit(**kwargs)
                return
        raise ProductNotFoundError(f"Produkt '{newName}' nie został znaleziony.")

    def mark_product_as_bought(self, name):
        """
        oznacza produkt jako kupiony
        :param name:
        :type name: str
        :raises ProductNotFoundError: gdy produkt nie istnieje
        """

        for product in self.products:
            if product.name == name:
                product.mark_as_bought()
                return
        raise ProductNotFoundError(f"Produkt '{name}' nie został znaleziony.")

    def filter_products(self, **kwargs):
        """
        filtruje produkty
        :param kwargs: kryteria filtrowania
        :type kwargs: dict
        :return: filtrowana lista produktów
        :rtype: list[Product]
        """

        filtered_products = self.products
        if 'price' in kwargs:
            filtered_products = [p for p in filtered_products if p.price <= kwargs['price']]
        if 'quantity' in kwargs:
            filtered_products = [p for p in filtered_products if p.quantity >= kwargs['quantity']]
        if 'bought' in kwargs:
            filtered_products = [p for p in filtered_products if p.bought == kwargs['bought']]
        return filtered_products

    def display(self):
        """
        wyświetla listę zakupów
        """
        for product in self.products:
            print(product)

    def save_to_file(self, filename):
        """
        zapisuje listę do pliku
        :param filename: nazwa pliku
        :type filename: str
        """
        FileHandler.save_to_file(self.products, filename)

    def load_from_file(self, filename):
        """
        wczytuję listę z pliku
        :param filename: nazwa pliku
        :type filename: str
        """
        self.products = FileHandler.load_from_file(filename)

    def get_statistics(self):
        """
        zwraca statystyki zakupów
        :return: statystyki(całkowity koszt, średnią cenę, ilość produktów, najczęściej kupowany produkt)
        :rtype: dict
        """
        total_cost = sum(p.price * p.quantity for p in self.products)
        average_price = total_cost / len(self.products)
        quantity = len(self.products)
        most_frequent_product = max(set(self.products), key=self.products.count)

        return {
            'total_cost': total_cost,
            'average_price': average_price,
            'number_of_products': quantity,
            'most_frequent_product': most_frequent_product.name
        }
