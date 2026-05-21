import argparse

parser = argparse.ArgumentParser(description="Cipher or decipher messages using the Caesar Cipher")
parser.add_argument("message", type=str, help="Input message to cipher/decipher" )
parser.add_argument("method", type=str, choices=['cipher', 'decipher'], default="cipher", help="Input cipher to cipher message / decipher to decipher" )
parser.add_argument("shift", type=int, help="Cipher shift amount (0 - 25)")
parser.add_argument("--preserve_case", action="store_true", help="Preserve original case (mixed-case output) instead of forcing uppercase")

args = parser.parse_args()

verb = "ciphered" if args.method == "cipher" else "deciphered"

if not 0 <= args.shift <= 25:
    parser.error("Shift must be between 0 and 25")

ciphered_message = ""

for letter in args.message:
    if letter == " ":
        ciphered_message += letter
    elif letter.isalpha():     

        anchor = ord("a") if letter.islower() else ord("A")
        position = ord(letter) - anchor
            
        if args.method == "cipher":
            shifted_position = (position + args.shift) % 26
        else:
            shifted_position = (position - args.shift) % 26

        shifted_letter = chr(shifted_position + anchor)

        ciphered_message += shifted_letter

output = ciphered_message if args.preserve_case else ciphered_message.upper()
print(f"Your {verb} message is: {output}")

    