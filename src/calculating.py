operations = set('+-*/')


def calculate(expression):
    stack = []
    for i in expression:
        if i.isdigit():
            stack.append(i)
        elif i in operations:
            second = float(stack.pop())
            if not stack and i == '-':
                first = 0
            else:
                first = float(stack.pop())
            stack.append({
                '+':   first + second,
                '-':   first - second,
                '*':   first * second,
                '/':   first / second if second != 0 else ZeroDivisionError,
                         }[i])

    return float(stack[-1])


lst = '0 22 + 2 +'.split()

if __name__ == '__main__':
    print(calculate(lst))