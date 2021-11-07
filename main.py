import brackets
import pluse_minus


def check_mistake(expression):
    if brackets.check_brackets(expression):
        problem = False
        d = {
            '+': 1,
            '-': 1,
            '*': 1,
            '/': 1
        }

        for i in range(len(expression) - 1):
            if expression[i] in d:
                if expression[i + 1].isdigit():
                    problem = True
                else:
                    return False

        return problem


def solve(strs):
    ans = pluse_minus.plus_minus(strs)
    return ans


s = str(input())
s = s.replace(' ', '')

while not check_mistake(s):
    print('Давай, братишка, я верю в тебя :)')
    s = str(input())

print(solve(s.strip()))
