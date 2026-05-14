def factorial(n: int) -> int:
    res = 1
    for i in range(1, n + 1): res *= i
    return res

def harmonic_sum(n: int) -> float:
    return sum(1/i for i in range(1, n + 1))

def multiplication_table(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i*j:4}", end="")
        print()

def main():
    n = int(input("Введіть n: "))
    print(f"{n}! = {factorial(n)}")
    print(f"H({n}) = {harmonic_sum(n):.6f}")
    multiplication_table(n)

if __name__ == "__main__":
    main()
