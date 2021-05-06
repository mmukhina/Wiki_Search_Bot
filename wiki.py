import wikipedia
wikipedia.set_lang("ru")


def search_wiki(word):
    print(word)
    if len(word.split()) > 1:
        word = "_".join(word.split())

    w = wikipedia.search(word)
    if w == []:
        return w
        
    else:
        w2 = wikipedia.page(word).url
        w1 = wikipedia.summary(word)
        return w1, "\nСсылка: " + w2
        
