class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class single_linked_list:

    def __init__(self):
        self.head = None

    def insertSorted(self, newNode):

        if not isinstance(newNode.data, str):
            raise ValueError("You can only enter a string to this list")

        if self.head:
            if self.head.next:
                current = self.head
                while (current.next is not None and
                       current.next.data.upper() < newNode.data.upper()):
                    current = current.next

                newNode.next = current.next
                current.next = newNode
            else:
                if self.head.data.upper() > newNode.data.upper():
                    oldNode = self.head
                    self.head = newNode
                    newNode.next = oldNode

                else:
                    self.head.next = newNode
        else:
            self.head = newNode

    def insertAtEnd(self, newNode):
        if self.head:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = newNode
        else:
            self.head = newNode

    def insertAtBeginning(self, newNode):
        if self.head:
            old_head = self.head
            self.head = newNode
            newNode.next = old_head

        else:
            self.head = newNode

    def getHead(self):
        return self.head.data

    def print_list(self):
        if self.head is None:
            print("list is empty")
            return
        if self.head.next:
            current_node = self.head
            print(current_node.data)
            while current_node.next:
                current_node = current_node.next
                print(current_node.data)

        else:
            print(self.head.data)

