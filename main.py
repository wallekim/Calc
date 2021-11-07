import brackets
import pluse_minus
import polsky_notation
import calculating
import re


def check_mistake(expression):
    expression = expression.replace(' ', '')
    operations = set('+-/*')
    if brackets.check_brackets(expression):
        problem = False

        for i in range(len(expression) - 1):
            if expression[i] in operations:
                if expression[i + 1].isdigit():
                    problem = True
                else:
                    return False

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
    ans = calculating.calculate(polsky_notation.transformation(expression))
    return ans


s = str(input())


while not check_mistake(s):
    print('Давай, братишка, я верю в тебя :)')
    s = str(input())

s = s.strip()
s = s.replace(' ', '')
s = spliter(s)

print(*solve(s))
