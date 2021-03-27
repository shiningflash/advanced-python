"""
List = [1, 2, "Amirul", 3.24, True]

List Comprehensions:
-
1. [expr for val in collection]
2. [expr for val in collection if <test>]
3. [expr for val in collection if <test> and <test>]
4. [expr for val1 in collection1 for val2 in collection2]

"""

# Example 1: Square of (0 - 9)
square = [i**2 for i in range(10)]
print(square)

# Example 2: Name starts with letter F
names = ['Amirul', 'Bagdad', 'Samiul', 'Faizun', 'faria']
names_F = [name for name in names if name.upper().startswith('F')]
print(names_F)

# Example 3: Name starts with letter F and ends with 'a'
names_F_a = [name for name in names if name.upper().startswith('F') and name.lower().endswith('a')]
print(names_F_a)

# Example 4: students with id below 20k
students = [('Amirul', 2025), ('Mamun', 1720), ('Bagdad', 1710)]
student_below_2k = [name for (name, id) in students if id < 2000]
print(student_below_2k)

# *** Example 5: Cartesian Product
"""
A = {1, 2}
B = {x, y}
A x B = {(1, x), (1, y), (2, x), (2, y)}
"""

A = {1, 2}
B = {'x', 'y', 'z'}

cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)
