def who_is_paying(name):
    #your code here
    if(name==[]):
        return ['']
    elif(len(name) == 0 or len(name) == 1 or len(name)==2):
        return [name]
    else:
        return [name,name[0:2]]
