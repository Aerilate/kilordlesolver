import fileinput
from collections import defaultdict
  

class Bitmap:

    def __init__(self):
        self.bits = [ [0] * 5 for _ in range(26)]

    def add(self, word):
        for ind, letter in enumerate(word):
            letter = ord(letter) - ord('a')
            self.bits[letter][ind] = 1

    def p(self):
        for ind, val in enumerate(self.bits):
            print(chr(ind + ord('a')) + " " + "".join([str(n) for n in val]))

def main():
    words = []
    for line in fileinput.input('words.txt'):
        words.append(line.strip())

    dex = defaultdict(dict)
    for word in words:
        for idx, letter in enumerate(word):
            dex[letter][idx] = word

    result = []
    b = Bitmap()
    for i in range(26):
        for j in range(5):
            if not b.bits[i][j]:
                if chr(i + ord('a')) in dex and j in dex[chr(i + ord('a'))]:
                    b.add(dex[chr(i + ord('a'))][j])
                    result.append(dex[chr(i + ord('a'))][j])

    # b.p()
    for a in result:
        print(a)
    print(len(result))


if __name__ == "__main__":
    main()
