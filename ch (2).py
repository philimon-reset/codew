def anagrams(word, words):
    # why wont u workkkkkkk
    new = []
    for item in words:
        x = list(set(item))
        for letter in x:
            if item.count(letter) == word.count(letter):
                new.append(item)
            else:
                if item in new:
                    new.pop()
                    break
                else:
                    break
    return list(set(new))

print(anagrams("abba", ["abbaa","bbaba", "bbzzaa","bbaa"]))