class Product:
    """
    Klasa odpowiadająca za produkty w liście zakupów


    name (str): Nazwa produktu\n
    quantity (int): Ilość produktów\n
    category (str): Kategoria produktu\n
    price (float): Cena produktu\n
    notes (str): Dodatkowe uwagi\n
    bought (bool): Status czy kupione\n

    Metody:
    mark_as_bought(self): Oznacza produkt jako kupiony.
    edit(self, **kwargs) Edytuje produkt

    """

    def __init__(self, name, quantity,category, price, notes='', bought=False):
        self.name = name
        self.quantity = quantity
        self.category = category
        self.price = price
        self.notes = notes
        self.bought = bought

    def __str__(self):
        status = "Kupione" if self.bought else "Nie kupione"
        return (f"Nazwa: {self.name}, Ilość: {self.quantity}, Kategoria: {self.category}, "
                f"Cena: {self.price}, Uwagi: {self.notes}, Status: {status}")

    def mark_as_bought(self):
        """
        oznacza produkt jako kupiony

        :param self:

        """
        self.bought = True

    def edit(self, name=None, quantity=None, category=None, price=None, notes=None):
        """
            umożliwia edycję produktu

        :param name:
        :type name: str
        :param quantity :
        :type quantity: int
        :param category:
        :type category: str
        :param price:
        :type price: float
        :param notes:
        :type notes: str

        """
        if name is not None:
            self.name = name
        if quantity is not None:
            self.quantity = quantity
        if category is not None:
            self.category = category
        if price is not None:
            self.price = price
        if notes is not None:
            self.notes = notes