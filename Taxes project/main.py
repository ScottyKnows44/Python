tax_input = int(input("How much did you get payed this year? $"))

rates = [.1, .12, .22, .24, .32, .35, .37]
bracket = [10275, 41775, 89075, 170050, 215950, 539900]


def taxes_rec(income, i):
    return income - (income * .10) if (i == 0) else (
                (income - bracket[i - 1]) - ((income - bracket[i - 1]) * rates[i]) + taxes_rec(bracket[i - 1], i - 1))


def taxes(income):
    for i in bracket:
        i = bracket.index(i)
        if income <= bracket[0]:
            i = 0
        if bracket[i - 1] < income <= bracket[i]:
            i = i
            break
    return taxes_rec(income, i)


print(taxes(tax_input))
