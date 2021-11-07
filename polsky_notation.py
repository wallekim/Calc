def transformation(expression):
    priority_sign = {
        '*': 3, '+': 2, '(': 1,
        '/': 3, '-': 2, ')': 1
    }
    final_expression = []
    stack = []
    for element in expression:
        if element.isdigit():
            final_expression.append(element)
        elif stack:
            if element == '(' or priority_sign[element] > max_sign:
                stack.append(element)
                max_sign = priority_sign[element]
            else:
                while max_sign >= priority_sign[element] or stack != []:

                    if stack[-1] == '(':
                        break

                    if max_sign == 1:
                        stack.pop()
                    else:
                        final_expression.append(stack.pop())

                    if stack:
                        max_sign = priority_sign[stack[-1]]
                    else:
                        max_sign = 0

                stack.append(element)

        else:
            stack.append(element)
            max_sign = priority_sign[element]
    while stack:
        if priority_sign[stack[-1]] == 1:
            stack.pop()
        else:
            final_expression.append(stack.pop())

    return final_expression


if __name__ == '__main__':
    print(transformation('(1+2)*4+3'))
