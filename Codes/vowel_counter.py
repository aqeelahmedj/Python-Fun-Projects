'''Problem: Word Vowel Counter
Write a Python program that:

Asks the user to enter a word (string).
Counts how many vowels (a, e, i, o, u) are in the word.

Prints:
The number of vowels.
The number of consonants.
And the word in reverse.

'''

vowel_count = 0
user_input = str(input(f"Enter any word: "))
print(user_input)

for letter in user_input:
    if letter == 'a' or 'e' or 'i' or 'o' or 'u':
        vowel_count = vowel_count + 1

    print("total vowels", vowel_count)



