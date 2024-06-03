import json

from product import Product


class FileHandler:
    """
    Klasa obsługuijąca operacje na plikach

    Metody:
    save_to_file(products, filename): zapisuje do pliku
    load_from_file(filename): odczytuje z pliku i zwraca ich listę
    """

    @staticmethod
    def save_to_file(products, filename):
        """
        Zapisuje produkty do pliku
        :param products:
        :type products: list
        :param filename:
        :type filename: str
        """

        data = [vars(product) for product in products]
        with open(filename, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def load_from_file(filename):
        """
        Odczytuje produkty z pliku i zwraca ich listę
        :param filename:
        :type filename: str
        :return: lista produktów odczytanych z pliku
        :rtype: list
        """

        with open(filename, 'r') as file:
            data = json.load(file)
        products = []
        for item in data:
            product = Product(**item)
            products.append(product)
        return products
