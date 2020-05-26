import status
import pickle

class charCreate:
    def __init__(self):
        self.life = status.BaseStatus(300,300)
        self.power = status.BaseStatus(100,100)
        self.defence = status.BaseStatus(100,100)

if __name__ == "__main__":
    
    max_life=100,
    life=100,
    max_pawer=100,
    power=100,
    max_defence=100,
    defence=100,
   
    pers_attr = {
        "my_status":[
            max_life,
            life,
            max_pawer,
            power,
            max_defence,
            defence,
        ]
    }
    charcter = charCreate()  
    print(charcter.life.var_param)

    with open('class.pickle',mode='wb') as f:
        pickle.dump(charcter, f)

        

