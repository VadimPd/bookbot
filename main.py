from stats import word_count
from stats import character_count
from stats import get_book_txt
from stats import sorted_list
from stats import formatted_text
import sys


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path_to_file = sys.argv[1]
text = get_book_txt(path_to_file)
file_contents = get_book_txt(path_to_file)

def main():
    print(f"============ BOOKBOT ============ \nAnalyzing book found at {path_to_file}...\n----------- Word Count ----------\nFound {len(word_count(path_to_file))} total words\n --------- Character Count -------\n{formatted_text(text)} \n============= END ===============")
main()