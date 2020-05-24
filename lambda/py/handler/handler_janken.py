import logging
import random

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core import utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class JankenIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        # Session Attributes を変数に代入
        sess_attr = handler_input.attributes_manager.session_attributes
        gameStartBools = sess_attr["gameMode"] == "janken"

        return gameStartBools

    def handle(self, handler_input):
                
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

                battleText = ("{}に{}のダメージ！自分に{}のダメージ！").format(en_status["name"],enemyDamege,myfishDamege)

                if my_status["life"] <= 0:
                    pers_attr["life"] = my_status["life"]
                    sess_attr["battle_cont"] = False
                    speak_output = ("{}{}との戦いに敗北しました！").format(battleText,en_status["name"])
                    bools = True

                elif en_status["life"] <= 0:
                    pers_attr["v_count"] += 1
                    pers_attr["life"] = my_status["life"]
                    sess_attr["battle_cont"] = False
                    speak_output = ("{}{}との戦いに勝利しました！").format(battleText,en_status["name"])
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
                        sess_attr["gamaMode"] = "normal"
                return(speak_output,pers_attr,sess_attr,bools)
#--------------------------------------------------------
        class BattleInit:
            @classmethod
            def battleFunc(cls,slots_id,my_status,en_status):
                # 相手と自分のコマンド入力
                my_cmd = int(slots_id)
                enemy_cmd = random.randint(0,2)
                winner = janken.main(my_cmd,enemy_cmd)
                # バトル計算
                tmp = DmageCalc(winner,my_status,en_status)
                my_status["life"] = tmp.my_l
                en_status["life"] = tmp.en_l

                return(
                    result.result_method(
                        my_status,
                        en_status,
                        pers_attr,
                        sess_attr,
                        tmp.myfishDamege,
                        tmp.enemyDamege
                    )
                )
                
        #-------------------------------------------------------


        # Persistent Attributes を変数に代入
        pers_attr = handler_input.attributes_manager.persistent_attributes
        # Session Attributes を変数に代入
        sess_attr = handler_input.attributes_manager.session_attributes
        # スロット値の取得
        slots = handler_input.request_envelope.request.intent.slots
        slots_id = slots["command"].resolutions.resolutions_per_authority[0].values[0].value.id
        print(slots_id)
        # バトル回数の指定
        MAX_ROUND = 3

        (speak_output,
        pers_attr,
        sess_attr,
        bools) = BattleInit.battleFunc(slots_id,sess_attr["my_status"],sess_attr["en_status"])
        
        handler_input.attributes_manager.persistent_attributes = pers_attr
        handler_input.attributes_manager.save_persistent_attributes()

        return(
                handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(bools)
                .response
                )