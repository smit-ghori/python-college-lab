class ConveyorBelt:
    def __init__(self):
        self.size = 8
        self.belt = [None] * self.size

    # Add product
    def add_product(self, slot, product):
        if 0 <= slot < self.size:
            if self.belt[slot] is None:
                self.belt[slot] = product
                print("Product added successfully.")
            else:
                print("Slot already occupied.")
        else:
            print("Invalid slot number.")

    def check_slot(self, slot):
        if 0 <= slot < self.size:
            if self.belt[slot] is None:
                print("Slot is empty.")
            else:
                print(f"Product at slot {slot}: {self.belt[slot]}")
        else:
            print("Invalid slot number.")

    def find_product(self, product):
        if product in self.belt:
            print(f"Product found at slot {self.belt.index(product)}")
        else:
            print("Product not found.")

    # Update product
    def update_slot(self, slot, product):
        if 0 <= slot < self.size:
            self.belt[slot] = product
            print("Slot updated successfully.")
        else:
            print("Invalid slot number.")

    
    def is_full(self):
        if None not in self.belt:
            print("Conveyor belt is FULL.")
        else:
            print("Conveyor belt is NOT FULL.")

    def display(self):
        print("\nConveyor Belt Status")
        for i in range(self.size):
            print(f"Slot {i}: {self.belt[i]}")
        print()



cb = ConveyorBelt()

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
        slot = int(input("Enter slot number (0-7): "))
        product = input("Enter product name: ")
        cb.add_product(slot, product)

    elif choice == 2:
        slot = int(input("Enter slot number (0-7): "))
        cb.check_slot(slot)

    elif choice == 3:
        product = input("Enter product name to search: ")
        cb.find_product(product)

    elif choice == 4:
        slot = int(input("Enter slot number (0-7): "))
        product = input("Enter new product name: ")
        cb.update_slot(slot, product)

    elif choice == 5:
        cb.is_full()

    elif choice == 6:
        cb.display()

    elif choice == 7:
        print("Program Ended.")
        break

    else:
        print("Invalid choice.")