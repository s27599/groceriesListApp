from exceptions import ProductNotFoundError
from product import Product
from shoppingList import ShoppingList

"""
Główna funkcja programu zawierająca menu konsolowe.

    Funkcje:
    - Dodawanie produktu do listy zakupów.
    - Usuwanie produktu z listy zakupów.
    - Edytowanie produktu na liście zakupów.
    - Oznaczanie produktu jako kupiony.
    - Wyświetlanie listy zakupów.
    - Filtrowanie produktów na podstawie podanych kryteriów.
    - Zapis listy zakupów do pliku.
    - Wczytywanie listy zakupów z pliku.
    - Wyświetlanie statystyk dotyczących zakupów.
    - Wyjście z programu.


"""



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
        filter_bought = input("Status (kupione/nie kupione, pozostaw puste, aby pominąć): ")

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
            elif filter_bought.lower() == 'nie kupione':
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
        print(f"średnia cena: {stats['average_price']:.2f}")
        print(f"ilość przedmiotów: {stats['number_of_products']}")
        print(f"Najczęściej kupowany produkt: {stats['most_frequent_product']}")

    elif choice == "0":
        print("Koniec programu.")
        break

    else:
        print("Nieprawidłowy wybór, spróbuj ponownie.")
