# Anonymous function - Lambda Expression

# format 1

func = lambda x: 3*x + 1
harmonic_mean = lambda x, y, z: 3 / (1/x + 1/y + 1/z)
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

print(func(3))
print(harmonic_mean(2, 4, 1))
print(full_name('  amIrul ', '  islam'))


# format 2

def get_quadratic_function(a, b, c):
    return lambda x: a*x**2 + b*x + c

print(get_quadratic_function(3, 0, 1)(2))
