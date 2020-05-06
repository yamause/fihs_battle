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
        attr = handler_input.attributes_manager.persistent_attributes
        
        #初期値の設定
        class char():
            def __init__(self,name,life,power,defence):
                self.name = name
                self.life = life
                self.power = power
                self.defence = defense

        my_fish = char(my,attr["life"],attr["power"],attr["defence"])
        
        enemy_fish_1 = char("ザコテキ",100,100,100)
        enemy_fish_2 = char("フツテキ",150,150,150)
        enemy_fish_3 = char("ツヨテキ",200,200,200)

        enemy_box[
            enemy_fish_1
            enemy_fish_2
            enemy_fish_3
        ]
        enemy_box[0].life

        
        myfish_power = my_fish.power - enemy_box[num].defense + int(random.randint(-5,10))
        emfish_power = enemy_box[num].power - my_fish.defense + int(random.randint(-5,10))

        #コマンド選択




        #割合の計算
        mdown = my_hp_after / my_fish.life
        edown = enemy_hp_after / enemy_box[num].life

        #比較
        if mdown > edown:
            speak_output = ("おまえの負け")
            attr["v_count"] += 1
            attr["life"] -= emfish_power

        elif mdown < edown:
            speak_output = ("おまえの勝ち")
            attr["life"] -= emfish_power
        else:
            speak_output = ("おまえら強さ同じ")

        # 生死判定
        if attr["life"] <= 0 :
            handler_input.attributes_manager.delete_persistent_attributes()
            bools = True
            speak_output = ("あなたのフィッシュのライフが0になり、死んでしまいました。また初めから遊んでください。")
        else:
            handler_input.attributes_manager.persistent_attributes = attr
            handler_input.attributes_manager.save_persistent_attributes()

        return (
            handler_input.response_builder
            .speak(speak_output)
            .set_should_end_session(False)
            .response
        )