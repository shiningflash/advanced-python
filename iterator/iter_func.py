def my_range(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

nums = my_range(1, 10)

for i in range(0, 5):
    print(next(nums))

for i in range(0, 5):
    print(next(nums))
