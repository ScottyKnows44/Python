class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class single_linked_list:

    def __init__(self):
        self.head = None

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
        if self.head.next:
            current_node = self.head
            print(current_node.data)
            while current_node.next:
                current_node = current_node.next
                print(current_node.data)

        else:
            print(self.head.data)


root = single_linked_list()

newNode = Node(9)
root.insertAtEnd(newNode)

newNode = Node(5)
root.insertAtEnd(newNode)

newNode = Node(12)
root.insertAtEnd(newNode)

newNode = Node(69)
root.insertAtBeginning(newNode)

root.print_list()


