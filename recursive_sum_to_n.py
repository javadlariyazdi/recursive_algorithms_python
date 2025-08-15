
#recursive_sum_to_n

def recursive_sum_to_n(n):
    """Return the sum of all numbers from 1 to n using recursion."""
    if n == 0:
        return 0
    return recursive_sum_to_n(n-1) + n

if __name__ == "__main__":
    try:
        n = int(input("enter a number:"))
        if n < 0 :
            raise ValueError("⚠️ please enter positive number! ⚠️")
    except ValueError as ve:
        print(f"❌ Input Error: {ve} ❌")  
    except RecursionError:
        print("❌ Input is too large! Maximum recursion depth exceeded. ❌")
    except Exception as e:
        print(f"⚠️ Unexpected Error: {e} ⚠️")       
    else:
        print(f"✅sum numbers: {recursive_sum_to_n(n)}")
        