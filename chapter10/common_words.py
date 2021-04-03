def count_common_words(filename, word):
    """Count how many times a word appears in a book."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)


        msg = f"'{word}' appesrs in {filename} about {word_count} times."
        print(msg)

filename = 'sherlock_holmes.txt'
count_common_words(filename, 'the')
