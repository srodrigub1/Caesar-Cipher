from __future__ import annotations

import unittest
from dataclasses import dataclass

from caesar_cipher import decrypt, encrypt


@dataclass(frozen=True)
class VerificationCase:
    name: str
    operation: str
    text: str
    key: int
    expected: str


VERIFICATION_CASES: tuple[VerificationCase, ...] = (
    VerificationCase(
        name="Encrypt lowercase",
        operation="encrypt",
        text="abc",
        key=3,
        expected="def",
    ),
    VerificationCase(
        name="Decrypt lowercase",
        operation="decrypt",
        text="def",
        key=3,
        expected="abc",
    ),
    VerificationCase(
        name="Wrap-around",
        operation="encrypt",
        text="xyz",
        key=3,
        expected="abc",
    ),
    VerificationCase(
        name="Mixed case + punctuation",
        operation="encrypt",
        text="Hello, World!",
        key=5,
        expected="Mjqqt, Btwqi!",
    ),
    VerificationCase(
        name="Round-trip with large key",
        operation="round_trip",
        text="Python 3.12",
        key=55,
        expected="Python 3.12",
    ),
)


def run_verification_report() -> None:
    """Print a screenshot-friendly verification report in terminal."""
    print("Caesar Cipher - Verification Report")
    print("=" * 40)

    passed_count = 0

    for index, case in enumerate(VERIFICATION_CASES, start=1):
        if case.operation == "encrypt":
            actual = encrypt(case.text, case.key)
        elif case.operation == "decrypt":
            actual = decrypt(case.text, case.key)
        else:
            actual = decrypt(encrypt(case.text, case.key), case.key)

        passed = actual == case.expected
        status = "PASS" if passed else "FAIL"

        print(f"[{index}] {case.name}")
        print(f"    Operation : {case.operation}")
        print(f"    Input     : {case.text!r}")
        print(f"    Key       : {case.key}")
        print(f"    Expected  : {case.expected!r}")
        print(f"    Actual    : {actual!r}")
        print(f"    Result    : {status}")
        print("-" * 40)

        if passed:
            passed_count += 1

    total = len(VERIFICATION_CASES)
    print(f"Summary: {passed_count}/{total} cases passed")

    if passed_count != total:
        raise SystemExit(1)


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
    import sys

    if "--report" in sys.argv:
        run_verification_report()
    else:
        unittest.main()