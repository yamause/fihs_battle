import random
import logging
formatter = '%(levelname)s : location:%(pathname)s(%(lineno)s) MSG__ %(message)s'
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

        cls.enemy_cmd = enemy_cmd
        cls.my_cmd = my_cmd

        logger.debug("自分の手　" + str(cls.my_cmd))
        logger.debug("相手の手　" + str(cls.enemy_cmd))

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
                
class calc():
    @classmethod
    def calc_method(cls,winner,myfish_status,enemy_status):
        my_name,my_p,my_d,my_l = [i for i in myfish_status.values()]
        en_name,en_p,en_d,en_l = [i for i in myfish_status.values()]

        if winner == "my_fish":
            my_p *= 1.5
        elif winner == "enemy":
            en_p *= 1.5
        logger.debug(("{}:{}").format(my_p,winner))
        logger.debug(en_p)
        myfish_power = my_p - en_d + random.randint(-5,10)
        emfish_power = en_p - my_d + random.randint(-5,10)
        myfish_power = 0 if myfish_power <= 0 else myfish_power
        emfish_power = 0 if emfish_power <= 0 else emfish_power
        
        my_l -= emfish_power
        en_l -= myfish_power
        
        logger.debug(("{}:{}").format(emfish_power,myfish_power))
        logger.debug(("{}:{}").format(my_l,en_l))
        return(int(my_l),int(en_l))

#--------------------------------------------------------

def Test_code(pers_attr,sess_attr,slots_id):
    if not sess_attr:
    
        sess_attr["round"] = 0
        sess_attr["my_status"] = {}
        sess_attr["en_status"] = {}
        my = "myfish"
        my_fish = (
            char(
                my,
                pers_attr["life"],
                pers_attr["power"],
                pers_attr["defence"]
                    )
        )
        enemy_1 = enemy_char("ザコテキ",100,100,100),
        enemy_2 = enemy_char("フツテキ",150,150,150),
        enemy_3 = enemy_char("ツヨテキ",200,200,200)
    
                # 敵のランダム出現
        num = random.randint(0,len(enemy_char.enemy_box) - 1)
        enemy_obj = enemy_char.enemy_box[num]
    
                
    
        # 相手と自分のコマンド入力
        my_cmd = int(slots_id)
        enemy_cmd = random.randint(0,2)
        
        winner = janken.main(my_cmd,enemy_cmd)
        logger.debug(winner)
    
        # バトル計算
        my_fish.status_dict["life"],enemy_obj.status_dict["life"] = calc.calc_method(
                        winner,
                        my_fish.status_dict,
                        enemy_obj.status_dict,
                        )
        logger.debug(("{}").format(my_fish.status_dict))
        logger.debug(("{}").format(enemy_obj.status_dict))

        if my_fish.status_dict["life"] <= 0:
            speak_output = ("{}との戦いに敗北しました！").format(enemy_obj.name)
            bools = True
    
        elif enemy_obj.status_dict["life"] <= 0:
            pers_attr["v_count"] += 1
            speak_output = ("{}との戦いに勝利しました！").format(enemy_obj.name)
            bools = False
            
        else :
            sess_attr["round"] += 1
            sess_attr["my_status"] = my_fish.status_dict
            sess_attr["en_status"] = enemy_obj.status_dict
            speak_output = ("次の戦闘に移ります")
            bools = True
    
       
        speak_output += ("自分のライフ:{},相手のライフ:{}".format(my_fish.status_dict["life"],enemy_obj.status_dict["life"]))
        return(speak_output)
    

#--------------------------------------------------------

# Persistent Attributes を変数に代入
pers_attr = {"life":100,"power":100,"defence":100}
# Session Attributes を変数に代入
sess_attr = {}
# スロット値の取得
slots_id = 0

logger.debug(("{}").format(Test_code(pers_attr,sess_attr,slots_id)))