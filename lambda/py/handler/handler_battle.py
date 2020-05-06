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
        
        #マイフィッシュの攻撃力、防御力を代入
        my_hp = attr["life"]
        my_power = attr["power"]
        my_defense = attr["defense"]
        
        #敵フィッシュの攻撃力、防御力を代入
        enemy_hp = my_hp + int(random.uniform(-10,20))
        enemy_power = my_power + int(random.uniform(-10,20))
        enemy_defense = my_defense + int(random.uniform(-10,20))

        #防御力を加味した攻撃力の計算
        myfish_power = my_power - enemy_defense + int(random.uniform(-5,10))
        emfish_power = enemy_power - my_defense + int(random.uniform(-5,10))

        #HPを減算
        my_hp_after = my_hp - emfish_power
        enemy_hp_after = enemy_hp - myfish_power

        #割合の計算
        mdown = 1 - my_hp_after / my_hp
        edown = 1 - enemy_hp_after / enemy_hp

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

        handler_input.attributes_manager.persistent_attributes = attr
        handler_input.attributes_manager.save_persistent_attributes()

        return (
            handler_input.response_builder
            .speak(speak_output)
            .set_should_end_session(False)
            .response
        )