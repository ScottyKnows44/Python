def is_balanced_parentheses(expression):
    stack = []
    opening_parentheses = ['[', '{', '(']
    closing_parentheses = ['}', ']', ')']
    matching_parentheses = {'[': ']', '{': '}', '(': ')'}

    # iterate though string
    for i in expression:
        # If opening parentheses add it to the stack
        if i in opening_parentheses:
            stack.append(i)
        elif i in closing_parentheses:
            # Check if stack is empty
            if not stack:
                return False

            # Get top of stack and see if it's a match
            last_opening = stack.pop()
            if matching_parentheses[last_opening] != i:
                return False

    # Return if stack is empty
    return len(stack) == 0


print(is_balanced_parentheses("{}{}{((()))}"))
