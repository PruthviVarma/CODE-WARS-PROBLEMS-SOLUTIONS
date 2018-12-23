def order(sentence):
    newstring = [] 
    for i in range(1,10):
        for item in sentence.split():
            if str(i) in item:
                 newstring.append(item)

    return " ".join(newstring)
