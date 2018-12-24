def fake_bin(x):
    pass
    result = ''
    for i in x:
        if(int(i)<5):
            result = result + '0'
        elif(int(i)>=5):
            result = result + '1'
    return result
