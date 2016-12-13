prime_total = 0


for a in range(1,11):
    for i in range(10):
        if i > a and i % a == 0:
            print str(i) + " is not prime"
        else:
            print str(i) + " is prime"
            prime_total += i

print prime_total
