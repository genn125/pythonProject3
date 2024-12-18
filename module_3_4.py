
# module_3_4.py

# "Однокоренные" - использования параметров *args/ **kwargs на практике

def single_root_words(txt, *other_words, root_word='гриб'):
    same_words = []

    for i in other_words:

        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)

    return print(f"{txt} {', '.join([*same_words,])}", end='\n\n')   # Не понятно как распечатался список, который выводился кортежем

single_root_words('"гриб" есть в словах:','грибник', 'гриБной', 'гробница', 'грибОЧЕк')
single_root_words('В слове "обелиск" присутствуют слова:','Чёрный', 'Обе', 'двЕ', 'ЛИС',
                  root_word = 'обелиск')

