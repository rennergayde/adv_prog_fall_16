sol_a = 0
sol_b = 0
sol_c = 0
found = False

for a in range(1, 1000):
    for b in range(1, 1000 - a):
        c = 1000 - a - b
        if ((a ** 2) + (b ** 2) == (c ** 2)):
            sol_a = a
            sol_b = b
            sol_c = c
            found = True
        if (found):
            break
    if(found):
        break
print a * b * c
