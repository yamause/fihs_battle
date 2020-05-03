# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import gettext

from ask_sdk_core.skill_builder import SkillBuilder
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

# S3
from ask_sdk_core.skill_builder import CustomSkillBuilder
from ask_sdk_s3.adapter import S3Adapter
s3_adapter = S3Adapter(bucket_name="bucketname")

# i18n
from alexa import data

# 各種ハンドラのインポート
from handler import handler_launchrequest
from handler import handler_helloworld
from handler import handler_helpintent
from handler import handler_cancelorstopintent
from handler import handler_sessionendedrequesthandler
from handler import handler_intentreflectionhandler
from handler import handler_localizationinterceptor
from handler import handler_catchallexceptionhandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = CustomSkillBuilder(persistence_adapter=s3_adapter)

sb.add_request_handler(handler_launchrequest.LaunchRequestHandler())
sb.add_request_handler(handler_helloworld.HelloWorldIntentHandler())
sb.add_request_handler(handler_helpintent.HelpIntentHandler())
sb.add_request_handler(handler_cancelorstopintent.CancelOrStopIntentHandler())
sb.add_request_handler(handler_sessionendedrequesthandler.SessionEndedRequestHandler())
# make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers
sb.add_request_handler(handler_intentreflectionhandler.IntentReflectorHandler())
sb.add_global_request_interceptor(handler_localizationinterceptor.LocalizationInterceptor())
sb.add_exception_handler(handler_catchallexceptionhandler.CatchAllExceptionHandler())

handler = sb.lambda_handler()
