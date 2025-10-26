with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()

print("Анализ файла input.txt:")
print(f"Всего символов: {len(text)}")

chars = {}
for char in text:
    if char not in ' \n\t':
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

print("\nСамые частые символы:")
sorted_chars = sorted(chars.items(), key=lambda x: x[1], reverse=True)
for char, count in sorted_chars[:5]:
    print(f"'{char}': {count}")

print("\nСамые редкие символы:")
for char, count in sorted_chars[-5:]:
    print(f"'{char}': {count}")