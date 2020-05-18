# coding: utf-8
# Your code here!
# coding: utf-8
# Your code here!

import random
import logging
formatter = '%(levelname)s : location:%(lineno)s MSG__ %(message)s'
logging.basicConfig(level=logging.DEBUG,format=formatter)
logger = logging.getLogger(__name__)

class CharCreate():
    #味方初期値の設定
    def __init__(self,name,life,power,defense):
        self.status_dict = {
            "name":name,
            "life":life,
            "power":power,
            "defense":defense
            }

class EnemyCharCreate(CharCreate):
    #敵初期値の設定
    enemy_box = []
    def __init__(self,name,life,power,defense):
        super().__init__(name,life,power,defense)
        EnemyCharCreate.enemy_box.append(self)

class janken():
    @classmethod
    def main(cls,my_cmd,enemy_cmd):

        logger.debug("自分の手　" + str(my_cmd))
        logger.debug("相手の手　" + str(enemy_cmd))

        #ジャンケン処理
        if enemy_cmd == my_cmd:
            winner = "drow"
            return(winner)
        elif (
            enemy_cmd == 0 and my_cmd == 1 or 
            enemy_cmd == 1 and my_cmd == 2 or 
            enemy_cmd == 2 and my_cmd == 0
            ):
            winner = "enemy"
            return(winner)
        else :
            winner = "my_fish"
            return(winner)
                
class DmageCalc():
    def __init__(self,winner,myfish_status,enemy_status):
        self.my_p = myfish_status["power"]
        self.my_d = myfish_status["defense"]
        self.my_l = myfish_status["life"]

        self.en_p = enemy_status["power"]
        self.en_d = enemy_status["defense"]
        self.en_l = enemy_status["life"]

        self.enemyDamege = 0
        self.myfishDamege = 0        

        self.winner = winner
        
        self.calc_method()

    def calc_method(self):
        
        self.CriticalCalc()
        
        self.enemyDamege = self.my_p - self.en_d + random.randint(-5,10)
        self.myfishDamege = self.en_p - self.my_d + random.randint(-5,10)
        self.enemyDamege = 0 if self.enemyDamege <= 0 else self.enemyDamege
        self.myfishDamege = 0 if self.myfishDamege <= 0 else self.myfishDamege

        self.myfishDamege = int(self.myfishDamege)
        self.enemyDamege  = int(self.enemyDamege)
        self.my_l   -= self.myfishDamege
        self.en_l   -= self.enemyDamege
    
    def CriticalCalc(self):
        if self.winner == "my_fish":
            self.my_p *= 1.5
        elif self.winner == "enemy":
            self.en_p *= 1.5
        
        
class result():
    @classmethod
    def result_method(cls,my_status,en_status,pers_attr,sess_attr,myfishDamege,enemyDamege):
        print(sess_attr)
        battleText = ("{}に{}のダメージ！自分に{}のダメージ！").format(en_status["name"],enemyDamege,myfishDamege)
        
        if my_status["life"] <= 0:
            pers_attr["life"] = my_status["life"]
            sess_attr["battle_cont"] = False
            speak_output = ("{}との戦いに敗北しました！").format(en_status["name"],battleText)
            bools = True
            
        elif en_status["life"] <= 0:
            pers_attr["v_count"] = 1
            pers_attr["life"] = my_status["life"]
            sess_attr["battle_cont"] = False
            speak_output = ("{}との戦いに勝利しました！").format(en_status["name"],battleText)
            bools = False
            
        else :
            pers_attr["life"] = my_status["life"]
            sess_attr["my_status"] = my_status
            sess_attr["en_status"] = en_status
            sess_attr["battle_cont"] = True
            speak_output = ("{}次の戦闘に移ります").format(battleText)
            bools = False
            sess_attr["round"] += 1
            if sess_attr["round"] >= 3 :
                speak_output = ("{}決着がつかなかった。戦闘を終了します。").format(battleText)
        return(speak_output,pers_attr,sess_attr,bools)
#--------------------------------------------------------
class BattleInit:
    
    def __init__(self,pers_attr,sess_attr):
        self.pers_attr = pers_attr
        self.sess_attr = sess_attr
        
        sess_attr["round"] = 0
        sess_attr["my_status"] = {}
        sess_attr["en_status"] = {}
        
        my = "myfish"
        
        self.my_fish = CharCreate(
                my,
                pers_attr["life"],
                pers_attr["power"],
                pers_attr["defence"]
                    )
    
        enemy_1 = EnemyCharCreate("ザコテキ",100,100,100)
        enemy_2 = EnemyCharCreate("フツテキ",150,150,150)
        enemy_3 = EnemyCharCreate("ツヨテキ",200,200,200)
        
                    # 敵のランダム出現
        num = random.randint(0,len(EnemyCharCreate.enemy_box) - 1)
        self.enemy_obj = EnemyCharCreate.enemy_box[num]
        
    def battleFunc(self,slots_id):
        # 相手と自分のコマンド入力
        my_cmd = int(slots_id)
        enemy_cmd = random.randint(0,2)
        
        winner = janken.main(my_cmd,enemy_cmd)
        # バトル計算
        tmp = DmageCalc(winner,self.my_fish.status_dict,self.enemy_obj.status_dict)
        self.my_fish.status_dict["life"] = tmp.my_l
        self.enemy_obj.status_dict["life"] = tmp.en_l
                    
        return(result.result_method(self.my_fish.status_dict,self.enemy_obj.status_dict,self.pers_attr,self.sess_attr,tmp.myfishDamege,tmp.enemyDamege))
    
#--------------------------------------------------------
class BattleSecond(BattleInit):
    def __init__(self,pers_attr,sess_attr):
        self.pers_attr = pers_attr
        self.sess_attr = sess_attr
    
        my = "myfish"
        self.my_fish = (
            CharCreate(
                my,
                pers_attr["life"],
                pers_attr["power"],
                pers_attr["defence"]
                    )
        )
        self.enemy_1 = EnemyCharCreate(
            sess_attr["en_status"]["name"],
            sess_attr["en_status"]["life"],
            sess_attr["en_status"]["power"],
            sess_attr["en_status"]["defense"]
        )

        self.enemy_obj = EnemyCharCreate.enemy_box[0]

#--------------------------------------------------------

if __name__ == "__main__":
    # Persistent Attributes を変数に代入
    pers_attr = {"life":100,"power":100,"defence":100,"v_count":1}
    # Session Attributes を変数に代入
    sess_attr = {}
    # スロット値の取得
    slots_id = 0
    # バトル回数の指定
    MAX_ROUND = 3
    
    battle_init     = BattleInit(pers_attr,sess_attr)
    
    
    speak_output,pers_attr,sess_attr,bools = battle_init.battleFunc(slots_id)
    
    logger.debug(("{}").format(speak_output))
    
    for i in range(MAX_ROUND):
        if MAX_ROUND <= sess_attr["round"] or not sess_attr["battle_cont"]:
            logger.debug(("{}").format("ブレイク"))
            break
        battle_second   = BattleSecond(pers_attr,sess_attr)
        speak_output,pers_attr,sess_attr,bools = battle_second.battleFunc(slots_id)
        logger.debug(("{}").format(speak_output))
