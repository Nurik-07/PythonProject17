def single_root_words (root_word, *other_words):
    same_words = []
    i = root_word.lower()
    for j in other_words:
        l = j.lower()
        if i in l or l in i: #лень было придумывать название
            same_words.append(j)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)