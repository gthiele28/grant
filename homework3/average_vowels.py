# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 
def counting_vowels_and_consonants(pg):
    vowels = 0
    cons = 0

    for i in pg:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vowels += 1
        else:
            cons += 1
    
    return (vowels, cons)

def average_vowels_and_consonants(pg):
    sentences = pg.split(".")
    divide = len(sentences)
    total_vowels = 0
    total_cons = 0

    for i in sentences:
        sentence = counting_vowels_and_consonants(i)
        total_vowels += sentence[0]
        total_cons += sentence[1]

    avg_vowels = total_vowels / divide
    avg_cons = total_cons / divide

    return (avg_vowels, avg_cons)

averages = average_vowels_and_consonants(paragraph)
print(f"In this quote, there are, on average, {averages[0]:.2f} vowels per sentence and {averages[1]:.2f} consonants per sentence")