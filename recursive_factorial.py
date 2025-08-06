

#recursive_factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n-1) * n

try:
    n = int(input("enter a number: "))
    if n < 0:
         raise ValueError("⚠️ please enter positive number! ⚠️")
    result = factorial(n)
except ValueError as ve:
    print(f"❌ Input Error:", {ve}, "❌")  
except RecursionError:
    print("❌ Input is too large! Maximum recursion depth exceeded. ❌")
except Exception as e:
    print(f"hmmm ⚠️ Unexpected Error: {e} ⚠️")    
else:
    print(f"✅ Result:{result}")