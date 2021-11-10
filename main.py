import logging
import notation
import calculating


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s]:" + logging.BASIC_FORMAT,
    handlers=[
        logging.StreamHandler()
    ]
)
log = logging.getLogger(__name__)


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
    log.info(calculating.calculate(notation.transformation(expression)))


s = str(input())
s = s.strip()
s = s.replace(' ', '')
s = spliter(s)

again = True

while again:
    try:
        again = False
        solve(s)
    except BaseException:
        again = True
        print('Try again')
        s = str(input())
        s = s.strip()
        s = s.replace(' ', '')
        s = spliter(s)


