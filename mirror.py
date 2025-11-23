word = input("Введіть слово: ")

reversed_word = ""

for char in word:
    reversed_word = char + reversed_word

print("Перевернуте слово:", reversed_word)
