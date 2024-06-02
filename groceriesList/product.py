# class Product:
#     def __init__(self, name, quantity,category, price, notes='', bought=False):
#         self.name = name
#         self.quantity = quantity
#         self.category = category
#         self.price = price
#         self.notes = notes
#         self.bought = bought
#
#     def __str__(self):
#         status = "Kupione" if self.bought else "Nie kupione"
#         return (f"Nazwa: {self.name}, Ilość: {self.quantity}, Kategoria: {self.category}, "
#                 f"Cena: {self.price}, Uwagi: {self.notes}, Status: {status}")
#
#     def mark_as_bought(self):
#         self.bought = True
#
#     def edit(self, name=None, quantity=None, category=None, price=None, notes=None):
#         if name is not None:
#             self.name = name
#         if quantity is not None:
#             self.quantity = quantity
#         if category is not None:
#             self.category = category
#         if price is not None:
#             self.price = price
#         if notes is not None:
#             self.notes = notes