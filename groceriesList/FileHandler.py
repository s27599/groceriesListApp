# import json
#
# from product import Product
#
#
# class FileHandler:
#     @staticmethod
#     def save_to_file(products, filename):
#         data = [vars(product) for product in products]
#         with open(filename, 'w') as file:
#             json.dump(data, file)
#
#     @staticmethod
#     def load_from_file(filename):
#         with open(filename, 'r') as file:
#             data = json.load(file)
#         products = []
#         for item in data:
#             product = Product(**item)
#             products.append(product)
#         return products
