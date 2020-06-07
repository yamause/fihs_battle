import logging
import random

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core import utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 必要な処理
# 指定エリアの取得
# 出現敵の決定
class BattleIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        
        return ask_utils.is_intent_name("BattleIntent")(handler_input)
    
    def handle(self, handler_input):

        pers_attr = handler_input.attributes_manager.persistent_attributes
        sess_attr = handler_input.attributes_manager.session_attributes



        # エリア情報の取得
        with open("mylib/area.json") as param:
            get_area = json.load(param)

        set_area_id = pers_attr["set_area"]
        set_area_name = get_area[set_area_id]["area_name"]


        # 敵のランダム出現
        with open("mylib/area.json") as param:
            get_enemy = json.load(param)

        set_area_enemy = get_area[set_area_id]["pop_enemy"]
        pop_enemy_id = random.choice(list(set_area_enemy.values()))
        pop_enemy_name = get_enemy[pop_enemy_id]["enemy_name"]

        sess_attr["gameMode"] = "janken" 
        sess_attr["round"] = 0
        sess_attr["enemy"] = pop_enemy_id

        speak_output = (f"{set_area_name}で{pop_enemy_name}が現れた！戦闘を開始します、グー、チョキ、パーから一つ選んでください。")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .set_should_end_session(False)
            .response
            )