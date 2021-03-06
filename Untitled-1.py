def anagrams(word, words):
    result=[]
    to_dict = lambda word_: {letter:word_.count(letter) for letter in word_}
    for item in words:
        if to_dict(word)==to_dict(item):
            result.append(item)
    return result

# a more compact solution, can get even more compact tho 
def anagrams(word, words):    
    to_dict = lambda word_: {letter:word_.count(letter) for letter in word_}
    result=[item for item in words if to_dict(word)==to_dict(item)]
    return result