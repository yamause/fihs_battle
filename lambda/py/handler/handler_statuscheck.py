import logging

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core import utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class StatusCheckHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("StatusCheckIntent")(handler_input)

    def handle(self, handler_input):
        
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.persistent_attributes
        print(attr)
        max_life = attr["max_life"]
        life = attr["life"]
        power = attr["power"]
        defense = attr["defense"]
        v_count = attr["v_count"]

        speak_output = ("フィッシュの最大ライフは{}、今のライフは{}、パワーは{}、ディフェンスは{}です。現在の勝利数は{}").format(max_life,life,power,defense,v_count)

        return (
            handler_input.response_builder
            .speak(speak_output)
            .set_should_end_session(False)
            .response
        )