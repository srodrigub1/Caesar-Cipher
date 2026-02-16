import unittest

from caesar_cipher import decrypt, encrypt


class CaesarCipherTests(unittest.TestCase):
    def test_encrypt_basic_lowercase(self) -> None:
        self.assertEqual(encrypt("abc", 3), "def")

    def test_decrypt_basic_lowercase(self) -> None:
        self.assertEqual(decrypt("def", 3), "abc")

    def test_wraparound_behavior(self) -> None:
        self.assertEqual(encrypt("xyz", 3), "abc")

    def test_mixed_case_and_punctuation(self) -> None:
        self.assertEqual(encrypt("Hello, World!", 5), "Mjqqt, Btwqi!")

    def test_round_trip_with_large_key(self) -> None:
        original = "Python 3.12"
        encrypted = encrypt(original, 55)
        self.assertEqual(decrypt(encrypted, 55), original)


if __name__ == "__main__":
    unittest.main()
