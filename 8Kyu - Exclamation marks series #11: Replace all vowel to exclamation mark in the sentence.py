def replace_exclamation(s):
    result_string = ""
    for i in s:
        if i.lower() in ['a','e','i','o','u']:
            result_string = result_string  + '!'
        else:
            result_string = result_string + i
    return result_string
