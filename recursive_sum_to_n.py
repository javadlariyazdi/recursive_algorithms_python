
#recursive_sum_to_n

def recursive_sum_to_n(n):
    if n == 0:
        return 0
    return recursive_sum_to_n(n-1) + n

n = int(input("enter a number: "))
print(recursive_sum_to_n(n))
        