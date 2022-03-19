# Create a program that returns the most common letter


# map through sentence and every letter add one to that letter in dictionary print the letter with the
# most after the final iteration


sentence = "This is a common interview question"
sentence2 = sentence.replace(" ", "")

char_frequency = {}

for char in sentence2:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_sorted = sorted(char_frequency.items(),
                               key=lambda kv: kv[1],
                               reverse=True)

print(char_frequency_sorted[0])
