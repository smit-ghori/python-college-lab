# Design and implement a program to simulate an Amazon fulfillment centre conveyor belt using a fixed-size array of 8 slots (indexed 0–7). Each slot can store one product. The program should allow the warehouse manager to:

# Check which product is stored at a specific slot.
# Search for a product on the conveyor belt.
# Update or replace the product in a given slot.
# Check whether the conveyor belt is completely full.

# The conveyor belt has a fixed capacity of 8 slots, and no additional slots can be added.


class ConveyerBelt(object):
    def __init__(self):
        self.size = 8
        self.belt = [None] * self.size

    def add_product(self, slot, product):
        if 0 <= slot < self.size:
            if self.belt[slot] == None:
                self.belt[slot] = product
                print("Product added in slot")
            else:
                print("Slot already occupied!!")
        else:
            print("Invalid slot number")

    def check_slot(self, slot):
        if 0 <= slot < self.size:
            if self.belt[slot] == None:
                print("Slot is empty")
            else:
                print(self.belt[slot])
        else:
            print("Invalid slot")

    # find product
    def find_product(self, product):
        if product in self.belt:
            print(f"Product found at slot {self.belt.index(product)}")
        else:
            print("Product ot found")

    # Update the slot
    def update_slot(self, slot, product):
        print("\n\n-------Current Belt--------")
        print(self.belt)
        if 0 <= slot < self.size:
            self.belt[slot] = product
            print("Slot updated")
        else:
            print("Invalid slot number")

    # check belt full
    def is_full(self):
        if None in self.belt:
            print("Slot is full")
        else:
            print("Slot is not full")

    # print belt
    def print_belt(self):
        print("\n-----Current status of belt------")
        print(self.belt)


c = ConveyerBelt()

if __name__ == "__main__":
    while True:

        print("\n===== AMAZON FULFILLMENT CENTRE =====")
        print("1. Add Product")
        print("2. Check Slot")
        print("3. Find Product")
        print("4. Update Slot")
        print("5. Check if Belt is Full")
        print("6. Display Belt")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            slot = int(input("Enter slot(0 to 7): "))
            product = input("Enter product: ")
            c.add_product(slot=slot, product=product)

        elif choice == 2:
            slot = int(input("Enter slot(0 to 7): "))
            c.check_slot(slot=slot)

        elif choice == 3:
            product = input("Enter product: ")
            c.find_product(product=product)

        elif choice == 4:
            slot = int(input("Enter slot(0 to 7): "))
            product = input("Enter product: ")
            c.update_slot(product=product, slot=slot)

        elif choice == 5:
            c.is_full()

        elif choice == 6:
            c.print_belt()

        elif choice == 7:
            break

        else:
            print("Invalid choice")
