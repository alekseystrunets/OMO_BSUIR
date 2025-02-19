
arr = [
    [0, -2, 16],
    [0, -2, 234],
    [7, -1, -6],
    [1, -1, 15]
]

new_array = []
for row in arr:
    new_row = []
    for element in row:
        if element > 0:
            new_row.append(1)
        else:
            new_row.append(0)
    new_array.append(new_row)

print("Изначальный массив:")
for row in arr:
    print(row)

print("\nНовый массив:")
for row in new_array:
    print(row)