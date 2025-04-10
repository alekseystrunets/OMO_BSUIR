
str = input("Введите строку слов, разделенных пробелами: ")

words = str.split()

longest_word = max(words, key=len)

print(f"Результат: {longest_word}")