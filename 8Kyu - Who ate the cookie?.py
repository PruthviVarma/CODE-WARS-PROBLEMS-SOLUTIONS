def cookie(x):
    #Good Luck
    if(isinstance(x,(str))):
        return "Who ate the last cookie? It was Zach!"
    elif(isinstance(x,(int,float)) and type(x) == int or type(x) == float):
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"
