# Supermarket Billing System (Compatible with Bytexl Nimbus)

# Product class
class Product:
    def _init_(self, code, name, price, stock):
        self.code = code  # unique identifier for the product
        self.name = name  # product name
        self.price = price  # price of the product
        self.stock = stock  # available stock of the product

    def update_stock(self, quantity):
        if quantity > self.stock:
            print(f"Not enough stock for {self.name}. Available stock: {self.stock}")
        else:
            self.stock -= quantity

    def display(self):
        return f"Code: {self.code}, Name: {self.name}, Price: ${self.price}, Stock: {self.stock}"

# Shopping Cart Class
class Cart:
    def _init_(self):
        self.items = {}  # dictionary to hold product code and quantity

    def add_to_cart(self, product, quantity):
        if product.code in self.items:
            self.items[product.code]['quantity'] += quantity
        else:
            self.items[product.code] = {'product': product, 'quantity': quantity}

    def remove_from_cart(self, product_code):
        if product_code in self.items:
            del self.items[product_code]

    def view_cart(self):
        total = 0
        print("\nItems in the Cart:")
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            total += product.price * quantity
            print(f"{product.name} (x{quantity}) - ${product.price * quantity}")
        return total

    def clear_cart(self):
        self.items.clear()

# Billing System
class BillingSystem:
    def _init_(self):
        self.products = []  # List to store all products
        self.cart = Cart()  # Cart object

    def add_product(self, code, name, price, stock):
        product = Product(code, name, price, stock)
        self.products.append(product)

    def find_product(self, code):
        for product in self.products:
            if product.code == code:
                return product
        return None

    def display_products(self):
        print("\nAvailable Products:")
        for product in self.products:
            print(product.display())

    def checkout(self):
        total = self.cart.view_cart()
        print(f"\nTotal: ${total}")
        apply_discount = input("Do you want to apply a discount (Y/N)? ").lower()
        if apply_discount == 'y':
            discount_percentage = float(input("Enter discount percentage: "))
            discount_amount = (discount_percentage / 100) * total
            total -= discount_amount
            print(f"Discount applied: -${discount_amount}")

        tax_percentage = 10  # Let's say tax is 10%
        tax_amount = (tax_percentage / 100) * total
        total += tax_amount
        print(f"Tax applied: +${tax_amount}")
        
        print(f"\nFinal Total to pay: ${total}")
        self.cart.clear_cart()
        print("Thank you for shopping with us!")

# Main function to run the program
def display_menu():
    print("\nSupermarket Billing System")
    print("1. Add Product")
    print("2. View Products")
    print("3. Add to Cart")
    print("4. Remove from Cart")
    print("5. View Cart")
    print("6. Checkout")
    print("7. Exit")

def main():
    system = BillingSystem()

    # Adding some initial products to the system (in a real scenario, this could be dynamic)
    system.add_product("P001", "Apple", 1.5, 50)
    system.add_product("P002", "Banana", 0.8, 100)
    system.add_product("P003", "Milk", 1.2, 30)
    system.add_product("P004", "Bread", 1.0, 20)

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            code = input("Enter product code: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            system.add_product(code, name, price, stock)

        elif choice == "2":
            system.display_products()

        elif choice == "3":
            code = input("Enter product code to add to cart: ")
            quantity = int(input("Enter quantity: "))
            product = system.find_product(code)
            if product and product.stock >= quantity:
                system.cart.add_to_cart(product, quantity)
                product.update_stock(quantity)
                print(f"{product.name} added to cart.")
            else:
                print("Insufficient stock or invalid product code.")

        elif choice == "4":
            code = input("Enter product code to remove from cart: ")
            system.cart.remove_from_cart(code)
            print("Item removed from cart.")

        elif choice == "5":
            total = system.cart.view_cart()
            print(f"Total: ${total}")

        elif choice == "6":
            system.checkout()

        elif choice == "7":
            print("Exiting the Supermarket Billing System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
