with open('article.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = text.lower().split()
clean_words = []
for word in words:
    clean_word = ''.join(char for char in word if char.isalpha())
    if clean_word:
        clean_words.append(clean_word)

total = len(clean_words)
print(f"Всего слов: {total}")

from collections import Counter
word_counts = Counter(clean_words)
most_common = word_counts.most_common(1)[0]

print(f"Самое частое слово: '{most_common[0]}' ({most_common[1]} раз)")