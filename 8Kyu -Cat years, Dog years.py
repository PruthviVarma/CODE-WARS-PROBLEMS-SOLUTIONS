def human_years_cat_years_dog_years(human_years):
    if(human_years == 1):
        return [1,15,15]
    elif(human_years == 2):
        return [2,24,24]
    else:
        new = []
        new.append(human_years)
        cat_years = 24 + (human_years - 2)*4
        new.append(cat_years)
        dog_years = 24 + (human_years - 2)*5
        new.append(dog_years)
        return new
