import brackets
import notation
import calculating


def check_mistake(expression):
    expression = expression.replace(' ', '')
    operations = set('+-/*()')
    for i in range(len(expression) - 1):
        if expression[i] in operations and expression[i + 1].isdigit():
            problem = True
        else:
            return False
    problem = brackets.check_brackets(expression)
    return problem


def spliter(expression):
    total = []
    value = str()
    operations = set('+-/*()')
    for element in expression:
        if element.isdigit():
            value += element
        elif element in operations:
            if value != '':
                total.append(value.strip())
            total.append(element)
            value = ''
    total.append(value)
    return total


def solve(expression):
    ans = calculating.calculate(notation.transformation(expression))
    return ans


s = str(input())


while not check_mistake(s):
    print('Давай, братишка, я верю в тебя :)')
    s = str(input())

s = s.strip()
s = s.replace(' ', '')
s = spliter(s)

print(*solve(s))
