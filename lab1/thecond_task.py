
def calculation(x):
    if x + 5 == 0:
        return "Знаменатель не может быть равен нулю Ошибка: (x = -5)"
    y = (x ** 3) / (2 * (x + 5))
    return y

x = float(input("Введите значение x: "))
result = calculation(x)

print(f"При x = {x}, y = {result}")