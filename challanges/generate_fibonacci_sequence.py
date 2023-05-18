def generate_fibonacci_sequence(num):
    array = [0, 1]
    if num <= 2:
        return array[:num]

    for i in range(2, num):
        number = (array[-2] + array[-1])
        array.insert(i, number)

    return array

print(generate_fibonacci_sequence(10))
