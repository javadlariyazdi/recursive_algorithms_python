#recursive_palindrome

def palindrome(st1):
    if len(st1) == 0 or len(st1) == 1:
        return True
    elif st1[0] == st1[-1]:
        return palindrome(st1[1:-1])
    else:
        return False

st1 = input("enter string: ")
print(palindrome(st1))