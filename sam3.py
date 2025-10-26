letters = 0
words = 0
lines = 0

with open('input.txt', 'r') as file:
    for line in file:
        lines += 1
        words += len(line.split())
        for char in line:
            if char.isalpha() and char.isascii():
                letters += 1

print("Input file contains:")
print(f"  {letters} letters")
print(f"  {words} words")
print(f"  {lines} lines")