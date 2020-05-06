import logging
import random
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core import utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class TrainingIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TrainingIntent")(handler_input)

    def handle(self, handler_input):
        bools = False
        attr = handler_input.attributes_manager.persistent_attributes

        #スロット値代入
        slots = handler_input.request_envelope.request.intent.slots
        menu = slots["menu"].resolutions.resolutions_per_authority[0].values[0].value.id

        # ステータスの上昇ちの計算
        status_add = int(random.uniform(0,10))
        attr["life"] -= 10
        print(attr["life"])
        #パワーを上げる
        if menu == "power" :
            attr["power"] += status_add
            status = attr["power"]
            comment = "パワー"

        #ディフェンスを上げる
        elif menu == "defense" :
            attr["defense"] += status_add
            status = attr["defense"]
            comment = "ディフェンス"

        #ライフを上げる
        elif menu == "life" :
            attr["max_life"] += status_add
            status = attr["max_life"]
            comment = "ライフの最大値"



        if attr["life"] <= 0 :
            handler_input.attributes_manager.delete_persistent_attributes()
            bools = True
            speak_output = ("あなたのフィッシュのライフが0になり、死んでしまいました。また初めから遊んでください。")
        else:
            speak_output = ("{}が{}上がったよ。現在の{}は{}です").format(comment,status_add,comment,status)
            handler_input.attributes_manager.persistent_attributes = attr
            handler_input.attributes_manager.save_persistent_attributes()  
                  
        return (
            handler_input.response_builder
            .speak(speak_output)
            .set_should_end_session(bools)
            .response
            )