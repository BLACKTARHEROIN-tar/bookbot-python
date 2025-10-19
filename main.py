from stats import get_book_text
from stats import sort_dict

count_dict, count = get_book_text("books/frankenstein.txt")
sorted_list = sort_dict(count_dict)
print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {count} total words")
print("--------- Character Count -------")
for dic in sorted_list:
    if dic["char"].isalpha():
        print(f"{dic["char"]}: {dic["num"]}")
print("============= END ===============")
    

