def product(numbers):
    # Implement me! :)
    # sure darling ;-)
    result = 1
    #checking whether list of numbers are NONE or EMPTY
    if(numbers==None or numbers==[]):
        return None
    else:
    #looping through the numbers.
        for num in numbers:
            result = result * num
      
    return result
    
    
