import json


# from exceptions import ProductNotFoundError
# from product import Product
# from shoppingList import ShoppingList
class ShoppingList:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                return
        raise ProductNotFoundError(f"Produkt '{name}' nie został znaleziony.")

    def edit_product(self, tmpname, **kwargs):
        for product in self.products:
            if product.name == tmpname:
                product.edit(**kwargs)
                return
        raise ProductNotFoundError(f"Produkt '{tmpname}' nie został znaleziony.")

    def mark_product_as_bought(self, name):
        for product in self.products:
            if product.name == name:
                product.mark_as_bought()
                return
        raise ProductNotFoundError(f"Produkt '{name}' nie został znaleziony.")

    def filter_products(self, **kwargs):
        filtered_products = self.products
        if 'price' in kwargs:
            filtered_products = [p for p in filtered_products if p.price <= kwargs['price']]
        if 'quantity' in kwargs:
            filtered_products = [p for p in filtered_products if p.quantity >= kwargs['quantity']]
        if 'bought' in kwargs:
            filtered_products = [p for p in filtered_products if p.bought == kwargs['bought']]
        return filtered_products

    def display(self):
        for product in self.products:
            print(product)

    def save_to_file(self, filename):
        FileHandler.save_to_file(self.products, filename)

    def load_from_file(self, filename):
        self.products = FileHandler.load_from_file(filename)

    def get_statistics(self):
        total_cost = sum(p.price * p.quantity for p in self.products)
        most_frequent_product = max(set(self.products), key=self.products.count)
        return {
            'total_cost': total_cost,
            'most_frequent_product': most_frequent_product.name
        }


class FileHandler:
    @staticmethod
    def save_to_file(products, filename):
        data = [vars(product) for product in products]
        with open(filename, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        products = []
        for item in data:
            product = Product(**item)
            products.append(product)
        return products


class ProductNotFoundError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


class Product:
    def __init__(self, name, quantity, category, price, notes='', bought=False):
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
        self.bought = True

    def edit(self, name=None, quantity=None, category=None, price=None, notes=None):
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


shopping_list = ShoppingList()

while True:
    print("\nMenu:")
    print("1. Dodaj produkt")
    print("2. Usuń produkt")
    print("3. Edytuj produkt")
    print("4. Oznacz produkt jako kupiony")
    print("5. Wyświetl listę zakupów")
    print("6. Filtruj produkty")
    print("7. Zapisz listę do pliku")
    print("8. Wczytaj listę z pliku")
    print("9. Wyświetl statystyki zakupów")
    print("0. Wyjście")
    choice = input("Wybierz opcję: ")

    if choice == "1":
        name = input("Nazwa: ")
        quantity = input("Ilość: ")
        category = input("Kategoria: ")
        price = input("Cena: ")
        notes = input("Uwagi: ")

        try:
            quantity = int(quantity)
            price = float(price)
            product = Product(name, quantity, category, price, notes)
            shopping_list.add_product(product)
            print("Produkt dodany.")
        except ValueError:
            print("Ilość musi być liczbą całkowitą, a cena liczbą rzeczywistą.")

    elif choice == "2":
        name = input("Nazwa produktu do usunięcia: ")
        try:
            shopping_list.remove_product(name)
            print("Produkt usunięty.")
        except ProductNotFoundError as e:
            print(e)

    elif choice == "3":
        name = input("Nazwa produktu do edycji: ")
        new_name = input("Nowa nazwa (pozostaw puste, aby nie zmieniać): ")
        new_quantity = input("Nowa ilość (pozostaw puste, aby nie zmieniać): ")
        new_category = input("Nowa kategoria (pozostaw puste, aby nie zmieniać): ")
        new_price = input("Nowa cena (pozostaw puste, aby nie zmieniać): ")
        new_notes = input("Nowe uwagi (pozostaw puste, aby nie zmieniać): ")

        kwargs = {}
        if new_name:
            kwargs['name'] = new_name
        if new_quantity:
            try:
                kwargs['quantity'] = int(new_quantity)
            except ValueError:
                print("Ilość musi być liczbą całkowitą.")
                continue
        if new_category:
            kwargs['category'] = new_category
        if new_price:
            try:
                kwargs['price'] = float(new_price)
            except ValueError:
                print("Cena musi być liczbą rzeczywistą.")
                continue
        if new_notes:
            kwargs['notes'] = new_notes

        try:
            shopping_list.edit_product(name, **kwargs)
            print("Produkt zaktualizowany.")
        except ProductNotFoundError as e:
            print(e)

    elif choice == "4":
        name = input("Nazwa produktu do oznaczenia jako kupiony: ")
        try:
            shopping_list.mark_product_as_bought(name)
            print("Produkt oznaczony jako kupiony.")
        except ProductNotFoundError as e:
            print(e)

    elif choice == "5":
        print("\nLista zakupów:")
        shopping_list.display()

    elif choice == "6":
        print("\nFiltruj produkty:")
        filter_price = input("Maksymalna cena (pozostaw puste, aby pominąć): ")
        filter_quantity = input("Minimalna ilość (pozostaw puste, aby pominąć): ")
        filter_bought = input("Status (kupione/niekupione, pozostaw puste, aby pominąć): ")

        kwargs = {}
        if filter_price:
            try:
                kwargs['price'] = float(filter_price)
            except ValueError:
                print("Cena musi być liczbą rzeczywistą.")
                continue
        if filter_quantity:
            try:
                kwargs['quantity'] = int(filter_quantity)
            except ValueError:
                print("Ilość musi być liczbą całkowitą.")
                continue
        if filter_bought:
            if filter_bought.lower() == 'kupione':
                kwargs['bought'] = True
            elif filter_bought.lower() == 'niekupione':
                kwargs['bought'] = False
            else:
                print("Nieprawidłowy status.")
                continue

        filtered_products = shopping_list.filter_products(**kwargs)
        print("\nFiltrowane produkty:")
        for product in filtered_products:
            print(product)

    elif choice == "7":
        filename = input("Nazwa pliku do zapisania: ")
        shopping_list.save_to_file(filename)
        print(f"Lista zakupów zapisana do pliku {filename}.")

    elif choice == "8":
        filename = input("Nazwa pliku do wczytania: ")
        shopping_list.load_from_file(filename)
        print(f"Lista zakupów wczytana z pliku {filename}.")

    elif choice == "9":
        stats = shopping_list.get_statistics()
        print("\nStatystyki zakupów:")
        print(f"Całkowity koszt: {stats['total_cost']:.2f}")
        print(f"Najczęściej kupowany produkt: {stats['most_frequent_product']}")

    elif choice == "0":
        print("Koniec programu.")
        break

    else:
        print("Nieprawidłowy wybór, spróbuj ponownie.")
