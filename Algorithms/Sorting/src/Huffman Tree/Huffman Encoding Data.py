from math import dist

from Node import Node


def Calculate_Probability(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) is None:
            symbols[element] = 1
        else:
            symbols[element] += 1
    return symbols


codes = dict()


def Calculate_Codes(node, val=''):
    newVal = val + str(node.code)

    if node.left:
        Calculate_Codes(node.left, newVal)
    if node.right:
        Calculate_Codes(node.right, newVal)
    if not node.left and not node.right:
        codes[node.symbol] = newVal

    return codes


def Output_Encoded(data, coding):
    encoding_output = []
    for c in data:
        print(coding[c], end='')
        encoding_output.append(coding[c])

    string = ''.join([str(item) for item in encoding_output])
    return string


def total_Gain(data, coding):
    before_compression = len(data)
    after_compression = 0
    symbols = coding.keys()
    for symbol in symbols:
        count = data.count(symbol)
        after_compression += count * len(coding[symbol])
    print("Space usage before compression (in bits): ", before_compression)
    print("Space usage after compression (in bits)", after_compression)


def Huffman_Encoding(data):
    symbols_with_probs = Calculate_Probability(data)
    symbols = symbols_with_probs.keys()
    probabilities = symbols_with_probs.values()
    print("symbols: ", symbols)
    print("Probabilities ", probabilities)

    nodes = []

    for symbol in symbols:
        nodes.append(Node(symbols_with_probs.get(symbol), symbol))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.prob)
        right = nodes[0]
        left = nodes[1]

        left.code = 0
        right.code = 1

        newNode = Node(left.prob + right.prob, left.symbol + right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffman_encoding = Calculate_Codes(nodes[0])
    print(huffman_encoding)
    total_Gain(data, huffman_encoding)
    encoded_output = Output_Encoded(data, huffman_encoding)
    print("Encoded_output: ", encoded_output)
    return encoded_output, nodes[0]


data = "AAAAAAAAAAAAAABCCCCCCCCCCCCCCCDDEEEEEEEE"

Huffman_Encoding(data)
