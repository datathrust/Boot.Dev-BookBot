def read_book(target):
    with open(target) as f:
        contents = f.read()
        return contents

def word_count(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_counts = []
    for c in text:
        c = c.lower()
        if c.isalpha(): #Skip non-letters
            if not any(dict['char'] == c for dict in character_counts):
                character_counts.append({'char': c, 'count': 1})
            else:
                for dict in character_counts:
                    if dict['char'] == c:
                        dict['count'] += 1
    
    return character_counts

def sort_on(dictionary):
    return dictionary['count']

def main():
    target = 'books/frankenstein.txt'
    text = read_book(target)
    characters = count_characters(text)
    characters.sort(reverse=True, key=sort_on)

    #Output Report to Console:
    print(f"--- Being report of {target} ---")
    print(f"{word_count(text)} words found in document\n")

    #TODO: Sort
    #for char, count in characters.items():
    #    print(f"The character '{char} was found {count} times.")
    for line in characters:
        print(f"The '{line['char']}' character was found {line['count']} times")

    print("\n--- End report ---")

main()