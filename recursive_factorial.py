

#recursive_factorial

def factorial(n):
    if n == 0:
        return 0
    return factorial(n-1) + n

n = int(input("enter a number: "))
print(factorial(n))