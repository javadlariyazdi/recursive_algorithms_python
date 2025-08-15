
#recursive_sum_digits

def sum_digit(n):
    """Return the sum of digits of an integer using recursion."""
    n = abs(n)  # handle negative numbers
    if n == 0:
        return 0
    return (n % 10) + sum_digit(n // 10)

if __name__ == "__main__":
    try:
        n = int(input("enter a number:"))
    except ValueError as ve:
        print(f"❌ Input Error: {ve} ❌")  
    except RecursionError:
        print("❌ Input is too large! Maximum recursion depth exceeded. ❌")
    except Exception as e:
        print(f"⚠️ Unexpected Error: {e} ⚠️")       
    else:
        print(f"✅sum digit: {sum_digit(n)}")