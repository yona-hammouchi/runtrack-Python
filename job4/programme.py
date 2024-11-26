def listAlphabet():
    return list(map(chr, range(97, 123)))

reversed_word_as_list = list(reversed(list(map(chr, range(97, 123)))))
print(reversed_word_as_list)