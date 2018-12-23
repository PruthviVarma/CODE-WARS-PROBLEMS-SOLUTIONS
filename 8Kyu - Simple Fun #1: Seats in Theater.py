def seats_in_theater(tot_cols, tot_rows, col, row):
    #your code here
    if(tot_cols>=1000 or tot_rows>=1000 or col>=1000 or row>=1000):
        return 0
    else:
        m = (tot_cols-col)+1 #need to include the col your sitting because those people also get blocked view
        n = (tot_rows-row)
        return m*n
