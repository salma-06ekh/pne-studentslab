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

def fibosum(n):
    sum = 0
    i = 1

    while i <= n:
        sum += fibon(i)
        i += 1
    return sum

print("Sum of the first 5 terms of the Fibonacci series: ", fibosum(5))
print("Sum of tge first 10 terms of the Fibonacci series: ", fibosum(10))