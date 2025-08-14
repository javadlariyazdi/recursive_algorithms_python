#recursive_pow

def recursive_pow(base, power):
    """Calculate base^power recursively."""
    if power == 0:
        return 1
    elif power == 1:
        return base
    return base * recursive_pow(base, power-1)

if __name__ == "__main__":
    try:
        base = int(input("enter base number: "))
        power = int(input("enter pow number: "))
        if base <= 0 or power <= 0:
            raise ValueError("⚠️ please enter positive number! ⚠️")
    except ValueError as ve:
        print(f"❌ Input Error: {ve} ❌")  
    except RecursionError:
        print("❌ Input is too large! Maximum recursion depth exceeded. ❌")
    except Exception as e:
        print(f"⚠️ Unexpected Error: {e} ⚠️")   
    else:    
        print(f"✅recursive_pow :{recursive_pow(base, power)}")