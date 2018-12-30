def reverseWords(str):
    output_str = ''
    for i in reversed(str.split()):
        output_str = output_str + i + " "
    return output_str.strip(' ')
