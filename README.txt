# Caesar Cipher

Simple Caesar cipher encrypter/decrypter in Python. Part of my offensive security learning project ladder.

## Usage
python ceaser_cipher.py<message><method><shift>

Arguments:
- `message` — the text to encrypt or decrypt (wrap in quotes if it contains spaces)
- `method` — `c` to encrypt, `d` to decrypt
- `shift` — integer between 0 and 25

## Example
$ python ceaser_cipher.py "hello world" c 3
Your ciphered message is: KHOOR ZRUOG

$ python ceaser_cipher.py "khoor zruog" d 3
Your deciphered message is: HELLO WORLD

## Current behavior
- Encrypts and decrypts using a Caesar shift
- Output is uppercase regardless of input case
- Punctuation and digits are stripped from output (to maintain integrity / resist trivial pattern analysis)
- Spaces are preserved
- Shift validated to 0–25 range
- Method validated to `c` / `d` via argparse choices

## Roadmap
- Add brute-force mode with English detection
- Preserve original case of input
- Switching method values to `encrypt`/`decrypt` for readability
