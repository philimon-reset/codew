# a more compact solution, can get even more compact tho
def anagrams(word, words):
    def to_dict(word_): return {letter: word_.count(letter)
                                for letter in word_}
    result = [item for item in words if to_dict(word) == to_dict(item)]
    return result
