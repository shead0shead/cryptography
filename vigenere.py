# (index1 + 1) + (index2 + 1) - 2 = index3
# index1 + index2 + 2 - 2 = index3
# index1 + index2 = index3

alphabet = 'abcdefghijklmnopqrstuvwxyz'

secret = 'Chair'
text = 'Example'

output = ''

for i in range(len(text)):
    letter = text.lower()[i]
    letter2 = secret.lower()[i % len(secret)]
    index = alphabet.find(letter)
    index2 = alphabet.find(letter2)
    new_index = (index + index2) % len(alphabet)
    output += ''.join(alphabet[new_index])

print(output)
