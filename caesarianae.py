alphabet = 'abcdefghijklmnopqrstuvwxyz'

type = 1
step = 3

input = 'Example'
output = ''

for i in range(len(input)):
    letter = input.lower()[i]
    index = alphabet.find(letter)
    if type == 1: new_index = (index + step) % len(alphabet)
    else: new_index = (index - step) % len(alphabet)
    output += ''.join(alphabet[new_index])

print(output)
