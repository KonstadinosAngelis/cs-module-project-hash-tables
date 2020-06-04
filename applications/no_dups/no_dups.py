def no_dups(s):
    counter = {}

    output = ""
    for idx, x in enumerate(s.split()):
        try: 
            counter[x]
            pass
        except KeyError:
            counter[x] = 1
    
    for key in counter:
        output += key + " "

    return output
        

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))