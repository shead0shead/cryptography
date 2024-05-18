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
