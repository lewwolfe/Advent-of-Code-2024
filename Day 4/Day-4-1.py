from typing import List

def load_word_search() -> List[List[str]]:
    word_search = []
    with open("Day-4-input.txt", "r") as input_file:
        for line in input_file:
            word_search.append([char for char in line.strip()])
    # data = [
    #     "X..S",
    #     "M..A",
    #     "A..M",
    #     "S..X"
    # ]
    # for line in data:
    #     word_search.append([char for char in line])
    return word_search

def check_horizontal(word_search) -> int:
    total = 0
    for level in word_search:
        word = ""
        for c in level:
            word += c
        total += word.count("XMAS")
        total += word.count("SAMX")
    print("hoz", total)
    return total

def check_vertical(word_search) -> int:
    total = 0
    words = []
    for y, level in enumerate(word_search):
        for x, char in enumerate(level):
            if y < 1:
                words.append("")
            words[x] += char
    for word in words:
        total += word.count("XMAS")
        total += word.count("SAMX")
    print("ver", total)
    return total

def check_diagonal(word_search) -> int:
    total = 0
    for y, level in enumerate(word_search):
        for x, char in enumerate(level):
            word = ""
            if (y + 3) <= len(word_search)-1 and (x + 3) <= len(level)-1:
                word = char + word_search[y+1][x+1] + word_search[y+2][x+2] + word_search[y+3][x+3]
                total += word.count("XMAS")
                total += word.count("SAMX")
            if (y + 3) <= len(word_search)-1 and x >= 3:
                word = char + word_search[y+1][x-1] + word_search[y+2][x-2] + word_search[y+3][x-3]
                total += word.count("XMAS")
                total += word.count("SAMX")
    print("diag", total)
    return total

def main():
    word_search = load_word_search()
    total_occurrences = 0
    total_occurrences += check_horizontal(word_search)
    total_occurrences += check_vertical(word_search)
    total_occurrences += check_diagonal(word_search)
    print(f"Total occurrences: {total_occurrences}")

if __name__ == "__main__":
    main()