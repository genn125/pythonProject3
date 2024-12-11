
# module_3_4.py

# "Однокоренные" - использования параметров *args/ **kwargs на практике

def single_root_words(*other_words, root_word='ГРИБ', ):
    same_words = []

    for i in other_words:

        if root_word.lower() in i.lower():
            same_words.append(i)

    return print(*same_words, sep=', ')


single_root_words('грибник', 'грибной', 'гробница', 'грибочек')
single_root_words('Disablement', 'Oble', 'Mable', 'Disable', 'Bagel', root_word = 'ABL')

'''
ABL — Любительский баскетбольный чемпионат в Москве. Для всех людей. Pro Omni Populo.
Oble — деревня в административном районе гмина Ядув в Воломинском повяте Мазовецкого воеводства
на востоке центральной Польши.
'''

