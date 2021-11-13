import logging
from src import delimiter, notation, calculating

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s]:" + logging.BASIC_FORMAT,
    handlers=[
        logging.StreamHandler()
    ]
)
log = logging.getLogger(__name__)


def solve(expression):
    log.info(calculating.calculate(notation.transformation(expression)))


s = str(input())
s = s.strip()
s = s.replace(' ', '')

again = True

while again:
    try:
        s = delimiter.split_(s)
        again = False
        solve(s)
    except BaseException:
        again = True
        print('Try again')
        s = str(input())
        s = s.strip()
        s = s.replace(' ', '')
        s = delimiter.split_(s)


