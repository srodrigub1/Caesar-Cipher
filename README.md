# Caesar Cipher (Python)

A simple Python implementation of the Caesar cipher with:

- **Encryption** and **decryption** functions
- Proper handling of **uppercase/lowercase** letters
- Preservation of **spaces, numbers, and punctuation**
- An interactive **CLI main program**
- Basic **unit tests**

## Project structure

```text
Caesar-Cipher/
├── README.md
└── Caesar_Script/
    ├── caesar_cipher.py
    └── tests.py
```

## How the code works

The core logic is in `Caesar_Script/caesar_cipher.py`.

### 1. Character shifting: `_shift_char(char, key)`

- If the character is not alphabetic (`isalpha()`), it returns it unchanged.
- For letters, it:
  1. Detects base ASCII code (`A` for uppercase, `a` for lowercase).
  2. Applies the shift with modulo 26.
  3. Converts back to a character.

This gives correct wrap-around behavior (e.g., `z` + 3 -> `c`).

### 2. Text encryption: `encrypt(text, key)`

- Applies `_shift_char` to every character in the input text.
- Returns the encrypted string.

### 3. Text decryption: `decrypt(text, key)`

- Reuses `encrypt` with a negative key.
- This keeps the implementation concise and consistent.

### 4. Interactive key input: `_read_numeric_key()`

- Repeatedly asks the user for a key.
- Accepts only whole numbers (`int`).
- Shows an error message and retries on invalid input.

### 5. Program entry point: `main()`

When you run the file directly, `main()` starts an interactive session:

1. Displays a menu:
   - `1) Encrypt`
   - `2) Decrypt`
2. Validates the option.
3. Reads the message.
4. Reads a numeric key.
5. Prints either:
   - `Encrypted message: ...`
   - `Decrypted message: ...`

The line `if __name__ == "__main__": main()` makes this interactive mode run only when the script is executed directly.

## Usage

From the repository root:

```bash
cd Caesar_Script
python3 caesar_cipher.py
```

Example interaction:

```text
Caesar Cipher (Python)
1) Encrypt
2) Decrypt
Choose an option (1 or 2): 1
Enter the message: Hello, World!
Enter the numeric key (integer): 5
Encrypted message: Mjqqt, Btwqi!
```

## Running tests

The tests are in `Caesar_Script/tests.py` and use Python's built-in `unittest`.

Run them with:

```bash
cd Caesar_Script
python3 -m unittest tests.py
```

The test suite covers:

- Basic encryption/decryption
- Alphabet wrap-around (`xyz` -> `abc`)
- Mixed case and punctuation
- Round-trip correctness with large keys