def find_needle(haystack):
    # your code here
    for i,ele in enumerate(haystack):
        if 'needle' == ele:
            return "found the needle at position {}".format(i)
