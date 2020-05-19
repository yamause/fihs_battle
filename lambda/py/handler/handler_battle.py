import logging
import random

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core import utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class BattleIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        
        return ask_utils.is_intent_name("BattleIntent")(handler_input)
    
    def handle(self, handler_input):
        
        class CharCreate():
            def __init__(self,name,life,power,defense):
                self.status_dict = {
                    "name":name,
                    "life":life,
                    "power":power,
                    "defense":defense
                    }

        class EnemyCharCreate(CharCreate):
            #敵初期値の設定
            enemy_box = []
            def __init__(self,name,life,power,defense):
            
                super().__init__(name,life,power,defense)
                EnemyCharCreate.enemy_box.append(self)

        class StandardCreate:
            def __init__(self,pers_attr,sess_attr):
                self.pers_attr = pers_attr
                self.sess_attr = sess_attr
                sess_attr["round"] = 0
                sess_attr["my_status"] = {}
                sess_attr["en_status"] = {}
                my = "myfish"

                self.my_fish = CharCreate(
                        my,
                        pers_attr["life"],
                        pers_attr["power"],
                        pers_attr["defense"]
                            )
                enemy_1 = EnemyCharCreate("ザコテキ",100,100,100)
                enemy_2 = EnemyCharCreate("フツテキ",150,150,150)
                enemy_3 = EnemyCharCreate("ツヨテキ",200,200,200)

                            # 敵のランダム出現
                num = random.randint(0,len(EnemyCharCreate.enemy_box) - 1)
                self.enemy_obj = EnemyCharCreate.enemy_box[num]

        pers_attr = handler_input.attributes_manager.persistent_attributes
        sess_attr = handler_input.attributes_manager.session_attributes

        char = StandardCreate(pers_attr,sess_attr)

        sess_attr["my_status"] = char.my_fish.status_dict
        sess_attr["en_status"] = char.enemy_obj.status_dict

        sess_attr["JankenMode"] = True 
        sess_attr["round"] = 0
        print (sess_attr)
        speak_output = ("{}が現れた！戦闘を開始します、グー、チョキ、パーから一つ選んでください。").format(char.enemy_obj.status_dict["name"])

        return (
            handler_input.response_builder
            .speak(speak_output)
            .set_should_end_session(False)
            .response
            )