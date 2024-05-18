alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Secret word
secret = 'Chair'
# Your text
text = 'Example'
# 'encrypt' or 'decrypt'
mode = 'encrypt'

# Do not touch it
output = ''

if mode == 'encrypt':
    for i in range(len(text)):
        letter = text.lower()[i]
        letter2 = secret.lower()[i % len(secret)]
        index = alphabet.find(letter)
        index2 = alphabet.find(letter2)
        new_index = (index + index2) % len(alphabet)
        output += ''.join(alphabet[new_index])
else:
    for i in range(len(text)):
        letter = text.lower()[i]
        letter2 = secret.lower()[i % len(secret)]
        index = alphabet.find(letter)
        index2 = alphabet.find(letter2)
        new_index = (index - index2) % len(alphabet)
        output += ''.join(alphabet[new_index])

print(output)
