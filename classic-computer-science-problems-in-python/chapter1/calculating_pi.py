def calculate_pi(n_terms: int) -> float:
    nominator = 4.0
    denominator = 1.0
    operation = 1.0
    pi = 0.0
    for _ in range(n_terms):
        pi += operation * (nominator / denominator)
        operation *= -1.0
        denominator += 2.0
    return pi


if __name__ == "__main__":
    # π = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11...
    print(calculate_pi(100000))
