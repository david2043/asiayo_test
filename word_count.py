import re

with open("words.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

words = re.findall(r"[a-z]+", text)

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

max_word = ""
max_count = 0

for word in count:
    if count[word] > max_count:
        max_count = count[word]
        max_word = word

print(max_count, max_word)
