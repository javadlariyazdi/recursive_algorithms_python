
#recursive_text
def recursive_text(word):
    if word == "":
        return ""
    return word[-1] + recursive_text(word[:-1])
        

word = input('please enter your text: ')
print(recursive_text(word))