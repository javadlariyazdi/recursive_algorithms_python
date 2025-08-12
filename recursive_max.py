
#recursive_max_number_in_list

def recursive_max(ls):
    if len(ls) == 1:
        return ls[0]
    max_rest =  recursive_max(ls[1:])
    return ls[0] if ls[0] > max_rest else max_rest


if __name__ == "__main__":
    ls = []
    try:
        while True:
            n = int(input("enter max number in list (for exit enter 0): "))
            if n == 0:
                break
            ls.append(n)
    except ValueError as ve:
        print(f"❌ Input Error: {ve} ❌")  
    except RecursionError:
        print("❌ Input is too large! Maximum recursion depth exceeded. ❌")
    except Exception as e:
        print(f"⚠️ Unexpected Error: {e} ⚠️")       
    if ls:
        print(f"✅ Maximum number is: {recursive_max(ls)}")
    else:
        print("⚠️ No numbers entered.")
