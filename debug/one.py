from datetime import datetime

from icecream import ic

from two import div_by_5


def div_by_3():
    for x in range(20):
        if x % 3 == 0:
            ic(x)


if __name__ == '__main__':
    ic.configureOutput(
        includeContext=True,
        prefix=f'debug || {datetime.now()} >> '
    )
    div_by_3()
    div_by_5()
