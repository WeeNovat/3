import math

def main():
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: "))

    sum_squares = a**2 + b**2 + c**2
    average = (a + b + c) / 3
    discriminant = b**2 - 4 * a * c
    hypotenuse = math.sqrt(a**2 + b**2)
    
    is_triangle = (a + b > c) and (a + c > b) and (b + c > a)

    print(f"\nРезультати:")
    print(f"1. Сума квадратів: {sum_squares:.2f}")
    print(f"2. Середнє арифметичне: {average:.2f}")
    print(f"3. Дискримінант: {discriminant:.2f}")
    print(f"4. Гіпотенуза (a, b): {hypotenuse:.2f}")
    print(f"5. Чи є трикутником: {'Так' if is_triangle else 'Ні'}")

if __name__ == "__main__":
    main()
