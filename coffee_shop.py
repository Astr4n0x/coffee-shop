# Coffee Shop Optimized with Colors

class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    END = "\033[0m"

class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_order(self, coffee):
        self.items.append(coffee)
        print(f"{Colors.GREEN}Added {coffee.name} to your cart!{Colors.END}")

    def total(self):
        return sum(item.price for item in self.items)

    def show_order(self):
        if not self.items:
            print(f"{Colors.YELLOW}Your cart is empty.{Colors.END}")
            return

        print(f"\n{Colors.BOLD}{Colors.CYAN}Your Orders:{Colors.END}")
        for i, item in enumerate(self.items, 1):
            print(f"{Colors.BLUE}{i}. {item.name} - ${item.price:.2f}{Colors.END}")
        print(f"{Colors.GREEN}Total: ${self.total():.2f}{Colors.END}\n")

    def checkout(self):
        if not self.items:
            print(f"{Colors.YELLOW}Your cart is empty.{Colors.END}")
            return

        self.show_order()
        confirm = input(f"{Colors.CYAN}Process your checkout? (yes/no): {Colors.END}").lower()
        if confirm == "yes":
            print(f"{Colors.GREEN}Checkout completed. Enjoy your coffee!{Colors.END}")
            self.items.clear()
        else:
            print(f"{Colors.YELLOW}Checkout cancelled.{Colors.END}")

def main():
    menu = [
        Coffee("Espresso", 2.50),
        Coffee("Americano", 3.00),
        Coffee("Latte", 3.50),
        Coffee("Cappuccino", 3.75),
        Coffee("Mocha", 4.00),
        Coffee("Flat White", 3.25),
        Coffee("Macchiato", 3.00),
        Coffee("Affogato", 4.50),
        Coffee("Cold Brew", 3.75),
        Coffee("Vietnamese Coffee", 3.00),
        Coffee("Iced Coffee", 3.50),
        Coffee("Irish Coffee", 4.25),
        Coffee("Turkish Coffee", 2.75),
    ]

    my_order = Order()

    while True:
        print(f"\n{Colors.HEADER}{Colors.BOLD}..........Welcome to the Coffee Shop..........{Colors.END}")
        for i, coffee in enumerate(menu, 1):
            print(f"{Colors.CYAN}{i}. {coffee.name} - ${coffee.price:.2f}{Colors.END}")
        print(f"{Colors.YELLOW}14. View your order")
        print("15. Checkout")
        print("16. Exit")

        choice = input(f"{Colors.BOLD}Choose an option (1-16): {Colors.END}")

        if choice.isdigit() and 1 <= int(choice) <= 13:
            my_order.add_order(menu[int(choice) - 1])
        elif choice == "14":
            my_order.show_order()
        elif choice == "15":
            my_order.checkout()
        elif choice == "16":
            print(f"{Colors.GREEN}Thank you for visiting the Coffee Shop!{Colors.END}")
            break
        else:
            print(f"{Colors.RED}Invalid choice, please try again.{Colors.END}")

if __name__ == "__main__":
    main()