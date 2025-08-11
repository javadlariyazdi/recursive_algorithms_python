

#recursive_gcd_lcm
def gcd(a, b):
    """calculate gcd using recursion"""
    if b == 0:
        return a
    return gcd(b , a%b)

def lcm(a, b):
    """calculate lcm using recursion"""
    return a * b // gcd(a, b)

if __name__ == "__main__":
    try:
        num1 = int(input("enter first number: "))
        num2 = int(input("enter second number: "))
        if num1 <= 0 or num2 <= 0:
            raise ValueError("⚠️ please enter positive number! ⚠️")
    except ValueError as ve:
        print(f"❌ Input Error:", {ve}, "❌")  
    except RecursionError:
        print("❌ Input is too large! Maximum recursion depth exceeded. ❌")
    except Exception as e:
        print(f"⚠️ Unexpected Error: {e} ⚠️")    
    else:
        print(f"gcd = {gcd(num1, num2)} and lcm = {lcm(num1, num2)}")