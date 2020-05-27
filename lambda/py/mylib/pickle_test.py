import pickle

class charCreate:
    def __init__(self):
        self.life = status.BaseStatus(100,100)
        self.power = status.BaseStatus(100,100)
        self.defence = status.BaseStatus(100,100)

with open('class.pickle', mode='rb') as f:
    charcter = pickle.load(f)

print(charcter.life.var_param.param_up)
    