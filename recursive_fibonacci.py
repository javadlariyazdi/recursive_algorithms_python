#recursive_fibonacci

def fibonacci(n):
    """Return the n-th Fibonacci number recursively, starting from 1."""
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == "__main__":
    try:
        n = int(input("enter a number: "))
        if n < 0:
            raise ValueError("⚠️ please enter positive number! ⚠️")
    except ValueError as ve:
        print(f"❌ Input Error: {ve} ❌")  
    except RecursionError:
        print("❌ Input is too large! Maximum recursion depth exceeded. ❌")
    except Exception as e:
        print(f"hmmm ⚠️ Unexpected Error: {e} ⚠️")    
    else:
        for i in range(n):
            print(fibonacci(i))