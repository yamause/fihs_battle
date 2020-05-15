# coding: utf-8
# Your code here!
# coding: utf-8
# Your code here!

import random
import logging
formatter = '%(levelname)s : location:%(lineno)s MSG__ %(message)s'
logging.basicConfig(level=logging.DEBUG,format=formatter)
logger = logging.getLogger(__name__)

class char():
    #味方初期値の設定
    def __init__(self,name,life,power,defense):
        self.status_dict = {
            "name":name,
            "life":life,
            "power":power,
            "defense":defense
            }

class enemy_char(char):
    #敵初期値の設定
    enemy_box = []
    def __init__(self,name,life,power,defense):
        super().__init__(name,life,power,defense)
        enemy_char.enemy_box.append(self)

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
                
class calc():
    def __init__(self,winner,myfish_status,enemy_status):
        self.my_p = myfish_status["power"]
        self.my_d = myfish_status["defense"]
        self.my_l = myfish_status["life"]

        self.en_p = enemy_status["power"]
        self.en_d = enemy_status["defense"]
        self.en_l = enemy_status["life"]
        
        self.winner = winner
        
        self.calc_method()

    def calc_method(self):
        
        self.CriticalCalc()
        
        myfish_power = self.my_p - self.en_d + random.randint(-5,10)
        emfish_power = self.en_p - self.my_d + random.randint(-5,10)
        myfish_power = 0 if myfish_power <= 0 else myfish_power
        emfish_power = 0 if emfish_power <= 0 else emfish_power
        
        self.my_l -= emfish_power
        self.en_l -= myfish_power
        
        return(int(self.my_l),int(self.en_l))
        
    def CriticalCalc(self):
        if self.winner == "my_fish":
            self.my_p *= 1.5
        elif self.winner == "enemy":
            self.en_p *= 1.5
        
        
class result():
    @classmethod
    def result_method(cls,my_status,en_status,pers_attr,sess_attr):
        
        if my_status["life"] <= 0:
            pers_attr["life"] = my_status["life"]
            sess_attr["battle_cont"] = False
            speak_output = ("{}との戦いに敗北しました！").format(en_status["name"])
            bools = True
            
        elif en_status["life"] <= 0:
            pers_attr["v_count"] = 1
            pers_attr["life"] = my_status["life"]
            sess_attr["battle_cont"] = False
            speak_output = ("{}との戦いに勝利しました！").format(en_status["name"])
            bools = False
            
        else :
            pers_attr["life"] = my_status["life"]
            sess_attr["my_status"] = my_status
            sess_attr["en_status"] = en_status
            sess_attr["battle_cont"] = True
            speak_output = ("次の戦闘に移ります")
            bools = False
        sess_attr["round"] += 1
        return(speak_output,pers_attr,sess_attr,bools)
#--------------------------------------------------------

def Test_code(pers_attr,sess_attr,slots_id):
    
    sess_attr["round"] = 0
    sess_attr["my_status"] = {}
    sess_attr["en_status"] = {}
    
    my = "myfish"
    
    my_fish = char(
            my,
            pers_attr["life"],
            pers_attr["power"],
            pers_attr["defence"]
                )

    enemy_1 = enemy_char("ザコテキ",100,100,100)
    enemy_2 = enemy_char("フツテキ",150,150,150)
    enemy_3 = enemy_char("ツヨテキ",200,200,200)
    
                # 敵のランダム出現
    num = random.randint(0,len(enemy_char.enemy_box) - 1)
    enemy_obj = enemy_char.enemy_box[num]
    
                
    
    # 相手と自分のコマンド入力
    my_cmd = int(slots_id)
    enemy_cmd = random.randint(0,2)
        
    winner = janken.main(my_cmd,enemy_cmd)

    
    # バトル計算
    tmp = calc(winner,my_fish.status_dict,enemy_obj.status_dict)
    my_fish.status_dict["life"] = tmp.my_l
    enemy_obj.status_dict["life"] = tmp.en_l
                    
    speak_output,pers_attr,sess_attr,bools = result.result_method(my_fish.status_dict,enemy_obj.status_dict,pers_attr,sess_attr)
    return(speak_output,pers_attr,sess_attr,bools)
    
#--------------------------------------------------------
def Test_code_second(pers_attr,sess_attr,slots_id):

    my = "myfish"
    my_fish = (
        char(
            my,
            pers_attr["life"],
            pers_attr["power"],
            pers_attr["defence"]
                )
    )
    enemy_1 = enemy_char(
        sess_attr["en_status"]["name"],
        sess_attr["en_status"]["life"],
        sess_attr["en_status"]["power"],
        sess_attr["en_status"]["defense"]
    )

    enemy_obj = enemy_char.enemy_box[0]
    
    # 相手と自分のコマンド入力
    my_cmd = int(slots_id)
    enemy_cmd = random.randint(0,2)
    winner = janken.main(my_cmd,enemy_cmd)


    # バトル計算
    tmp = calc(winner,my_fish.status_dict,enemy_obj.status_dict)
    my_fish.status_dict["life"] = tmp.my_l
    enemy_obj.status_dict["life"] = tmp.en_l
    
    speak_output,pers_attr,sess_attr,bools = result.result_method(my_fish.status_dict,enemy_obj.status_dict,pers_attr,sess_attr)
    return(speak_output,pers_attr,sess_attr,bools)

 
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
    
    speak_output,pers_attr,sess_attr,bools = Test_code(pers_attr,sess_attr,slots_id)
    logger.debug(("{}").format(speak_output))
    
    for i in range(MAX_ROUND):
        if MAX_ROUND <= sess_attr["round"] or not sess_attr["battle_cont"]:
            logger.debug(("{}").format("ブレイク"))
            speak_output
            break
        
        speak_output,pers_attr,sess_attr,bools = Test_code_second(pers_attr,sess_attr,slots_id)
        logger.debug(("{}").format(speak_output))
