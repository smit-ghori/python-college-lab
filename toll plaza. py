class CircularQueue:
    def __init__(self, size=5):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Add a vehicle
    def enqueue(self, vehicle):
        if (self.rear + 1) % self.size == self.front:
            print("Toll Plaza is FULL! Vehicle must wait.")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = vehicle
        print(vehicle, "entered the toll plaza.")

    # Remove a vehicle
    def dequeue(self):
        if self.front == -1:
            print("No vehicles at the toll plaza.")
            return

        vehicle = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(vehicle, "has crossed the toll.")

    # Display queue
    def display(self):
        if self.front == -1:
            print("Toll Plaza is empty.")
            return

        print("\nVehicles in Toll Plaza:")

        i = self.front
        while True:
            print(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size



cq = CircularQueue()

while True:
    print("\n===== TOLL PLAZA MENU =====")
    print("1. Vehicle Arrives")
    print("2. Vehicle Crosses Toll")
    print("3. Display Vehicles")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        vehicle = input("Enter Vehicle Number: ")
        cq.enqueue(vehicle)

    elif choice == 2:
        cq.dequeue()

    elif choice == 3:
        cq.display()

    elif choice == 4:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")