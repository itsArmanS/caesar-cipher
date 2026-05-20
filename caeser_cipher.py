message = input("Enter a phrase to cipher/decrypt: ")
message = message.lower()

cipher_method = input("Input C to Cipher | Enter D to Decipher: ")

shift = input("Enter a shift amount between 0 and 25: ")

ciphered_message = ""

for letter in message:
    if letter == " ":
        ciphered_message += letter
    elif letter.isalpha(): 
        position = ord(letter) - ord("a")
        if cipher_method == "C":
            shifted_position = (position + int(shift)) % 26
        else: 
            shifted_position = (position - int(shift)) % 26

        shifted_letter = chr(shifted_position + ord("a"))
        ciphered_message += shifted_letter

if cipher_method == "C":
    print(f"Your ciphered message is: {ciphered_message.upper()}")
else:
    print(f"Your deciphered message is: {ciphered_message.upper()}")
