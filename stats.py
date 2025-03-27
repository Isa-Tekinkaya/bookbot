import sys

def num_of_words(book_text):
    words = book_text.split()
    return len(words)

def num_of_letters(book_text):
    letters = {}
    for letter in book_text.lower():
        if letter.isalpha():
            letters[letter] = letters.get(letter, 0) + 1
    return letters

def sorted_letters(book_text):
    total_words = book_text.split()  # Split the book text into words
    letters = num_of_letters(book_text)  # Get the frequency of each letter
    sorted_letters_frequency = sorted(letters.items(), key=lambda x: x[1], reverse=True)  # Sort the letters by frequency
    
    # Format sorted letters as a string to print neatly
    sorted_letters_str = "\n".join([f"{letter}: {count}" for letter, count in sorted_letters_frequency])
    print("============ BOOKBOT ============")
    # Print the result in a readable format
    print("Analyzing book found at", sys.argv[1], "...")
        
    print(f"""----------- Word Count ----------
Found {len(total_words)} total words
--------- Character Count -------
{sorted_letters_str}
============ END ===============""")






