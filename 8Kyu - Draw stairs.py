def draw_stairs(n):
    # do something
    stairs = '''I'''
    i = 1
    new_line = '\n'
    under_score = ' '
    result = ''
    while i<n:
        result = result + stairs + new_line
        result = result + under_score*i
        i = i + 1
    return result + stairs
        
        
