
#recursive_text
def recursive_text(word):
    if word == "":
        return ""
    print(word[-1],end=" ")
    return recursive_text(word[:-1])
        

word = input('please enter your text: ')
print(recursive_text(word))