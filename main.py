
from stats import number_of_words , number_of_characters, sorted_list_of_dictionaries
import sys
book_path = ""

def get_book_text(book_path):
        with    open(book_path) as file:
                book_text = file.read()
        return book_text

def main():
        
        if len(sys.argv) > 1:
                book_path = sys.argv[1]
                book_text = get_book_text(book_path)
                word_count = number_of_words(book_text)
                dict_chars = number_of_characters(book_text)
                sorted_chars = sorted_list_of_dictionaries(dict_chars)

                print("============ BOOKBOT ============")
                print(f"Analyzing book found at books/frankenstein.txt...")
                print("----------- Word Count ----------")
                print(f"Found {word_count} total words")
                print("--------- Character Count -------")
                for char, count in sorted_chars:
                        print(f"{char}: {count}")
                print("============= END ===============")
        else:
                print("Usage: python3 main.py <path_to_book>")
                sys.exit(1)
main()