import string
excluded = string.punctuation[0:6] + string.punctuation[7:32]

def word_count(s):
    counter = {}
    for word in s.split():
        out = "".join(c for c in word if c not in (excluded))
        out = out.lower()
        try:
            counter[out]
            counter[out] += 1

        except KeyError:
            counter[out] = 1
    print(counter)
    return counter

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))