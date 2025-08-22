from stats import get_book_text, get_number_symbols, sort_dict
import sys
import os

def main():
    file_name = ""

    if len(sys.argv) == 2:
        # args must be equal to two and if they are, run this code
        file_name = sys.argv[1] 
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    if not os.path.exists(file_name):
        print("Usage: Err - File path does not exist, exitting program")
        sys.exit()

    content = get_book_text(file_name)
    dicti = get_number_symbols(file_name)
    sorting = sort_dict(dicti)

    print("Found",content, "total words")
    for char in dicti:
        print(f"{char}: {dicti[char]}")
    print(sorting)

main()


