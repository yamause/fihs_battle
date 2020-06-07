import logging

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core import utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response
from mylib import status


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class StatusCheckHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("StatusCheckIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        pers_attr = handler_input.attributes_manager.persistent_attributes
        my_char = status.charCreate(pers_attr)

        max_life    = my_char.life.max_param
        life        = my_char.life.var_param
        power       = my_char.power.max_param
        defense     = my_char.defence.max_param
        v_count     = "調整中です"

        speak_output = ("フィッシュの最大ライフは{}、今のライフは{}、パワーは{}、ディフェンスは{}です。現在の勝利数は{}").format(max_life,life,power,defense,v_count)

        return (
            handler_input.response_builder
            .speak(speak_output)
            .set_should_end_session(False)
            .response
        )