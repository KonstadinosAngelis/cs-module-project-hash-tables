def histo():
    cache = {}
    with open("applications\histo\\robin.txt") as histo:
        for line in histo:
            for word in line.split():
                output = word.lower()
                output = "".join(c for c in output if c not in (",", ".", '"', "?", ";", "!"))
                
                if output in cache:
                    cache[output] += 1
                else:
                    cache[output] = 0

    # for k in sorted(cache, key=lambda k: len(cache[k]), reverse=True):
    #     print(k, cache[k])
    
histo()