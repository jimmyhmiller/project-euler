from itertools import product, izip, cycle
from string import ascii_letters


ascii_letters = set(l for l in ascii_letters)
f = open("cipher.txt", "r")
g = open("words.txt", "r")
words = g.read()
data = f.read()
data = [int(i) for i in data.split(",")]
words = set(w.lower() for w in words.split(","))
lowercase_letters = range(97,123)


def decrypt(key,text):
    return "".join(chr(x ^ y) for (x,y) in izip(text, cycle(key)))


def contains_words(text):
    text = text.lower()
    total = 0
    for word in words:
        if word in text and len(word) > 3:
            total += 1
        if total > 2:
            return True
    return False


def main():
    for key in product(lowercase_letters,repeat=3):
        if contains_words(decrypt(key,data[:60])):
            print sum(x ^ y for (x,y) in izip(data, cycle(key)))


if __name__ == '__main__':
    main()