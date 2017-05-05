import nltk

def spl():
    sentence="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    words= nltk.word_tokenize(sentence)
    print(words)
    l=len(words)
    c = []
    while l>0:
        d=(words[l-1])
        c.insert(0,d[0])
        l=l-1

    print(c)
spl()