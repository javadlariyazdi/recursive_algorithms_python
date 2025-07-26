
#recursive_sum_digits

def sum_digit(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digit(n // 10)

n = int(input("enter a number:"))
print(sum_digit(n))