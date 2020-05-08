#------------------------------------------------
import random

class battle():
    #バトルの処理
    @classmethod
    def battle(cls,my_cmd):
        
        # グー      ０ 
        # チョキ    １ 
        # パー      ２
        #相手のジャンケンコマンド
        
        cls.enemy_cmd = random.randint(0,2)
        cls.my_cmd = my_cmd
        
        print("自分の手　" + str(cls.my_cmd))
        print("相手の手　" + str(cls.enemy_cmd))
        
        #ジャンケン処理
        if cls.enemy_cmd == cls.my_cmd:
            cls.winner = "drow"
            return(cls.winner)
        elif (
            cls.enemy_cmd == 0 and cls.my_cmd == 1 or 
            cls.enemy_cmd == 1 and cls.my_cmd == 2 or 
            cls.enemy_cmd == 2 and cls.my_cmd == 0
            ):
            cls.winner = "enemy"
            return(cls.winner)
        else :
            cls.winner = "my_fish"
            return(cls.winner)

for i in range(10):
    print ("勝者は　" + battle.battle(2))
    print( "-------------------------")
    #------------------------------------------------