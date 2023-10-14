import node as Node

text = open('./text.txt', "r")

root = Node.single_linked_list()

for row in text:
    words = row.split()
    for word in words:
        node = Node.Node(word)
        root.insertSorted(node)


root.print_list()
