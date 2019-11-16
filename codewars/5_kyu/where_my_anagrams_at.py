# https://www.codewars.com/kata/where-my-anagrams-at/train/python/5dbcaddc4ca9970012544946


def anagrams(word, words):
    # my solution is to sort the word by characters
    # then do the same with every w in words
    # and compare those sorted strings
    list_word = list(word)
    list_word.sort()
    word_sorted = "".join(list_word)

    anagrams = []
    for w in words:
        list_w = list(w)
        list_w.sort()
        w_sorted = "".join(list_w)
        if w_sorted == word_sorted:
            anagrams.append(w)
    return anagrams
