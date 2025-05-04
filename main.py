def get_book_text (books):

    with open(books) as file:
        file_contents = file.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print (book_text)

main()