
def nod(a, b):
    while b != 0:
        tm = a
        a = b
        b = tm % b
    return a

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

result = nod(num1, num2)

print(f"НОД при значениях  {num1} и {num2} равен : {result}")