# from exceptions import ProductNotFoundError
#
#
# class ShoppingList:
#     def __init__(self):
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def remove_product(self, name):
#         for product in self.products:
#             if product.name == name:
#                 self.products.remove(product)
#                 return
#         raise ProductNotFoundError(f"Produkt '{name}' nie został znaleziony.")
#
#     def edit_product(self, name, **kwargs):
#         for product in self.products:
#             if product.name == name:
#                 product.edit(**kwargs)
#                 return
#         raise ProductNotFoundError(f"Produkt '{name}' nie został znaleziony.")
#
#     def mark_product_as_bought(self, name):
#         for product in self.products:
#             if product.name == name:
#                 product.mark_as_bought()
#                 return
#         raise ProductNotFoundError(f"Produkt '{name}' nie został znaleziony.")
#
#     def filter_products(self, **kwargs):
#         filtered_products = self.products
#         if 'price' in kwargs:
#             filtered_products = [p for p in filtered_products if p.price <= kwargs['price']]
#         if 'quantity' in kwargs:
#             filtered_products = [p for p in filtered_products if p.quantity >= kwargs['quantity']]
#         if 'bought' in kwargs:
#             filtered_products = [p for p in filtered_products if p.bought == kwargs['bought']]
#         return filtered_products