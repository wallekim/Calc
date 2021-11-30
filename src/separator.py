def append_value(val, lst):
    if val != '':
        lst.append(val)


operations = set('+-/*()^!')
unary_operation = set('+-')
left_assoc = {'cos', 'tan', 'sin', 'atan'}


def split_(expression):
    expression = ' ' + expression
    total = []
    op_count = 0
    value = ''
    digit = False
    bracket = False
    some_oper = ''

    for i in range(len(expression)):
        if expression[i].isdigit():
            value += expression[i]
            digit = True
            bracket = False
        elif expression[i] in operations:
            append_value(value.strip(), total)
            some_oper = ''

            if expression[i] in unary_operation and not digit and not bracket:
                total.append('0')

            bracket = True if expression[i] == ')' else False

            total.append(expression[i])
            digit = False
            value = ''
            op_count += 1
        elif expression[i].isalpha():
            some_oper += expression[i]
            if some_oper in left_assoc:
                total.append(some_oper)
                op_count += 1
            bracket = False
        elif expression[i] == ' ':
            append_value(value.strip(), total)
            value = ''
            some_oper = ''
        else:
            raise BaseException

    append_value(value.strip(), total)

    if op_count == 0:
        raise BaseException
    return total


if __name__ == '__main__':
    print(*split_('sin(30)+0+22-343-22+343!'))
