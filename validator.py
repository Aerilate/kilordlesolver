import fileinput

guess_file = "valid_answers.txt"

def mark_letter_placements(filename):
    words = set(line.strip() for line in fileinput.input(filename))

    letters = [[0, 0, 0, 0, 0] for _ in range(26)]
    for word in words:
        for idx, val in enumerate(word):
            letters[ord(val) - ord('a')][idx] = 1
    return letters

def print_letter_placements(letters):
    for idx, val in enumerate(letters):
        print(f"{chr(idx + ord('a'))}: {val}")

print_letter_placements(mark_letter_placements(guess_file))
