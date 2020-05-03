import logging
import gettext
import random

from ask_sdk_core.dispatch_components import (AbstractRequestHandler, AbstractRequestInterceptor, AbstractExceptionHandler)
from ask_sdk_core import utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class BattleIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BattleldIntent")(handler_input)

    def handle(self, handler_input):
        
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.persistent_attributes
        
        #マイフィッシュの攻撃力、防御力を代入
        mhp = attr["life"]
        mp = attr["power"]
        md = attr["defense"]
        
        #敵フィッシュの攻撃力、防御力を代入
        ehp = mhp + random.uniform(-10,20)
        ep = mp + random.uniform(-10,20) 
        ed = md + rando.uniform(-10,20)

        #防御力を加味した攻撃力の計算
        myfish_A = ma - ed + random.uniform(-5,10)
        emfish_A = ea - md + random.uniform(-5,10)

        #HPを減産
        mhp_after = mhp - emfish_A
        ehp_after = ehp - myfish_A

        #割合の計算
        mdown = 1 - mhp_after / mhp
        edown = 1 - ehp_after / ehp

        #比較
        if mdown > edown:
	    speak_output = ("おまえの負け")
	    attr["v_count"] += 1
        attr["life"] -= emfish_A
        elif mdown < edown:
	    speak_output = ("おまえの勝ち")
        attr["life"] -= emfish_A
        else:
	　　speak_output = ("おまえら強さ同じ")

        handler_input.attributes_manager.persistent_attributes = attr
        handler_input.attributes_manager.save_persistent_attributes()

        return (
            handler_input.response_builder
            .speak(speak_output)
            # .ask("add a reprompt if you want to keep the session open for the user to respond")
            .response
        )