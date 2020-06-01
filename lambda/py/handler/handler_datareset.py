import logging

from ask_sdk_core.dispatch_components import AbstractRequestHandler
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

        # `yes_no_slot`スロット値の取り出し
        slots = handler_input.request_envelope.request.intent.slots
        slots_id = slots["yes_no_slot"].resolutions.resolutions_per_authority[0].values[0].value.id
        
        # スロット値で条件分岐、データを消してもいいかの確認
        if slots_id == "yes":
            speak_output = ("データを消去しました、ゲームを終了します。")
            handler_input.attributes_manager.delete_persistent_attributes()
            bools = True
        else:
            speak_output = ("キャンセルしました")
            bools = False
        return (
            handler_input.response_builder
            .speak(speak_output)
            .set_should_end_session(bools)
            # .ask("add a reprompt if you want to keep the session open for the user to respond")
            .response
        )