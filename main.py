def read_file(file_name):
    with open(file_name) as f:
        file_contents = f.read()

    return file_contents

def count_words(text):
    return len(text.split())

def count_chars(text):
    chars_occurrencies = dict()
    for c in text:
        if c.lower() in chars_occurrencies:
            chars_occurrencies[c.lower()] += 1
        else:
            chars_occurrencies[c.lower()] = 1


    return chars_occurrencies

def print_report(book_name, words_count, chars_count):
    print(f"--- Begin report of {book_name} ---")
    print(f"{words_count} words found in the document")
    print("")
    for c in chars_count:
        print(f"The '{c}' character was found {chars_count[c]} times")



def main():
    book_path = "./books/frankenstein.txt"
    file_content = read_file(book_path)
    words_count = count_words(file_content)
    chars_count = count_chars(file_content)

    print_report(book_path.strip("./ "), words_count, chars_count)

main()

