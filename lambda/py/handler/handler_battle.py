import logging
import random

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core import utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class BattleIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BattleIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        pers_attr = handler_input.attributes_manager.persistent_attributes
        sess_attr = handler_input.attributes_manager.session_attributes
        sess_attr["round"] = 0

        #クラス
        class char():
            #味方初期値の設定
            def __init__(self,name,life,power,defense):
                self.name = name
                self.life = life
                self.power = power
                self.defense = defense


        class enemy_char(char):
            #敵初期値の設定
            enemy_box = []
            def __init__(self,name,life,power,defense):
                self().__init__(name,life,powerf,defense):
                char.enemy_box.append(self)

        class battle():
            #バトルの処理
            @classmethod
            def battle(cls,enemy,my_cmd):
                
                # グー      ０ 
                # チョキ    １ 
                # パー      ２

                #相手のジャンケンコマンド
                cls.enemy_cmd = random.randint(0,2)
                print(cls.enemy_cmd)

                #ジャンケン処理
                if cls.enemy_cmd == cls.my_cmd:
                    winner = "aiko"
                    print(winner)
                elif (
                    cls.enemy_cmd == 0 and cls.my_cmd == 1 or 
                    cls.enemy_cmd == 1 and cls.my_cmd == 2 or 
                    cls.enemy_cmd == 2 and cls.my_cmd == 0:
                    )
                    cls.winner = "enemy"
                    print(cls.winner)
                else :
                    cls.winner = "my_fish"
                    print(cls.winner)
                
                myfish_power = my_fish.power - enemy.defense + int(random.randint(-5,10))
                emfish_power = enemy.power - my_fish.defense + int(random.randint(-5,10))
                myfish_power = 0 if myfish_power <= 0 else myfish_power
                emfish_power = 0 if emfish_power <= 0 else emfish_power
        
                my_fish.life -= emfish_power
                self.life -= myfish_power
                print("--------------------------------------------")
                print("●"+my_fish.name+ "に" + str(emfish_power) + "のダメージ!残りは"+str(my_fish.life)+"！")
                print("●"+self.name + "に" + str(myfish_power) + "のダメージ!残りは"+str(self.life)+"！")
                print("--------------------------------------------")


        class battle_2(battle):


        if sess_attr["round"] == 0:
            my_fish = char(my,pers_attr["life"],pers.attr["power"],pers.attr["defence"])
            
            enemy_fish_1 = char("ザコテキ",100,100,100),
            enemy_fish_2 = char("フツテキ",150,150,150),
            enemy_fish_3 = char("ツヨテキ",200,200,200)

            # 敵のランダム出現
            num = random.randint(0,len(char.enemy_box) - 1)
            char.enemy_box[num].name

            #ラウンド分岐
            char.enemy_box[num].battle()

        elif sess_attr["round"] == 1 :
            my_fish = char(my,pers_attr["life"],pers.attr["power"],pers.attr["defence"])
            #teki
            char.enemy_box[num].battle_2()

        elif sess_attr["round"] == 2 :
            my_fish = char(my,pers_attr["life"],pers.attr["power"],pers.attr["defence"])
            #teki
            char.enemy_box[num].battle_2()
            char.enemy_box[num].finish()





        #コマンド選択




        #割合の計算
        mdown = my_hp_after / my_fish.life
        edown = enemy_hp_after / enemy_box[num].life

        #比較
        if mdown > edown:
            speak_output = ("おまえの負け")
            pers_attr["v_count"] += 1
            pers_attr["life"] -= emfish_power

        elif mdown < edown:
            speak_output = ("おまえの勝ち")
            pers_attr["life"] -= emfish_power
        else:
            speak_output = ("おまえら強さ同じ")

        # 生死判定
        if attr["life"] <= 0 :
            handler_input.attributes_manager.delete_persistent_attributes()
            bools = True
            speak_output = ("あなたのフィッシュのライフが0になり、死んでしまいました。また初めから遊んでください。")
        else:
            handler_input.attributes_manager.persistent_attributes = pers_attr
            handler_input.attributes_manager.save_persistent_attributes()

        return (
            handler_input.response_builder
            .speak(speak_output)
            .set_should_end_session(False)
            .response
        )