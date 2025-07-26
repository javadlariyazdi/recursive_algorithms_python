#recursive_fibonacci

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)


n = int(input("enter a number: "))
for i in range(1, n+1):
    print(fibonacci(i))