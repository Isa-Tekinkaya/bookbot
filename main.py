from stats import (
    sorted_letters
)
import sys



def get_book_text(file_path):
    with open(file_path) as file:
        book_text = file.read()
        return book_text
        

def main():
    if len(sys.argv) <=  1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    sorted_letters(book_text)

main()