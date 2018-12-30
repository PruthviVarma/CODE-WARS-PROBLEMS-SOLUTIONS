def define_suit(card):
    # Good luck
    if(card.endswith('C')):
        return 'clubs'
    elif(card.endswith('S')):
        return 'spades'
    elif(card.endswith('D')):
        return 'diamonds'
    else:
        return 'hearts'
