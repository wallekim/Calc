priority_sign = {
    'cos': 5, 'sin': 5,
    '^': 4,
    '*': 3, '+': 2, '(': 1,
    '/': 3, '-': 2, ')': 1
}

left_assoc = {'cos', 'tan', 'sin', 'atan'}


def transformation(expression):
    final_expression = []
    stack = []
    max_sign = 0
    for element in expression:
        if element.isdigit() or element == '!':
            final_expression.append(element)

        elif element == '(' or priority_sign[element] > max_sign or element == '^' or element in left_assoc:
            stack.append(element)
            max_sign = priority_sign[element]

        elif element == ')':
            while stack[-1] != '(' and stack:
                final_expression.append(stack.pop())
            stack.pop()
            max_sign = priority_sign[stack[-1]] if stack else 0

        else:
            while max_sign >= priority_sign[element] and stack:
                final_expression.append(stack.pop())
                max_sign = priority_sign[stack[-1]] if stack else 0
            stack.append(element)
            max_sign = priority_sign[element]

    while stack:
        final_expression.append(stack.pop())

    return final_expression


if __name__ == '__main__':
    print(*transformation('sin ( 30 ) + 0 + 22 - 343 - 22 + 343 !'.split()))