def transformation(expression):
    priority_sign = {
        '*': 3, '+': 2, '(': 1,
        '/': 3, '-': 2, ')': 1
    }
    final_expression = []
    stack = []
    max_sign = 0
    for chr in expression:
        if chr.isdigit():
            final_expression.append(chr)
        elif priority_sign[chr] > max_sign:
            stack.append(chr)
            max_sign = priority_sign[chr]
        elif chr == ')' or max_sign >= priority_sign[chr]:
            while stack[-1] != '(' or max_sign >= priority_sign[chr]:
                final_expression.append(stack.pop())
                if stack != []:
                    max_sign = priority_sign[stack[-1]]
                else:
                    max_sign = 0
            stack.pop()
    while stack:
        final_expression.append(stack.pop())

    return final_expression


print(transformation('(1+2)*4+3'))
