class CashRegister:
    def __init__(self):
        self.total = 0.00

    def add_item(self, price):
        self.total += price

    def remove_item(self, price):
        if self.total >= price:
            self.total -= price
        else:
            print("Insufficient funds.")

    def print_receipt(self):
        print(f"Total: ${self.total:.2f}")


def main():
    register = CashRegister()

    while True:
        print("1. Add item")
        print("2. Remove item")
        print("3. Print receipt")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            price = float(input("Enter the price of the item: "))
            register.add_item(price)
        elif choice == "2":
            price = float(input("Enter the price of the item to remove: "))
            register.remove_item(price)
        elif choice == "3":
            register.print_receipt()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

        print()


if __name__ == "__main__":
    main()
    