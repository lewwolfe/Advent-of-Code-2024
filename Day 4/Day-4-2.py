from typing import List

def load_word_search() -> List[List[str]]:
    word_search = []
    with open("Day-4-input.txt", "r") as input_file:
        for line in input_file:
            word_search.append([char for char in line.strip()])
    return word_search

def check_diagonal(word_search) -> int:
    total = 0
    for y, level in enumerate(word_search):
        for x, char in enumerate(level):
            if char == '.':
                continue
            if (y + 2) <= len(word_search)-1 and (x + 2) <= len(level)-1:
                first =  char + word_search[y+1][x+1] + word_search[y+2][x+2]
                second = word_search[y][x+2] + word_search[y+1][x+1] + word_search[y+2][x]
                print(x, y, "first", first, "second", second)
                if (first == "MAS" or first == "SAM") and (second == "MAS" or second == "SAM"):
                    total += 1
    return total

def main():
    word_search = load_word_search()
    total_occurrences = check_diagonal(word_search)
    print(f"Total occurrences: {total_occurrences}")

if __name__ == "__main__":
    main()