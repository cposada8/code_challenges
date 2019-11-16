# https://www.codewars.com/kata/most-frequently-used-words-in-a-text/train/python/5dd04ee849a419002d189cb5

import re


def top_3_words(text):

    word_list = re.findall("[a-z']*[a-z]+[a-z']*", text.lower())

    word_count = {}
    for word in word_list:
        if word not in word_count:
            word_count[word] = word_list.count(word)

    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    output = [x[0] for x in sorted_words[:3]]
    return output
