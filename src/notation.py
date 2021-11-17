priority_sign = {
    '*': 3, '+': 2, '(': 1,
    '/': 3, '-': 2, ')': 1
}


def transformation(expression):
    final_expression = []
    stack = []
    for element in expression:
        if element.isdigit():
            final_expression.append(element)
        elif stack:
            if element == '(' or priority_sign[element] > max_sign:
                stack.append(element)
                max_sign = priority_sign[element]

            elif element == ')':
                while stack[-1] != '(':
                    final_expression.append(stack.pop())
                    max_sign = priority_sign[stack[-1]]
                stack.pop()
                if stack:
                    max_sign = priority_sign[stack[-1]]
                else:
                    max_sign = 0

            elif max_sign >= priority_sign[element]:
                while max_sign >= priority_sign[element]:
                    final_expression.append(stack.pop())
                    if stack:
                        max_sign = priority_sign[stack[-1]]
                    else:
                        max_sign = 0
                stack.append(element)
                max_sign = priority_sign[element]
        else:
            stack.append(element)
            max_sign = priority_sign[element]
    while stack:
        final_expression.append(stack.pop())

    return final_expression


if __name__ == '__main__':
    print(transformation(['(', '(', '2', '+', '2', ')', '*', '(', '3', '*', '3', ')', '+', '1', ')', '*', '9']))