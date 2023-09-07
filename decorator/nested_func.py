def hello(val):

    def nested(n):

        def nested2(x):
            return val + n + x

        return nested2
    
    return nested

if __name__ == '__main__':
    print(hello(5)) # <function hello.<locals>.nested at 0x7f05ff545620>
    print(hello(5)(3)) # <function hello.<locals>.nested.<locals>.nested2 at 0x7f05ff545b70>
    print(hello(5)(3)(2)) # 10
 