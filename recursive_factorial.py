

#recursive_factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n-1) * n

n = int(input("enter a number: "))
print(factorial(n))