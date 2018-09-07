#!/usr/bin/env python3

# Q1
########################


def file_facts(filenm):
    """ Takes a file as input and tells you
    how many lines, words, and non whitespace
    characters are in the file """

    lines = 0
    words = 0
    chars = 0
    with open(filenm) as f:
        for line in f:
            wordlist = line.split()
            lines += 1
            words += len(wordlist)
            chars += sum(len(word) for word in wordlist)
    return (lines, words, chars)


print(file_facts("a6.txt"))
########################

# Q2
########################


def merge_lists(*lists):
    """ Input is an arbitrary number of lists. Output is
    merged list of unique elements """

    merged = []
    [merged.append(x) for i in lists for x in i if x not in merged]
    return merged


print(merge_lists(["this", "a", "list", "one"], ["this", "is", "list", "two"]))
########################

# Q3
########################
nums = (1, 20, 300, 400)
constant = 8

print(list(map(lambda x: x + constant, nums)))
print([x + constant for x in nums])
########################

# Q4
########################
wl1 = ["double", "triple", "int", "quadruple"]
wl2 = ["double", "home run"]
wl3 = ["int", "double", "float"]


def wordlists(*wl):
    """ Input is arbitrary number of lists of strings.
    Output is one dictionary where each string is a key
    and the count of those strings is the value """

    word_dict = {}
    for i in wl:
        for x in i:
            if x in word_dict:
                word_dict[x] += 1
            else:
                word_dict[x] = 1
    return word_dict


print(wordlists(wl1, wl2, wl3))
########################

# Q5
########################
dict1 = {"a": "apple", "b": "banana", "c": "cherry"}
dict2 = {"d": "dragonfruit", "e": "elderberry", "a": "apricot"}
dict3 = {"d": "date", "b": "blueberry", "f": "fig"}


def merge_dicts(*dicts):
    """ Input is an arbitrary amount of dictionaries.
    Output is a merged dictionary where the keys are the
    keys from all the input dicts, and the values are a
    list of all the values each key holds """

    new_dict = {}
    for i in dicts:
        for (k, v) in i.items():
            if k in new_dict:
                new_dict[k].append(v)
            else:
                new_dict[k] = [v]
    return new_dict


print(merge_dicts(dict1, dict2, dict3))
