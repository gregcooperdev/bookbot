def main():
    book_path = "books/frankenstein.txt"    
    print(f"--- Begin report of {book_path} ---")
    with open(book_path) as f:
        text = f.read()             #reads book and stores as variable text
    num_words = word_count(text)    #passes text into function to count words
    print(f"There are {num_words} words in this document.")
    num_letters = letter_count(text)
    num_letters.sort(reverse=True, key=sort_letters)
    for item in num_letters:
        print(f"The '{item['char']}' character was found {item['count']} times")
    print(f"--- End of {book_path} report ---")

def word_count(passage):
    words = passage.split()
    return len(words)

def letter_count(letters):
    letter_dict = {}
    low_letters = letters.lower()
    for letter in low_letters:
        if letter.isalpha():        #checks if a string is only alphabetic character
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    count_list = [{"char": char, "count": count} for char, count in letter_dict.items()]
    #above converts dictionary into a list of dictionaries
    return count_list

def sort_letters(item):
    return item["count"]

main()