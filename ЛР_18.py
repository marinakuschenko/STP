words = ["hello", "computer", "yes", "phone", "key", "book"]
string = "".join(words)
rates = {}

for i in string:
    if i not in rates.keys():
        rates[i] = string.count(i) / len(string)

print("Введите слово")
word = input()
chance = 1
for i in word:
    chance *= rates[i]

print(chance)
