def fibon(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    i = 2
    n1 = 0
    n2 = 1

    while i <= n:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        i += 1

    return n3

print ("5th Fibonacci term: ", fibon(5))
print("10th Fibonacci term: ", fibon(10))
print("15th Fibonacci term: ", fibon(15))
