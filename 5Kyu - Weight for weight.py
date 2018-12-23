def order_weight(strng):
    # your code
    calculated_weight = 0
    calculated_newlist = []
    calculated_newlist1 = []
    pairing_weight_weights = {}
    sorted_list = []
    final_string = ""
    splitted_string = strng.split()
    splitted_string = sorted(splitted_string)
    length = len(splitted_string)
    changed_string = ""
    pos = 0
    split_string = ""
    #split the string using split function
    for weights in strng.split():
        if(int(weights)>0 or weights != " " or weights != ""):
    #Take each weight and accumulate each digit
            calculated_weight = 0
            for weight in weights:
            # do type casting for the weight as it as string.
                calculated_weight = calculated_weight + int(weight)
                
            changed_string = str(calculated_weight) + ":" + weights + " "+ changed_string   
            calculated_newlist1.append(changed_string)
            calculated_newlist.append(calculated_weight)
            pairing_weight_weights[weights] = calculated_weight
      
    sorted_list = sorted(calculated_newlist)
    split_string = changed_string.split()
    #print(sorted_list)
    #print(changed_string)
    #print(pairing_weight_weights)
    for items in sorted_list:
        for item in splitted_string:
            d = pairing_weight_weights[item]
            if (items==d): 
                for ite in split_string:
                    pos=ite.find(':')
                    if(ite[pos+1:]==item):
                        final_string = final_string + " " + item
                        split_string.remove(ite)
                        break
        
    return final_string.lstrip()
