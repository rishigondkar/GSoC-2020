#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2020 by YOUR NAME HERE
#
#    This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
#

from genericworker import *
from PySide2.QtCore import QDateTime
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

#AGM related imports
import AGMModelConversion
from AGGL import *

from multiprocessing import Process
import socket
import os
import time
from datetime import date, datetime
import requests
import json

try:
    from ui_chatbotUI import *
except:
    print("Can't import ui_chatbotUI file")

try:
    from ui_rasaUI import *
except:
    print("Can't import ui_rasaUI file")

try:
    import speech_recognition as sr
    import pyaudio
    import wave
except:
    print("Can't import speech_recognition or pyaudio or wave")

# If RoboComp was compiled with Python bindings you can use InnerModel in Python
# sys.path.append('/opt/robocomp/lib')
# import librobocomp_qmat
# import librobocomp_osgviewer
# import librobocomp_innermodel


class OpenChatbotUI(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.parent = parent
        self.ui = Ui_interactionWindow()
        self.ui.setupUi(self)
        self.setModal(True)
        #proc = Process(target=self.compute, args=())
        #proc.start()

        self.interactionUI = False
        self.bot_message = ""

        #self.ui.textbox.setFocus()
        self.ui.send.clicked.connect(self.send_message)
        self.ui.rasa_server.clicked.connect(self.rasa_server_button_click())
        self.ui.action_server.clicked.connect(self.action_server_button_click())

        #text formatting
        self.ui.textbox.setStyleSheet("font-weight: bold; font-size: 18pt; font-family: Times New Roman, Times, serif;")
        self.ui.display.setStyleSheet("font-size: 12pt; font-family: Times New Roman, Times, serif;")

        # initialisation related to TTS/ASR
        self.ui.speak.clicked.connect(self.speak_button_press)
        self.ui.listen.clicked.connect(self.listen_button_press)
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.RECORD_SECONDS = 5
        self.WAVE_OUTPUT_FILENAME = "output.wav"

    # Send post request to Rasa server
    def send_message(self):
        if self.ui.textbox.text() != '':
            self.ui.display.append("<span style= color:blue; font-size:14pt >Person: </span>"+ self.ui.textbox.text() + "\n")
            msg = self.ui.textbox.text()
            self.ui.textbox.clear()
            r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": "Person", "message": msg})
            for i in r.json():
                bot_message = i['text']
                self.ui.display.append("<span style= color:blue; font-size:14pt >Robot: </span>" + bot_message + "\n")#f"{i['text']}""
                self.bot_message = bot_message
        else:
            return
        

    def rasa_server_button_click(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 5002))

        if result == 0:
            return

        else:
            proc = Process(target=self.start_rasa_server, args=())
            proc.start()


    def action_server_button_click(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 5055))

        if result == 0:
            return

        else:
            proc = Process(target=self.start_action_server, args=())
            proc.start()


    def start_rasa_server(self):
        try:
            os.system("cd chatbot; gnome-terminal -e 'rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml --enable-api'")
        except:
            print("Cannot start Rasa Server")


    def start_action_server(self):
        try:
            os.system("cd chatbot;gnome-terminal -e 'rasa run actions'")
        except:
            print("Cannot start Actions Server")



    def rasa_server_button_color(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 5002))
        if result == 0:
            self.ui.rasa_server.setStyleSheet("background-color: green")
        else:
            self.ui.rasa_server.setStyleSheet("background-color: red")


    def action_server_button_color(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 5055))
        if result == 0:
            self.ui.action_server.setStyleSheet("background-color: green")
        else:
            self.ui.action_server.setStyleSheet("background-color: red")


    #Calling functions to change button colours together
    def button_colors(self):
        self.rasa_server_button_color()
        self.action_server_button_color()


    #Text to speech implementation
    def _say_with_festival(self, text):
        shellcommand = "echo \"%s\" | iconv -f utf-8 -t iso-8859-1 | padsp festival --tts --language english" % text
        print('Order: ' + text)
        print('Shell: "' + shellcommand + '"')
        if os.system(shellcommand):
            print("install festivale using the below command")
            print("sudo apt-get install festival festvox-kallpc16k")


    def listen_button_press(self):
        print("speak")
        speak_text = self.bot_message
        self._say_with_festival(speak_text)


    #Speech to text implementation
    def speak_button_press(self):
        try:
            p = pyaudio.PyAudio()
            stream = p.open(format=self.FORMAT,
                            channels=self.CHANNELS,
                            rate=self.RATE,
                            input=True,
                            frames_per_buffer=self.CHUNK)
            self.ui.status.setText("recording..")
            self.ui.status.repaint()
            print("* recording")

            frames = []

            for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
                data = stream.read(self.CHUNK)
                frames.append(data)

            self.ui.status.setText("Done recording")
            self.ui.status.repaint()
            print("* done recording")

            stream.stop_stream()
            stream.close()
            p.terminate()

            wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

            r = sr.Recognizer()
            with sr.Microphone() as source:  # use the default microphone as the audio source
                audio = r.adjust_for_ambient_noise(
                    source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels

            with sr.WavFile("output.wav") as source:
                audio = r.record(source)
            try:
                self.ui.status.setText("Analysing")
                self.ui.status.repaint()
                command = r.recognize_google(audio,
                                             language="en-US")  # recognize speech using Google Speech Recognition
                print(command)
                self.ui.textbox.setText(command)
                self.ui.status.setText("")
                self.ui.status.repaint()
            except LookupError:  # speech is unintelligible
                self.ui.status.setText("Say Again..")
                self.ui.status.repaint()
                print("Could not understand audio")
                self.ui.textbox.setText("Error, not understand audio")
        except:
            print("error ")



class OpenRasaUI(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.parent = parent
        self.ui = Ui_rasaWindow()
        self.ui.setupUi(self)
        self.setModal(True)


        self.ui.action_server.clicked.connect(self.action_server_button_click_rasaUI)
        self.ui.rasa_train.clicked.connect(self.rasa_train_button_click)
        self.ui.rasa_interactive.clicked.connect(self.rasa_interactive_button_click)
        self.ui.rasa_shell.clicked.connect(self.rasa_shell_button_click)
        self.ui.rasa_visualize.clicked.connect(self.rasa_visualize_button_click)

    def action_server_button_click_rasaUI(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 5055))

        if result == 0:
            os.system("fuser -k 5055/tcp")

        else:
            proc = Process(target=self.start_action_server, args=())
            proc.start()


    def start_action_server(self):
        try:
            os.system("cd chatbot;gnome-terminal -e 'rasa run actions'")
        except:
            print("Cannot start Actions Server")

    def action_server_button_color(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 5055))
        if result == 0:
            self.ui.action_server.setStyleSheet("background-color: green")
        else:
            self.ui.action_server.setStyleSheet("background-color: red")


    #Button to train a new Rasa model
    def rasa_train_button_click(self):
        proc = Process(target=self.start_rasa_train, args=())
        proc.start() 

    def start_rasa_train(self):
        try:
            os.system("cd chatbot;gnome-terminal -e 'rasa train'")
        except:
            print("Cannot train model, check for errors in rasa files")


    #Button to start an interactive session to create new stories by simulating conversations
    def rasa_interactive_button_click(self):
        proc = Process(target=self.start_rasa_interactive, args=())
        proc.start() 

    def start_rasa_interactive(self):
        try:
            os.system("cd chatbot;gnome-terminal -e 'rasa interactive'")
        except:
            print("Cannot start interactive learning session")


    #Button to start Rasa shell for testing
    def rasa_shell_button_click(self):
        proc = Process(target=self.start_rasa_shell, args=())
        proc.start() 

    def start_rasa_shell(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 5055))
        if result == 0:
            print("Rasa actions server already running")

        else:
            proc = Process(target=self.start_action_server, args=())
            proc.start()
        try:
            os.system("cd chatbot;gnome-terminal -e 'rasa shell'")
        except:
            print("Cannot start rasa shell")


    #Button to visualize Rasa Stories
    def rasa_visualize_button_click(self):
        proc = Process(target=self.start_rasa_visualize, args=())
        proc.start() 

    def start_rasa_visualize(self):
        try:
            os.system("cd chatbot;gnome-terminal -e 'rasa visualize'")
        except:
            print("Cannot visualize Rasa Stories")




