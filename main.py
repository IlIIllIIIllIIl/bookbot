def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    final_report = report(book_path, num_words, chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        if c.isalpha() == True:
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def report_sort(new_dict):
    #dict_to_list = list(dict.items())
    final = sorted(new_dict.items(), key=lambda x: x[1], reverse=True)
    for letter, number in final:
        print(f"The {letter} character was found {number} times")

def report(path, word_count, dict):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    report_sort(dict)
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()