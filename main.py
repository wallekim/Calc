def getsign(sign, number):
    return number * (-1) if sign == False else number


def find_digit(j, s_searching):
    processing_number = ''
    while s_searching[j].isdigit() == True:
        processing_number += s_searching[j]
        if j < len(s_searching) - 1:
            j += 1
        else:
            break
    return j, int(processing_number)


def plus_minus(strs_without_multipl):
    i = 0
    sum = 0
    processed_number = ''
    sign = True

    while i < len(strs_without_multipl)-1:
        if strs_without_multipl[i] == '-':
            sign = False
            i += 1
        elif strs_without_multipl[i] == '+':
            sign = True
            i += 1

        i, processed_number = find_digit(i, strs_without_multipl)

        if sum != '':
            sum += getsign(sign, processed_number)
            processed_number = ''
    return sum

    def multiplication(not_readystr):
        i = not_readystr.find('*')


def check_problems(s):
    b = True

    d ={
        '+': 1,
        '-': 1,
        '*': 1,
        '/': 1
        }

    for i in s:
        if i.isdigit() == True or i in d:
            b = True
        else:
            b = False
    return b

def solve(strs):

    out = plus_minus(strs)

# Multiplication coming soon
#     LOL

    return out

s = str(input())

while check_problems(s) != True:
    print('Давай, братишка, я верю в тебя :)')
    s = str(input())

print(solve(s))
