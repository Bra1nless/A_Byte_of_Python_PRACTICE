poem = '''Программировать весело.
Если работа скучна,
Чтобы придать ей веселый тон -
    использу Python!
'''

with open('poem.txt', 'w') as f:
    f.write(poem)


with open('poem.txt') as f:
    for line in f:
        print(line, end='')