

#recursive_gcd_lcm
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b ,a%b)



a = int(input("enter once number: "))
b = int(input("enter twice number: "))
print(f"gcd = {gcd(a, b)} and lcm = {int(a*b/gcd(a, b))}")