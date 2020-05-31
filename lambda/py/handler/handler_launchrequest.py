import logging
import json

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core import utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput
from mylib import status
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

        class charCreate:
            def __init__(self,status_dict):

                basic_life = status_dict["basic_status"]["basic_life"]
                basic_power = status_dict["basic_status"]["basic_power"]
                basic_defence = status_dict["basic_status"]["basic_defence"]

                var_life = status_dict["var_status"]["var_life"]
                var_power = status_dict["var_status"]["var_power"]
                var_defence = status_dict["var_status"]["var_defence"]

                self.life = status.LifeStatus(basic_life,var_life,0)
                self.power = status.PowerStatus(basic_power,var_power,0)
                self.defence = status.DefenceStatus(basic_defence,var_defence,0)

        if pers_attr :
            var_life = pers_attr["my_status"]["var_status"]["var_life"]
            basic_life = pers_attr["my_status"]["var_status"]["basic_life"]
            condition_seed =  var_life / basic_life
            
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

            # リファクタリング予定地
            # キャラクタ作成モードに遷移させてキャラクタ特性を選択後にから下記の処理を実行する様にしたい

            with open("mylib/parameter_seeds.json") as param:
                pers_attr = json.load(param)

            # My Characterの初期ステータスを作成

            my_char = charCreate(
                pers_attr["parameter"]["my_status"]
                )

            # MY Character のステータスを保存
            # pers_attr -> my_status
            pers_attr["parameter"]["my_status"] = my_char.life.commit_param(pers_attr)
            pers_attr["parameter"]["my_status"] = my_char.power.commit_param(pers_attr)
            pers_attr["parameter"]["my_status"] = my_char.defence.commit_param(pers_attr)

            handler_input.attributes_manager.persistent_attributes = pers_attr
            handler_input.attributes_manager.save_persistent_attributes()

            speak_output = ("初めまして！フィッシュバトルへようこそ！この子があなたの新しいフィッシュです。")
            
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )