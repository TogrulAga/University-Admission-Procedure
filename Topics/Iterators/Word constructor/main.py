word_1 = input()
word_2 = input()

result = ''
for letter_1, letter_2 in zip(word_1, word_2):
    result += letter_1 + letter_2

print(result)
