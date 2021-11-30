from math import factorial, sin, cos, tan, atan

operations = set('+-*/^')
left_assoc = {'cos', 'tan', 'sin', 'atan', '!'}

operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "/": lambda x, y: x / y,
        "*": lambda x, y: x * y,
        '^': lambda x, y: x ** y,
        'cos': lambda x: cos(x),
        'sin': lambda x: sin(x),
        'tan': lambda x: tan(x),
        'atan': lambda x: atan(x),
        '!': lambda x: factorial(x)
}


def calculate(expression):
    stack = []
    for element in expression:
        if element.isdigit():
            stack.append(element)
        elif element in left_assoc:
            second = float(stack.pop())
            stack.append(operators[element](second))
        else:
            second = float(stack.pop())
            first = float(stack.pop())
            stack.append(operators[element](first, second))

    return float(stack[-1])


lst = '30 sin 0 + 22 + 343 - 22 - 8 ! +'.split()

if __name__ == '__main__':
    print(calculate(lst))