def digitize(n):
    new = []
    for i in reversed(str(n)):
        new.append(int(i))
    return new
