def get_book_text(book_path):
    with open(book_path) as f:
        letters_dict = {}
        count = 0
        contents = f.read()
        lower_contents = contents.lower()
        words = lower_contents.split()
        for word in words:
            count = count + 1
            word_string = " ".join(word)
            chars = word_string.split() 
            for char in chars:
                if char in letters_dict:
                    letters_dict[char] = letters_dict[char] + 1
                else:
                    letters_dict[char] = 1
        

        print(letters_dict)
        print(f"Found {count} total words")
