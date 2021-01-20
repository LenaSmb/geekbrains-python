mapping = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
}

lines = []

with open('translater.txt') as fd:
    for line in fd:
        word, number = line.split(' — ')

        word_ru = mapping[word.lower()]

        lines.append(word_ru.capitalize() + ' - ' + number)

with open('new_file.txt', 'w') as fd:
    fd.writelines(lines)
