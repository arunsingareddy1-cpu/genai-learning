#Give two senteces about the word and extract all words
str = "Im learning python programming and it's really fun! Im learning python programming and it's really fun!"
def extract_words(str):
    words= str.split(" ")
    return words

print(extract_words(str))

def remove_duplicate_words(str):
    words = str.split(" ")
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return unique_words

print(remove_duplicate_words(str))