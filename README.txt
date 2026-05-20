# Caesar Cipher

Simple Caesar cipher encrypter/decrypter in Python. Part of my offensive security learning project ladder.

## Usage
python ceaser_cipher.py

Then enter:
- The message to encrypt or decrypt
- C to encrypt, D to decrypt
- The shift amount (0-25)

## Example
Enter a phrase to cipher/decrypt: hello world
Input C to Cipher | Enter D to Decipher: C
Enter a shift amount between 0 and 25: 3
Your ciphered message is: KHOOR ZRUOG

## Current behavior
- Encrypts and decrypts using a Caesar shift
- Output is uppercase regardless of input case
- Punctuation and digits are stripped from output (to maintain integrity / resist trivial pattern analysis)
- Spaces are preserved

## Roadmap
- Add brute-force mode with English detection
- Switch from input() to argparse CLI args
- Preserve original case of input
- Input validation (reject non-numeric shifts, invalid mode characters)