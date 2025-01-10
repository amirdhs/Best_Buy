import Products

class Store:
    def __init__(self,products):
        if products:
            self.products = products
        else:
            self.products = []

    def add_product(self,product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity

        return f"{total_quantity} items are in the store in total."

    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

bose = Products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Products.Product("MacBook Air M2", price=1450, quantity=100)

store = Store([bose, mac])

pixel = Products.Product("Google Pixel 7", price=500, quantity=250)
store.add_product(pixel)

print(store.get_total_quantity())
print(store.get_all_products())