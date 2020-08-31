# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import time
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa.core.actions.action import (  # pytype: disable=pyi-error
        ACTION_LISTEN_NAME,
    )
#Robocomp imports
#import trialComponent1 
#from specificworker import *
#import AGMModelConversion
#from AGGL import *

import sys, traceback, IceStorm, time, os, copy, Ice, json
from termcolor import colored

# Ctrl+c handling
import signal

from PySide2 import QtCore
from PySide2 import QtWidgets



class actionlinktalking(Action):
  def name(self):
    return "action_link_talking"

  def run(self, dispatcher, tracker, domain):
    print("action_link_talking")
    talk_dict = { "rasa" : "is_talking"}
    json_object = json.dumps(talk_dict, indent = 4) 
    with open("rasa_conversation.json", "w") as outfile: 
        outfile.write(json_object) 
    return


class actionlinkwaiting(Action):
  def name(self):
    return "action_link_waiting"

  def run(self, dispatcher, tracker, domain):
    print("action_link_waiting")
    talk_dict = { "rasa" : "is_waiting_for_response"}
    json_object = json.dumps(talk_dict, indent = 4) 
    with open("rasa_conversation.json", "w") as outfile: 
        outfile.write(json_object) 
    return


class actionSetGender(Action):
  def name(self):
    return "action_set_gender"

  def run(self, dispatcher, tracker, domain):
    with open('person_attributes.json', 'r') as openfile: 
        # Reading from json file 
        json_object = json.load(openfile)
    
    data = json_object["imGender"]
    SlotSet("gender", data)
    return [SlotSet("gender", data)]


class actionSetSituation(Action):
  def name(self):
    return "action_set_situation"

  def run(self, dispatcher, tracker, domain):
    with open('person_attributes.json', 'r') as openfile: 
        # Reading from json file 
        json_object = json.load(openfile)
    
    data = json_object["imSituation"]
    SlotSet("situation", data)
    return [SlotSet("situation", data)]


class actionStopChatbot(Action):
  def name(self):
    return "action_stop_chatbot"

  def run(self, dispatcher, tracker, domain):
    print("action_link_waiting")
    talk_dict = { "rasa" : "stop"}
    json_object = json.dumps(talk_dict, indent = 4) 
    with open("rasa_conversation.json", "w") as outfile: 
        outfile.write(json_object) 
    return



