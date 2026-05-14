def main():
    raw_input = input("Введіть число: ")

    try:
        val_float = float(raw_input)
        val_int = int(val_float)
        val_bool = bool(val_float)
        
        print(f"\nТипи даних:")
        print(f"Рядок: '{raw_input}' | {type(raw_input)}")
        print(f"Целе: {val_int} | {type(val_int)}")
        print(f"Дійсне: {val_float:.2f} | {type(val_float)}")
        print(f"Булеве: {val_bool} | {type(val_bool)}")
    except ValueError:
        print("Помилка: введене значення не є числом!")

    print(f"\n{' Демонстрація функцій ':=^30}")
    name, age = "Олексій", 19
    print(f"Ім'я: {name:<10} | Вік: {age:03d}")
    
    r_list = list(range(1, 6))
    print(f"Список: {r_list} | Довжина: {len(r_list)} | ID: {id(r_list)}")

if __name__ == "__main__":
    main()
