# encoding=UTF-8

with open('referat.txt', 'r', encoding = 'utf-8') as text:
    word_count = 0
    for line in text:
        word_count += len(line.split())
        # print(line.decode())
    print('В файле', word_count, 'слов')
