alphabet = 'abcdefghijklmnopqrstuvwxyz'

# 1 - Encrypt 2 - Decrypt
type = 1
# Shift step
step = 3
# Your text
text = 'Example'

# Do not touch it
output = ''

for i in range(len(text)):
    letter = text.lower()[i]
    index = alphabet.find(letter)
    if type == 1: new_index = (index + step) % len(alphabet)
    else: new_index = (index - step) % len(alphabet)
    output += ''.join(alphabet[new_index])

print(output)
