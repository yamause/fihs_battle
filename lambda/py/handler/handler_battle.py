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
        speak_output = "戦闘を開始します、グー、チョキ、パーから一つ選んでください。"
        sess_attr = handler_input.attributes_manager.session_attributes
        sess_attr["battleMode"] = True 
        sess_attr["round"] = 0

        return (
            handler_input.response_builder
            .speak(speak_output)
            .set_should_end_session(False)
            .response
            )