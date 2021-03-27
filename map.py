import math

# def area(r):
#     return math.pi * r**2

area = lambda r: math.pi * r**2

radii = [2, 3, 7.4, 1]

# Method 1 : Direct Method

areas = []
for r in radii:
    areas.append(area(r))
print(areas)

# Method 2 :

areas = [area(r) for r in radii]
print(areas)

# Method 3 : Using Map

areas = list(map(area, radii))
print(areas)


# CELCIUS to FARENHITE

temps = [("Berlin", 29), ("New York", 28), ("London", 22)]

c_to_f = lambda data: (data[0], (9/5.0)*data[1] + 32)

temps_fer = list(map(c_to_f, temps))

print(temps_fer)
