def append_value(val, lst):
    if val != '':
        lst.append(val)


operations = set('+-/*()')
unary_operation = set('+-')


def split_(expression):
    expression = ' ' + expression
    total = []
    op_count = 0
    value = ''
    val_oper = bool()

    for i in range(len(expression)):
        if expression[i].isdigit():
            value += expression[i]
            val_oper = True
        elif expression[i] in operations:
            append_value(value.strip(), total)

            if expression[i] in unary_operation and (not val_oper and expression[i-1] != ')'):
                total.append('0')

            total.append(expression[i])
            val_oper = False
            value = ''
            op_count += 1
        elif expression[i] == ' ':
            append_value(value.strip(), total)
            value = ''
        else:
            raise BaseException

    append_value(value.strip(), total)

    if op_count == 0:
        raise BaseException
    return total


if __name__ == '__main__':
    print(*split_('+22+2'))
