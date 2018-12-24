import re
def to_alternating_case(string):
    #your code here
    x = ''
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
    for i in string:
        if i.isupper():
            x = x + i.lower()
        elif i.islower():
            x = x + i.upper()
        elif i.isdigit():
            x = x + i
        elif i.isspace():
            x = x + i
        elif i in ['.','<','=','>','!',':',';','?','/',',']:
            x = x + i
    return x
