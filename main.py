import fileinput
from scipy.optimize import linprog


def hash(word):
    hash = [0] * 26 * 5
    for ind, c in enumerate(word):
        letter = ord(c) - ord('a')
        hash[letter * 5 + ind] = -1
    return hash

def possible(words):
    res = hash(words[0])
    for word in words:
        h = hash(word)
        for i in range(len(h)):
            if h[i] == -1:
                res[i] = -1
    return 0 not in res

def run(words, bound):
    lhs_ineq = [[] for _ in range(26 * 5)]
    for word in words:
        h = hash(word)
        for i, bit in enumerate(h):
            lhs_ineq[i].append(bit)

    obj = [1] * len(words)
    rhs_ineq = [-1] * 26 * 5
    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, 
                                 method="revised simplex")

    result = []
    for i, x in enumerate(opt.x):
        if x > bound:
            result.append(words[i])
    print(possible(result), len(result))
    return result

def main():
    words = []
    for line in fileinput.input('words.txt'):
        words.append(line.strip())

    for bound in [0, 0.2, 0.2]:
        words = run(words, bound)
    print(words)


if __name__ == "__main__":
    main()
