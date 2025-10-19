from stats import get_book_text
from stats import sort_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
print(sys.argv)
count_dict, count = get_book_text(sys.argv[1])
sorted_list = sort_dict(count_dict)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {count} total words")
print("--------- Character Count -------")
for dic in sorted_list:
    if dic["char"].isalpha():
        print(f"{dic["char"]}: {dic["num"]}")
print("============= END ===============")
