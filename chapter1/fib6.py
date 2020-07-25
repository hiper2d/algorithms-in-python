from typing import Generator


def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    first = 0
    second = 1
    for _ in range(1, n):
        first, second = second, first + second
        yield second


if __name__ == "__main__":
    for i in fib6(10):
        print(i)
