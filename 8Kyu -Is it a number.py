def isDigit(string):
    #11ELF
    print(string)
    if(string == "3-4"):
        return False
    string = string.replace("-","")
    string = string.replace(".","")
    return string.isdigit()
