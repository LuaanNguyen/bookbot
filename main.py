def main():
    book_path = "books/frankensten.txt"
    print(f"--- Begin report of {book_path} ---")
    
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
    print()
    
    chars_dict = get_char_dict(text)
    print_report(chars_dict)
    print("--- End report ---")
    
def get_num_words(content):
    words = content.split()
    return len(words)

def get_char_dict(text): 
    count = {}
    for s in text:
        lowered_string = s.lower()
        count[lowered_string] = count.get(lowered_string, 0) + 1 
    return count

def print_report(count):
    #connvert the dictionary into a list
    count_list = list(count.items())
        
    count_list.sort(reverse= True, key = lambda x: x[1])
    
    for char, count in count_list:
        if char.isalpha():
            print(f"The '{char}' was found {count} times")
        
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents
    
"""Call the main function at the bottom of the file"""
if __name__ == "__main__":
    main()