file = open('input.txt', 'r')
original_text = file.read()
file.close()

def get_replacement(word_type):
    return input(f"Enter a {word_type.lower()}: ")

placeholders = ["ADJECTIVE", "NOUN", "ADVERB", "VERB"]

words = original_text.split()
for i in range(len(words)):
    word = words[i].strip('.,;:!?')
    if word in placeholders:
        replacement = get_replacement(word)
        words[i] = words[i].replace(word, replacement)
modified_text = ' '.join(words)

print("\nModified text:")
print(modified_text)

file = open('output.txt', 'w')
file.write(modified_text)
file.close()

print("\nThe modified text has been saved to 'output.txt'")