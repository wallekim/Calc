import logging
from src import separator, notation, calculating

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


if __name__ == '__main__':

    s = str(input())
    try:
        s = separator.split_(s)
        solve(s)
    except BaseException:
        print('Try again')

