def mydecorator(func):

    def wrapper():
        print('Before calling func()')
        func()
        print('After calling func()')
    
    return wrapper


@mydecorator
def hello():
    print('Hello World!')


if __name__ == '__main__':
    hello()
