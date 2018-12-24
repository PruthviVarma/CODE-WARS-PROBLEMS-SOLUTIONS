def how_much_i_love_you(nb_petals):
    # your code
    n = nb_petals
    if (n % 6 == 1):
        return "I love you"
    elif (n% 6 ==  2):
        return "a little"    
    elif (n% 6 ==  3):
        return "a lot"
    elif (n% 6 ==  4):
        return "passionately"
    elif (n% 6 ==  5):
        return "madly"
    else:
        return "not at all"
