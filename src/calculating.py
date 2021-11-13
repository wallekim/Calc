first = int()
second = int()

operations = set('+-*/')


def calculate(expression):
    stack = []
    total = 0
    for i in expression:
        if i.isdigit():
            stack.append(i)
        elif i in operations:
            second = int(stack.pop())
            first = int(stack.pop())
            stack.append({
                '+':   first + second,
                '-':   first - second,
                '*':   first * second,
                '/':   first / second if second != 0 else "Деление на 0!",
                         }[i])

    return int(stack[-1])


lst = ['1','2', '+', '4', '*', '3', '+']

if __name__ == '__main__':
    print(calculate(lst))