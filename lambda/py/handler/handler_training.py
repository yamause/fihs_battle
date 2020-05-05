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
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.persistent_attributes
        #---------test-------------
        slots = handler_input.request_envelope.request.intent.slots
        speak_output = slots["menu"].resolutions.resolutions_per_authority[0].values[0].value.id
        print(speak_output)
        print(slots)
        #---------test-------------
        
        
        #マイフィッシュの攻撃力、防御力を代入
        my_hp = attr["life"]
        my_power = attr["power"]
        my_defense = attr["defense"]
        
        return (
            handler_input.response_builder
            .speak(speak_output)
            .set_should_end_session(False)
            .response
            )
"""
        #パワーとディフェンスどちらを上げる？
        slot_power = slots[]
        if  == :
        #パワーを上げる
        attr["power"] += random.uniform(0,10)
        speak_output = ("パワーが上がったよ")
        attr["life"] -= 10
        
        #ディフェンスを上げる
        attr["defense"] += random.uniform(0,10)
        speak_output = ("ディフェンスが上がったよ")
        attr["life"] -= 10
        
        #ライフを上げる
        attr["max_life"] += random.uniform(0,10)
        speak_output = ("ライフの最大値が上がったよ")
        attr["life"] -= 10
        
        handler_input.attributes_manager.persistent_attributes = attr
        handler_input.attributes_manager.save_persistent_attributes()
"""