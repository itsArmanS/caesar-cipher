import argparse

parser = argparse.ArgumentParser(description="Cipher or decipher messages using the Caesar Cipher")
parser.add_argument("message", type=str, help="Input message to cipher/decipher" )
parser.add_argument("method", type=str, choices=['c', 'd'], default="c", help="Input c to cipher message / d to decipher" )
parser.add_argument("shift", type=int, help="Cipher shift amount (0 - 25)")

args = parser.parse_args()

if not 0 <= args.shift <= 25:
    parser.error("Shift must be between 0 and 25")

message = args.message.lower()

ciphered_message = ""

for letter in message:
    if letter == " ":
        ciphered_message += letter
    elif letter.isalpha(): 
        position = ord(letter) - ord("a")
        if args.method == "c":
            shifted_position = (position + args.shift) % 26
        else:
            shifted_position = (position - args.shift) % 26

        shifted_letter = chr(shifted_position + ord("a"))
        ciphered_message += shifted_letter

if args.method == "c":
    print(f"Your ciphered message is: {ciphered_message.upper()}")
else:
    print(f"Your deciphered message is: {ciphered_message.upper()}")
