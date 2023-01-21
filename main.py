
def word_count(data):
    words = data.split()
    return len(words)

def letter_count(data):
    letter_count_dict = {}
    words = data.split()

    for word in words:
        for letter in list(word.lower()):
            if letter not in letter_count_dict.keys():
                letter_count_dict[letter] = 1
            else:
                letter_count_dict[letter] = letter_count_dict[letter] + 1


    return letter_count_dict
    
with open("books/frankenstein.txt",'r') as f:
    file_contents = f.read()
#print(file_contents)

num_of_words = word_count(file_contents)
#print(num_of_words)

num_of_letters = letter_count(file_contents)
#print(num_of_letters)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{num_of_words} words found in the document")

list_of_alpha = [x for x in list(num_of_letters) if x.isalpha()]
list_of_alpha.sort()

for alphabet in list_of_alpha:
    print(f"The '{alphabet}' character was found {num_of_letters[alphabet]} times")

print("--- End report ---")