import logging

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core import utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from mylib import status

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class BattleIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        
        return ask_utils.is_intent_name("TestIntent")(handler_input)
    
    def handle(self, handler_input):
        
        pers_attr = handler_input.attributes_manager.persistent_attributes

        class charCreate:
            def __init__(self,basic_life,var_life,basic_power,var_power,basic_defence,var_defence):
                self.life = status.LifeStatus(basic_life,var_life)
                self.power = status.PowerStatus(basic_power,var_power)
                self.defence = status.DefenceStatus(basic_defence,var_defence)

            char = charCreate()

        return(
                handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                .response
                )        