class SpecificWorker(GenericWorker):
    def __init__(self, proxy_map):
        super(SpecificWorker, self).__init__(proxy_map)
        self.timer.timeout.connect(self.compute)
        self.Period = 2000
        self.timer.start(self.Period)
        self.rasa_server_active = False
        self.action_server_active = False
        self.AGMinit()

        self.situation = ''
        self.human_id = ''
        self.robot_id = ''
        self.human_gender = ''
        self.link = ''
        self.action = 'none'
        self.change_attributes = {"rasa": ""}
        self.ui_lock = False
        self.restart = False
        
        self.eraseFiles()

        #UI Connection
        self.ui.rasa_server.clicked.connect(self.rasa_server_button_click)
        self.ui.action_server.clicked.connect(self.action_server_button_click)
        self.ui.rasa_dialog.clicked.connect(self.openRasaDialog)
        self.ui.kill_all.clicked.connect(self.kill_all_server)

        self.interaction = OpenChatbotUI(self)
        self.rasaDialog = OpenRasaUI(self)



    def __del__(self):
        print('SpecificWorker destructor')

        return True

    #Open Rasa dialog box
    def openRasaDialog(self):
        self.rasaDialog.show()

    #Initialize AGM
    def AGMinit(self):
        self.worldModel = AGMGraph()
        try:
            w = self.agmexecutive_proxy.getModel()
            self.AGMExecutiveTopic_structuralChange(w)
            print("Running")

        except:
            print("The executive is probably not running, waiting for first AGM model publication...")
        src = self.worldModel


    #Function to update dsr when we have made changes to AGM local model
    def updatingDSR(self):
        try:
            newModel = AGMModelConversion.fromInternalToIce(self.worldModel)
            self.agmexecutive_proxy.structuralChangeProposal(newModel, "component_name", "Log_fileName")
            w = self.agmexecutive_proxy.getModel()
            self.worldModel = AGMModelConversion.fromIceToInternal_model(w)
            print("AGM successfully updated")
        except:
            print("Exception moving in AGM") 


    #Function to erase and initialize rasa_conversation Json file
    def eraseFiles(self):
        sample = self.change_attributes
        json_object = json.dumps(sample, indent = 4)
        with open('chatbot/rasa_conversation.json', 'w') as outfile:
            outfile.write(json_object)
    
    #Function to write to file
    def writeToFile(self,id,situation):
        self.AGMinit()
        try:
            src = self.worldModel
            person_attributes = src.getNode(id).attributes
            attributes = {}
            attributes['imGender'] = person_attributes['imGender']
            attributes['imSituation'] = situation
            self.human_gender = person_attributes['imGender']

            json_object = json.dumps(attributes, indent = 4)
            with open("chatbot/person_attributes.json", "w") as outfile: 
                outfile.write(json_object)
        except:
            print("Could not write to file person_attributes.json")
        return


    #Function to read from file
    def readFromFile(self):
        with open('chatbot/rasa_conversation.json', 'r') as openfile: 
            attrs = json.load(openfile)
            if attrs["rasa"] == self.change_attributes["rasa"]:
                return False
            else:
                attrs["timeStarted"] = str(datetime.now())
                self.change_attributes = attrs
                return True

    #Function to update AGM Graph locally and globally
    def updateGraph(self):
        flag = self.readFromFile()
        if flag:
            attrs = self.change_attributes
            try:
                model = self.worldModel
                model.addEdge(self.human_id, self.robot_id, self.link, attrs)
                self.updatingDSR()
            except:
                print("Could not change attributes of link")
            if attrs["rasa"] == "stop":
                self.stopChatbot()
            else:
                return
        else:
            return


    #Function to stop chatbot and close interaction dialog box when user says OK to move
    def stopChatbot(self):
        self.interaction.interactionUI = False
        self.interaction.ui.display.clear()
        #self.interaction.ui.textbox.clear()
        self.interaction.hide()
        r = requests.post('http://localhost:5002/conversations/default/tracker/events', json=[{"event": "restart"}, {"event": "followup","name": "action_listen"}])
        self.ui_lock = True
        self.change_attributes = {"rasa": ""}
        self.eraseFiles()

        time.sleep(15)
        print(self.ui_lock)
        self.ui_lock = False
        print(self.ui_lock)
        print(self.action)
        if self.action != 'none':
            print("I am here")
            self.interaction.interactionUI = True
            self.startChatbot
        else:
            self.situation = ''
            self.human_id = ''
            self.robot_id = ''
            self.human_gender = ''
            self.link = ''
            self.change_attributes = {}
            return

    #Function to start chatbot and initialize conversation
    def startChatbot(self):
        self.interaction.show()
        r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": "Person", "message": "start"})
        for i in r.json():
            bot_message = i['text']
            self.interaction.ui.display.append("<span style= color:blue; font-size:14pt >Robot: </span>" + bot_message + "\n")#f"{i['text']}""
            self.interaction.bot_message = bot_message
        print("Chatbot started successfully!!!")
        return


    #Function to keep interaction ui active even if user tries to close it to force the user to reply
    def keepUiActive(self):
        if self.interaction.interactionUI == True:
            if self.interaction.isVisible() == False:
                self.interaction.show()
        return


    def rasa_server_button_click(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 5002))

        if result == 0:
            os.system("fuser -k 5002/tcp")
            self.rasa_server_active = False

        else:
            if self.rasa_server_active == False:
                proc = Process(target=self.start_rasa_server, args=())
                proc.start()
                self.rasa_server_active = True
            else:
                return


    def action_server_button_click(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 5055))

        if result == 0:
            os.system("fuser -k 5055/tcp")
            self.action_server_active = False

        else:
            if self.action_server_active == False:
                proc = Process(target=self.start_action_server, args=())
                proc.start()
                self.action_server_active = True
            else:
                return


    def start_rasa_server(self):
        try:
            os.system("cd chatbot;gnome-terminal -e 'rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml --enable-api'")
        except:
            print("Cannot start Rasa Server")


    def start_action_server(self):
        try:
            os.system("cd chatbot;gnome-terminal -e 'rasa run actions'")
        except:
            print("Cannot start Actions Server")


    #Button to kill both Rasa and Action server
    def kill_all_server(self):
        os.system("fuser -k 5002/tcp")
        os.system("fuser -k 5055/tcp")


    def rasa_server_button_color(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 5002))
        if result == 0:
            self.ui.rasa_server.setStyleSheet("background-color: green")
        else:
            self.ui.rasa_server.setStyleSheet("background-color: red")


    def action_server_button_color(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 5055))
        if result == 0:
            self.ui.action_server.setStyleSheet("background-color: green")
        else:
            self.ui.action_server.setStyleSheet("background-color: red")
    



    @QtCore.Slot()
    def compute(self):
        self.rasa_server_button_color()
        self.action_server_button_color()
        self.interaction.button_colors()
        self.rasaDialog.action_server_button_color()
        self.keepUiActive()
        #self.restartChatbot()
        if self.interaction.interactionUI == True:
            self.updateGraph()

        return True



    #
    # SUBSCRIPTION to edgeUpdated method from AGMExecutiveTopic interface
    #
    def setParams(self, params):
        
        return True
    def AGMExecutiveTopic_edgeUpdated(self, modification):
        #
        #subscribesToCODE
        #
        pass


    #
    # SUBSCRIPTION to edgesUpdated method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_edgesUpdated(self, modifications):
        #
        #subscribesToCODE
        #
        pass


    #
    # SUBSCRIPTION to selfEdgeAdded method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_selfEdgeAdded(self, nodeid, edgeType, attributes):
        #
        #subscribesToCODE
        #
        pass


    #
    # SUBSCRIPTION to selfEdgeDeleted method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_selfEdgeDeleted(self, nodeid, edgeType):
        #
        #subscribesToCODE
        #
        pass


    #
    # SUBSCRIPTION to structuralChange method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_structuralChange(self, w):
        self.mutex.lock()
        #print("before")
        #print(type(self.worldModel), type(w))
        self.worldModel = AGMModelConversion.fromIceToInternal_model(w)
        #print("after")
        #print(type(self.worldModel), type(w))
        #print(self.worldModel)
        # fromIceToInternal(w, worldModel)
        self.mutex.unlock()


    #
    # SUBSCRIPTION to symbolUpdated method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_symbolUpdated(self, modification):
        #
        #subscribesToCODE
        #
        pass


    #
    # SUBSCRIPTION to symbolsUpdated method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_symbolsUpdated(self, modifications):
        #
        #subscribesToCODE
        #
        pass


    # =============== Methods for Component Implements ==================
    # ===================================================================

    #
    # activateAgent
    #

    #Function that will recieve parameters from mission and will activate agent
    def AGMCommonBehavior_activateAgent(self, prs):
        print("------------------------parameters recieved------------------------")
        ret = bool()
        self.action = prs['action'].value
        if not self.ui_lock:
            if prs['action'].value != 'none':
                
                if self.interaction.interactionUI == False:
                    print("--------------Planning to start UI-------------------------")
                    if prs['action'].value == 'path_blocked':
                        if self.interaction.isVisible() == False:
                            self.interaction.interactionUI = True
                            self.situation = 'one'
                            self.link = "block"
                            self.human_id = prs['human'].value
                            self.robot_id = prs['robot'].value
                            self.writeToFile(prs['human'].value, self.situation)
                            self.startChatbot()
                    
                    elif prs['action'].value == 'path_softBlocked':
                        if self.interaction.isVisible() == False:
                            self.interaction.interactionUI = True
                            self.situation = 'two'
                            self.link = "softBlock"
                            self.human_id = prs['human'].value
                            self.robot_id = prs['robot'].value
                            self.writeToFile(self.situation)
                            self.startChatbot()
                    
                    elif prs['action'].value == 'path_affordanceBlock':
                        if self.interaction.isVisible() == False:
                            self.interaction.interactionUI = True
                            self.situation = 'three'
                            self.link = "affordanceBlock"
                            self.human_id = prs['human'].value
                            self.robot_id = prs['robot'].value
                            self.writeToFile(prs['human'].value, self.situation)
                            self.startChatbot()

                    else:
                        print("Wrong Plan Recieved")

                else:        

                    if prs['action'].value == 'path_blocked':
                        if self.interaction.isVisible() == False:
                            self.interaction.show()  
                    
                    elif prs['action'].value == 'path_softBlocked':
                        if self.interaction.isVisible() == False:
                            self.interaction.show()
                    
                    elif prs['action'].value == 'path_affordanceBlock':
                        if self.interaction.isVisible() == False:
                            self.interaction.show() 

                    else:
                        print("Wrong Plan Recieved")

            else:
                if self.interaction.interactionUI == False:
                    return

                else:
                    self.interaction.interactionUI = False
                    #self.interaction.ui.display.clear()
                    #self.interaction.ui.textbox.clear()
                    self.interaction.hide()
                    r = requests.post('http://localhost:5002/conversations/default/tracker/events', json=[{"event": "restart"}, {"event": "followup","name": "action_listen"}])
                    print(r)
                    print("Conversation cleared")
        return ret


    #
    # deactivateAgent
    #
    def AGMCommonBehavior_deactivateAgent(self):
        ret = bool()
        #
        # implementCODE
        #
        return ret


    #
    # getAgentParameters
    #
    def AGMCommonBehavior_getAgentParameters(self):
        ret = ParameterMap()
        print("IT WORKED YAY AGMCommonBehavior_getAgentParameters 1234444324343243")
        print(type(ret))
        print(ret)
        print("BYE")
        #
        # implementCODE
        #
        return ret


    #
    # getAgentState
    #
    def AGMCommonBehavior_getAgentState(self):
        ret = StateStruct()
        #
        # implementCODE
        #
        return ret


    #
    # killAgent
    #
    def AGMCommonBehavior_killAgent(self):
        #
        # implementCODE
        print("Vedika is called GUTTA SINGH and BHOPLA")
        #
        pass


    #
    # reloadConfigAgent
    #
    def AGMCommonBehavior_reloadConfigAgent(self):
        ret = bool()
        #
        # implementCODE
        #
        return ret


    #
    # setAgentParameters
    #
    def AGMCommonBehavior_setAgentParameters(self, prs):
        ret = bool()
        #
        # implementCODE
        #
        return ret


    #
    # uptimeAgent
    #
    def AGMCommonBehavior_uptimeAgent(self):
        ret = int()
        #
        # implementCODE
        #
        return ret

    # ===================================================================
    # ===================================================================



    def updatingDSR(self):
        try:
            newModel = AGMModelConversion.fromInternalToIce(self.worldModel)
            self.agmexecutive_proxy.structuralChangeProposal(newModel, "component_name", "Log_fileName")
            w = self.agmexecutive_proxy.getModel()
            self.worldModel = AGMModelConversion.fromIceToInternal_model(w)
            print("AGM successfully updated")
        except:
            print("Exception moving in AGM")

