
#recursive_text
def recursive_text(word):
    """Return the reverse of a string using recursion."""
    if word == "":
        return ""
    return word[-1] + recursive_text(word[:-1])
        
if __name__ == "__main__":
    word = input('please enter your text: ')
    print(recursive_text(word))