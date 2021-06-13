sentence = input()

filtered_sentence = ''.join(filter(lambda x: x not in ",.!?", sentence)).lower()
print(filtered_sentence)
