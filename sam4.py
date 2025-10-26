with open('input.txt', 'r') as file:
    bad_words = file.read().split()

text = input("Введите текст: ")
print("Исходный:", text)

for word in bad_words:
    stars = '*' * len(word)
    text = text.replace(word, stars)
    text = text.replace(word.upper(), stars)
    text = text.replace(word.title(), stars)

print("Результат:", text)