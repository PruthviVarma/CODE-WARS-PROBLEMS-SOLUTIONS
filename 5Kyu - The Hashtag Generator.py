def generate_hashtag(s):
    if(s=="" or len(s)>140):
        return False
    else:
        s = s.title() #To capitalize the title of the first letters
        s = s.strip() #To strip trailing and ending spaces
        s = s.replace(" ","") #To replace the blank with null characters
        s = '#' + s #Append #(hash tag)
        return s
