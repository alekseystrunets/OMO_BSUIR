
def count_dg(num):
    return len(str(abs(num)))

number = int(input("Введите число: "))

print(f"Количество цифр в числе {number}: {count_dg(number)}")