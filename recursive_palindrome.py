#recursive_palindrome

def palindrome(st1):
    """Check if a string is a palindrome recursively."""
    if len(st1) == 0 or len(st1) == 1:
        return True
    elif st1[0] == st1[-1]:
        return palindrome(st1[1:-1])
    else:
        return False

if __name__ == "__main__":
    st1 = input("enter string: ")
    print(f"✅palindrome :{palindrome(st1)}")