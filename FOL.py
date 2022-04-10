 
class President: 
    def __init__(self, name, president, strong_vision, country_future, goals): 
        self.name = name 
        self.president = president 
        self.strong_vision = strong_vision 
        self.country_future = country_future 
        self.goals = goals 
def check_if_vision(object):
    if(object.president==True and object.strong_vision=="good" and object.country_future=="good"): 
        print(f"{object.name} is a President \n") 
        return True 
    else: 
        print(f"{object.name} is not a President \n") 
        return False 

def check_if_best_president(object): 
    if(check_if_best_president(object)): 
        if(object.goals=="good" and object.strong_vision=="yes"): 
            print(f"----> {object.name} is the best President \n") 
        else: 
            print(f"{object.name} is not the best President \n") 


Abdul_Kalam = President('Abdul_Kalam',True, 'good','good','good','yes') 
Ramnath_Kovind = President('Ramnath Kovind', True, 'good','good','bad','no') 
Narendra_Modi = President('Narendra Modi', True, 'bad', 'good', 'bad','yes') 
Amit_Shah =President('Amit Shah',False,'good','good','good','no') 

check_list = [Abdul_Kalam, Ramnath_Kovind, Narendra_Modi, Amit_Shah]

for i in check_list: 
    check_if_best_president(i) 


