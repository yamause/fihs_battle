import logging
import gettext
import random

from ask_sdk_core.dispatch_components import (AbstractRequestHandler, AbstractRequestInterceptor, AbstractExceptionHandler)
from ask_sdk_core import utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class DataResetHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("DataResetIntent")(handler_input)

    def handle(self, handler_input):
        
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.persistent_attributes
        speak_output = ("データを消したよ")

        handler_input.attributes_manager.delete_persistent_attributes()

        return (
            handler_input.response_builder
            .speak(speak_output)
            # .ask("add a reprompt if you want to keep the session open for the user to respond")
            .response
        )