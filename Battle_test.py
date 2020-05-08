# coding: utf-8
# Your code here!
import random
class char():
    enemy_box = []
    def __init__(self,name,life,power,defense):
        char.enemy_box.append(self)
        self.name = name
        self.life = life
        self.power = power
        self.defense = defense
        
    def battle(self):
        myfish_power = my_fish.power - self.defense + int(random.randint(-5,10))
        emfish_power = self.power - my_fish.defense + int(random.randint(-5,10))
        myfish_power = 0 if myfish_power <= 0 else myfish_power
        emfish_power = 0 if emfish_power <= 0 else emfish_power
        
        my_fish.life -= emfish_power
        self.life -= myfish_power
        print("--------------------------------------------")
        print("●"+my_fish.name+ "に" + str(emfish_power) + "のダメージ!残りは"+str(my_fish.life)+"！")
        print("●"+self.name + "に" + str(myfish_power) + "のダメージ!残りは"+str(self.life)+"！")
        print("--------------------------------------------")
        
class char_1():
    def __init__(self,name,life,power,defense):
        self.name = name
        self.life = life
        self.power = power
        self.defense = defense

#my_fish = char(my,attr["life"],attr["power"],attr["defence"])
my_fish = char_1("ミカタ",100,100,100)

enemy_fish_1 = char("ザコテキ",100,100,100)
enemy_fish_2 = char("フツテキ",150,150,150)
enemy_fish_3 = char("ツヨテキ",200,200,200)

for i in range(10):
    num = random.randint(0,len(char.enemy_box) - 1)
    char.enemy_box[num].battle()

def janken()
    import random
    rand = random.randint(0,2)
    print(rand)
    cmd = 1
    if rand == cmd:
        print("aiko")
    elif rand == 0 and cmd == 1 or rand == 1 and cmd == 2 or rand == 2 and cmd == 0:
        print("Lose")
    else :
        print("Win")
