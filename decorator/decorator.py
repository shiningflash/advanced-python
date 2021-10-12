# ref: https://fazlerabby7.github.io/python-decorator-bangla/


from datetime import datetime
from time import sleep


def log(func):

    def wrapper():
        with open('log.txt', 'a') as file:
            now = datetime.now().strftime('%I:%M:%S%p on %d %B, %Y')
            file.write(now + '\n')
        func()
    
    return wrapper


@log
def hello():
    print('Hello World!')


if __name__ == '__main__':
    for i in range(5):
        hello()
        sleep(5)
