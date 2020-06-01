import logging

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core import utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput
from mylib import status


from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class DeadIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        pers_attr = handler_input.attributes_manager.persistent_attributes
        my_char = status.charCreate(pers_attr)
        return my_char.life.var_param <= 0

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        speak_output = ("あなたのフィッシュが死んでしまいました...また初めから遊んでください。ゲームを終了します。")
        handler_input.attributes_manager.delete_persistent_attributes()
        bools = True

        return (
            handler_input.response_builder
            .speak(speak_output)
            .set_should_end_session(bools)
            # .ask("add a reprompt if you want to keep the session open for the user to respond")
            .response
        )