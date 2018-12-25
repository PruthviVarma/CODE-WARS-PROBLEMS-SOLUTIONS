def remove_duplicate(arr):
    new = []
    for el in arr:
        if not el in new:
            new.append(el)
    return new
