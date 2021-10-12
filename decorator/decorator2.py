# decorator with parameter/argument


from datetime import datetime
from time import sleep


def log(filename='log.txt'):
    def log_decorator(func):
        def wrapper():
            with open(filename, 'a') as file:
                now = datetime.now().strftime('%I:%M:%S%p on %d %B, %Y')
                file.write(now + '\n')
            func()
        return wrapper
    return log_decorator


@log(filename='history.txt')
def hello():
    print('Hello World!')


if __name__ == '__main__':
    for i in range(5):
        hello()
        sleep(3)
