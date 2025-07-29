#recursive_pow

def recursive_pow(base, power):
    if power == 0:
        return 1
    elif power == 1:
        return base
    return base * recursive_pow(base, power-1)


base = int(input("enter base number: "))
power = int(input("enter pow number: "))
print(recursive_pow(base, power))