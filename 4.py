import math

def triangle_type(a: float, b: float, c: float) -> str:
    if not (a + b > c and a + c > b and b + c > a):
        return "не є трикутником"
    
    sides = sorted([a, b, c])
    is_right = abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-9
    
    if a == b == c: return "рівносторонній"
    elif a == b or b == c or a == c:
        return "рівнобедрений прямокутний" if is_right else "рівнобедрений"
    elif is_right: return "прямокутний"
    else: return "різносторонній"

def triangle_area(a: float, b: float, c: float) -> float:
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def main():
    a = float(input("Сторона a: "))
    b = float(input("Сторона b: "))
    c = float(input("Сторона c: "))
    
    t_type = triangle_type(a, b, c)
    print(f"Тип: {t_type}")
    if t_type != "не є трикутником":
        print(f"Площа: {triangle_area(a, b, c):.2f}")

if __name__ == "__main__":
    main()
