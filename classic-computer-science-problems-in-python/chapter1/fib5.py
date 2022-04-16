def fib1(n: int) -> int:
    if n == 0:
        return 0
    previous: int = 0
    current: int = 1
    for _ in range(1, n):
        previous, current = current, previous + current
    return current


if __name__ == "__main__":
    print(fib1(50))
