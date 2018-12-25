def split_and_merge(string, sp):
    if(sp!=""):
        li = string.split(" ")
        x = ''
        for i in li:
            i = sp.join(i)
            x = x + ' ' + i
    return x.strip(" ")
