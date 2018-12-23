class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

def declare_winner(fighter1, fighter2, first_attacker):
    x = ""
    y = ''
    
    if(first_attacker == fighter1.name):
        x = first_attacker
    elif(first_attacker == fighter2.name):
        y = first_attacker
    else:
        return " "
    
    #Fighter1 is the first attacker
    if(x!=" " and x!=""):
    
        while True:
            fighter2.health = fighter2.health - fighter1.damage_per_attack
            if(fighter2.health<=0):
                return fighter1.name
                break
            fighter1.health = fighter1.health - fighter2.damage_per_attack
            if(fighter1.health<=0):
                return fighter2.name
                break
                
    #Fighter2 is the first attacker            
    elif(y!=" " and y!=""):
    
         while True:
            fighter1.health = fighter1.health - fighter2.damage_per_attack
            if(fighter1.health<=0):
                return fighter2.name
                break
            fighter2.health = fighter2.health - fighter1.damage_per_attack
            if(fighter2.health<=0):
                return fighter1.name
                break
    else:
        return "zero"
