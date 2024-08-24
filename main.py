def main():
    with open("books/frankensten.txt") as f:
        file_contents = f.read()
    print(count_words(file_contents))
    
def count_words(content):
    words = content.split()
    return len(words)
        
        
"""Call the main function at the bottom of the file"""
if __name__ == "__main__":
    main()