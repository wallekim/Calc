def get_sign(sign, number):
    return number * (-1) if sign == False else number


def find_digit(j, s_searching):
    processing_number = ''
    while s_searching[j].isdigit():
        processing_number += s_searching[j]
        if j < len(s_searching) - 1:
            j += 1
        else:
            break
    return j, int(processing_number)


def plus_minus(expression):
    i = 0
    total = 0
    processed_number = ''
    sign = True

    while i < len(expression)-1:
        if expression[i] == '-':
            sign = False
            i += 1
        elif expression[i] == '+':
            sign = True
            i += 1

        i, processed_number = find_digit(i, expression)

        if total != '':
            total += get_sign(sign, processed_number)
            processed_number = ''

    return total