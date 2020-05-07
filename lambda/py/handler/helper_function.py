import logging

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core import utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def died_fish(bools=True,)
    # フィッシュの死亡処理。S3のデータを削除する。
    handler_input.attributes_manager.delete_persistent_attributes()
    speak_output = ("あなたのフィッシュのライフが0になり、死んでしまいました。また初めから遊んでください。")

    return(speak_output,bools)