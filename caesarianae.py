alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Your text
text = 'Example'
# Shift step
step = 3
# 'encrypt' or 'decrypt'
mode = 'encrypt'

# Do not touch it
output = ''

for i in range(len(text)):
    letter = text.lower()[i]
    index = alphabet.find(letter)
    if mode == 'encrypt': new_index = (index + step) % len(alphabet)
    else: new_index = (index - step) % len(alphabet)
    output += ''.join(alphabet[new_index])

print(output)
