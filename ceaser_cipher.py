message = input("Enter a phrase to cipher: ")
# message = 'testing'
shift = input("Enter a shift amount between 0 and 25: ")

ciphered_word = ""

for letter in message:
    if letter == " ":
        ciphered_word += letter
    else:
        position = ord(letter) - ord("a")
        shifted_position = (position + int(shift)) % 26
        shifted_letter = chr(shifted_position + ord("a"))
        ciphered_word += shifted_letter


print(ciphered_word)


