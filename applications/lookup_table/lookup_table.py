# Your code here
cache = {}

import math
def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    try:
        #See if the value is in the cache, if it is. Just return it!
        cache[x,y]
        return cache[x,y]
    except KeyError:
        #If it isn't in the cache, operate normally, add it to the cache and move on
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        cache[x,y] = v
        return v



# Do not modify below this line!
import random
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
