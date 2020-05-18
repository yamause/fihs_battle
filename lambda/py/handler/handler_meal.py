import logging
import random

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core import utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class MealIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MealIntent")(handler_input)

    def handle(self, handler_input):

        attr = handler_input.attributes_manager.persistent_attributes

        Life = attr["life"]
        MaxLife = attr["max_life"]

        if Life >= MaxLife:
            speak_output = "もうお腹いっぱいで食べられないみたい"

        else:    
            #ライフを回復する
            life_healing = int(30)
            Life += life_healing
            Life = MaxLife if Life >= MaxLife else Life 
            
            status = Life
            real_healing = Life - attr["life"]

            speak_output = ("ライフが{}回復したよ。現在のライフは{}です").format(real_healing,status)

            attr["life"] = Life
            handler_input.attributes_manager.persistent_attributes = attr
            handler_input.attributes_manager.save_persistent_attributes()

        return (
            handler_input.response_builder
            .speak(speak_output)
            .set_should_end_session(False)
            .response
            )
