def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    # your code
    
    new_price = 0
    months = 1
    percent_increased = 0.5
    percent_loss_new = 0
    percent_loss_old = 0
    
    #Difference b/w startPriceOld and startPriceNew
    diff = startPriceNew - startPriceOld
    
    if(diff == 0):
        return [0,0]     
    elif(startPriceOld>startPriceNew):
        return [0,startPriceOld - startPriceNew]
    else:
        while(new_price<=startPriceNew):
            #New Price
            percent_loss_new = (startPriceNew * (percentLossByMonth/100))
            startPriceNew = startPriceNew - percent_loss_new 
            
            #Old Price
            percent_loss_old = (startPriceOld * (percentLossByMonth/100))
            startPriceOld = startPriceOld - percent_loss_old
            
            new_price = savingperMonth*months + startPriceOld
            
            months = months + 1
            
            if(months%2==0):
                percentLossByMonth = percentLossByMonth + percent_increased
                
            
            
        return [months-1,round(new_price-startPriceNew)]
