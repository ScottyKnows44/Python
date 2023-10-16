class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Node_Tree:

    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head:
            self.insert_recursive(self.head, newNode)

        else:
            self.head = newNode

    def insert_recursive(self, current_node, new_node):

        if new_node.data.upper() < current_node.data.upper():
            if current_node.left is None:
                current_node.left = new_node
            else:
                self.insert_recursive(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self.insert_recursive(current_node.right, new_node)

    def print_recursive(self, current):
        if current:
            self.print_recursive(current.left)
            print(current.data)
            self.print_recursive(current.right)


    def printTree(self):
        if self.head:
            self.print_recursive(self.head)
        else:
            print("list is empty")

text = open('./text.txt', "r")

root = Node_Tree()

for row in text:

    words = row.split()
    for word in words:
        node = Node(word)
        root.insert(node)


root.printTree()