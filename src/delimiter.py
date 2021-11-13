def split_(expression):
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
        else:
            raise BaseException
    total.append(value)
    return total