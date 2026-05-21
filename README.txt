# Caesar Cipher

Simple Caesar cipher encrypter/decrypter in Python. Part of my offensive security learning project ladder.

## Usage
python ceaser_cipher.py<message><method><shift>[--preserve_case]

## Arguments:
- `message` — the text to encrypt or decrypt (wrap in quotes if it contains spaces)
- `method` — `c` to encrypt, `d` to decrypt
- `shift` — integer between 0 and 25
- `--preserve_case` — optional flag; keeps original case instead of uppercasing the output

## Examples
$ python ceaser_cipher.py "hello world" cipher 3
Your ciphered message is: KHOOR ZRUOG

$ python ceaser_cipher.py "Hello World" cipher 3 --preserve_case
Your ciphered message is: Khoor Zruog

$ python ceaser_cipher.py "khoor zruog" decipher 3
Your deciphered message is: HELLO WORLD

## Current behavior
- Encrypts and decrypts using a Caesar shift
- Output is uppercase by default; use `--preserve_case` for mixed-case
- Punctuation and digits are stripped from output (CTF / historical cipher style)
- Spaces are preserved
- Shift validated to 0–25 range
- Method validated to `cipher` / `decipher` via argparse choices

## Roadmap
- Add brute-force mode with English detection
- Optional flag to pass non-letters (punctuation, digits) through unchanged