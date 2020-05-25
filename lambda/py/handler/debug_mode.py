import logging

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core import utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class DebugIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("DebugIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        pers_attr = handler_input.attributes_manager.persistent_attributes

        pers_attr["max_life"] = 1000
        pers_attr["life"] = 1000
        pers_attr["power"] = 1000
        pers_attr["defense"] = 1000
        pers_attr["v_count"] = 1000

        speak_output = ("デバッグモードに入ります。デバッグ終了後はデータを消去してください")
        handler_input.attributes_manager.persistent_attributes = pers_attr
        handler_input.attributes_manager.save_persistent_attributes()
        bools = False

        return (
            handler_input.response_builder
            .speak(speak_output)
            .set_should_end_session(bools)
            # .ask("add a reprompt if you want to keep the session open for the user to respond")
            .response
        )