
#recursive_max_number_in_list

def recursive_max(ls):
    if len(ls) == 1:
        return ls[0]
    max_rest =  recursive_max(ls[1:])
    return ls[0] if ls[0] > max_rest else max_rest



ls = []
while True:
    n = int(input("enter max number in list (for exit enter 0): "))
    if n == 0:
        break
    ls.append(n)

print(recursive_max(ls))