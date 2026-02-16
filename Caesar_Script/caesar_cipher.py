
from __future__ import annotations


ALPHABET_SIZE = 26


def _shift_char(char: str, key: int) -> str:
    """Shift one alphabetic character by `key` positions.

    Non-alphabetic characters are returned unchanged.
    """
    if not char.isalpha():
        return char

    base = ord("A") if char.isupper() else ord("a")
    shifted = (ord(char) - base + key) % ALPHABET_SIZE
    return chr(base + shifted)


def encrypt(text: str, key: int) -> str:
    """Encrypt text with a Caesar cipher using the provided key."""
    return "".join(_shift_char(char, key) for char in text)


def decrypt(text: str, key: int) -> str:
    """Decrypt text with a Caesar cipher using the provided key."""
    return encrypt(text, -key)


def _read_numeric_key() -> int:
    """Read and validate a numeric key from standard input."""
    while True:
        raw_key = input("Enter the numeric key (integer): ").strip()
        try:
            return int(raw_key)
        except ValueError:
            print("Invalid key. Please enter a whole number.")


def main() -> None:
    """Run an interactive Caesar cipher session."""
    print("Caesar Cipher (Python)")
    print("1) Encrypt")
    print("2) Decrypt")

    option = input("Choose an option (1 or 2): ").strip()
    if option not in {"1", "2"}:
        print("Invalid option. Please run the program again and choose 1 or 2.")
        return

    message = input("Enter the message: ")
    key = _read_numeric_key()

    if option == "1":
        result = encrypt(message, key)
        print(f"Encrypted message: {result}")
    else:
        result = decrypt(message, key)
        print(f"Decrypted message: {result}")


if __name__ == "__main__":
    main()
