class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data=data)

        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def append_at_first(self, data):
        newNode = Node(data=data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def append_at_position(self, data, position):
        newNode = Node(data=data)

        if position == 0:
            newNode.next = self.head
            self.head.next = newNode
            return

        temp = self.head

        for i in range(position - 1):
            if temp == None:
                print("Position not found")
                return

            temp = temp.next

        if temp is None:
            print("Position not found")
            return

        newNode.next = temp.next
        temp.next = newNode

    def disp(self):
        temp = self.head
        while temp is not None:
            print(temp.data, "->")
            temp = temp.next


l = LinkedList()
l.append(11)
l.append(45)
l.append(99)
l.append_at_first(10000)
l.append_at_position(5555, 90)
l.disp()
