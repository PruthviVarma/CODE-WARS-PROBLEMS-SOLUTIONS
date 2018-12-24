def bonus_time(salary, bonus):
    #your code here
    if(bonus):
        salary = salary*10
        salary = str(salary)
        return salary.rjust(len(salary)+1,'$')
    else:
        salary = str(salary)
        return salary.rjust(len(str(salary))+1,'$')
