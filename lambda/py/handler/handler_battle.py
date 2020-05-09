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

        class janken():
            @classmethod
            def main(cls,my_cmd,enemy_cmd):

                # グー      ０ 
                # チョキ    １ 
                # パー      ２
                #相手のジャンケンコマンド

                cls.enemy_cmd = enemy_cmd
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
                
        class calc():
            @classmethod
            def calc_method(cls,winner,my_p,my_d,my_l,en_p,en_d,en_l):
                if winner == my_fish:
                    my_p *= 1.5
                elif winner == enemy:
                    en_p *= 1.5

                myfish_power = my_p - en_d + random.randint(-5,10)
                emfish_power = en_p - my_d + random.randint(-5,10)
                myfish_power = 0 if my_p <= 0 else my_p
                emfish_power = 0 if en_p <= 0 else en_p
        
                my_l -= emfish_power
                en_l -= myfish_power

                return(my_l,en_l)

#--------------------------------------------------------

        pers_attr = handler_input.attributes_manager.persistent_attributes
        sess_attr = handler_input.attributes_manager.session_attributes

        # スロット値の取得
        slots = handler_input.request_envelope.request.intent.slots
        slots_id = slots["janken_slot"].resolutions.resolutions_per_authority[0].values[0].value.id

        if not sess_attr["round"]:

            sess_attr["round"] = 0
            sess_attr["my_status"] = {}
            sess_attr["en_status"] = {}

            my_fish = (
                char(
                    my,
                    pers_attr["life"],
                    pers.attr["power"],
                    pers.attr["defence"]
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

            # バトル計算
            my_l,en_l = calc.calc_method(
                            winner,
                            my_fish.life,
                            my_fish.power,
                            my_fish.defense,
                            enemy_obj.life,
                            enemy_obj.power,
                            enemy_obj.defense
                            )

            if my_l <= 0:
                handler_input.attributes_manager.delete_persistent_attributes()
                speak_output = ("あなたのフィッシュのライフが0になり、死んでしまいました。また初めから遊んでください。")
                bools = True

            elif en_l <= 0:
                pers_attr["v_count"] += 1
                speak_output = ("{}との戦いに勝利しました！").format(enemy_obj.name)
                bools = False

            sess_attr["round"] += 1
            sess_attr["my_status"] = my_l
            sess_attr["en_status"] = enemy_obj.life,enemy_obj.power,enemy_obj.defense
            speak_output = ("")
            bools = True




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
            .set_should_end_session(bools)
            .response
        )