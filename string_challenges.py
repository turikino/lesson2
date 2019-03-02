# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв а в слове
word = 'Архангельск'
print(len(word))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ['а', 'о', 'у', 'ы', 'э', 'я', 'и', 'ю', 'е']
word_vowels = [letter for letter in word.lower() if letter in vowels]
print(len(word_vowels))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
print(len(words))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
words = []
for word in sentence.split():
    words.append(len(word))
words_average = sum(words)//len(words)
print(words_average)