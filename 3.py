def classify_grade(score: int) -> str:
    if 90 <= score <= 100: return "A"
    elif 82 <= score <= 89: return "B"
    elif 74 <= score <= 81: return "C"
    elif 64 <= score <= 73: return "D"
    elif 60 <= score <= 63: return "E"
    elif 35 <= score <= 59: return "FX"
    else: return "F"

def main():
    try:
        score = int(input("Введіть оцінку (0-100): "))
        if not 0 <= score <= 100:
            print("Помилка: діапазон 0-100")
        else:
            grade = classify_grade(score)
            passed = grade not in ("FX", "F")
            print(f"Оцінка {score} → ЄКТС: {grade} ({'Зараховано' if passed else 'Не зараховано'})")
    except ValueError:
        print("Помилка: введіть ціле число")

if __name__ == "__main__":
    main()
