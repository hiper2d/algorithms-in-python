from secrets import token_bytes
from typing import Tuple


def _random_key(length: int) -> int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")


def encrypt(source: str) -> Tuple[int, int]:
    source_bytes: bytes = source.encode()
    source_key = int.from_bytes(source_bytes, "big")
    dummy_key = _random_key(len(source_bytes))
    encrypted_key = source_key ^ dummy_key
    return dummy_key, encrypted_key


if __name__ == "__main__":
    print(encrypt("11")[1])
