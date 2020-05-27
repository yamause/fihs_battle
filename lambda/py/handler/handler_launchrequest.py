import logging

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core import utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        pers_attr = handler_input.attributes_manager.persistent_attributes
        sess_attr = handler_input.attributes_manager.session_attributes

        sess_attr["gameMode"] = "normal" 


        if pers_attr :
            life = pers_attr["life"]
            max_life = pers_attr["max_life"]
            condition_seed =  life / max_life
            
            if condition_seed == 1:
                fish_condition = "元気いっぱい"
            elif condition_seed > 0.8:
                fish_condition = "調子は普通"
            elif condition_seed > 0.5:
                fish_condition = "ちょっと疲れてる"
            elif condition_seed <= 0:
                fish_condition = "じっと動かない...とても具合が悪い"
            else:
                fish_condition = "とても疲れてる"

            speak_output = ("こんにちは！フィッシュバトルへようこそ！あなたのフィッシュは{}みたい。").format(fish_condition)
        else:
            pers_attr["max_life"] = 100
            pers_attr["life"] = 100
            pers_attr["power"] = 100
            pers_attr["defense"] = 100
            pers_attr["v_count"] = 0

            handler_input.attributes_manager.persistent_attributes = pers_attr
            handler_input.attributes_manager.save_persistent_attributes()
            speak_output = ("初めまして！フィッシュバトルへようこそ！この子があなたの新しいフィッシュです。")
            
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )