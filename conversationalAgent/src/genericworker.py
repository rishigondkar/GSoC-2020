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

import sys, Ice, os
from PySide2 import QtWidgets, QtCore

ROBOCOMP = ''
try:
    ROBOCOMP = os.environ['ROBOCOMP']
except KeyError:
    print('$ROBOCOMP environment variable not set, using the default value /opt/robocomp')
    ROBOCOMP = '/opt/robocomp'

Ice.loadSlice("-I ./src/ --all ./src/CommonBehavior.ice")
import RoboCompCommonBehavior

additionalPathStr = ''
icePaths = [ '/opt/robocomp/interfaces' ]
try:
    SLICE_PATH = os.environ['SLICE_PATH'].split(':')
    for p in SLICE_PATH:
        icePaths.append(p)
        additionalPathStr += ' -I' + p + ' '
    icePaths.append('/opt/robocomp/interfaces')
except:
    print('SLICE_PATH environment variable was not exported. Using only the default paths')
    pass

Ice.loadSlice("-I ./src/ --all ./src/AGMCommonBehavior.ice")
from RoboCompAGMCommonBehavior import *
Ice.loadSlice("-I ./src/ --all ./src/AGMExecutive.ice")
from RoboCompAGMExecutive import *
Ice.loadSlice("-I ./src/ --all ./src/AGMExecutiveTopic.ice")
from RoboCompAGMExecutiveTopic import *
Ice.loadSlice("-I ./src/ --all ./src/AGMWorldModel.ice")
from RoboCompAGMWorldModel import *
Ice.loadSlice("-I ./src/ --all ./src/GenericBase.ice")
from RoboCompGenericBase import *
Ice.loadSlice("-I ./src/ --all ./src/InnerModelManager.ice")
from RoboCompInnerModelManager import *
Ice.loadSlice("-I ./src/ --all ./src/Laser.ice")
from RoboCompLaser import *
Ice.loadSlice("-I ./src/ --all ./src/OmniRobot.ice")
from RoboCompOmniRobot import *
Ice.loadSlice("-I ./src/ --all ./src/Planning.ice")
from RoboCompPlanning import *

from agmcommonbehaviorI import *
from agmexecutivetopicI import *


try:
    from ui_mainUI import *
except:
    print("Can't import UI file. Did you run 'make'?")
    sys.exit(-1)



class GenericWorker(QtWidgets.QWidget):

    kill = QtCore.Signal()

    def __init__(self, mprx):
        super(GenericWorker, self).__init__()

        self.agmexecutive_proxy = mprx["AGMExecutiveProxy"]
        self.innermodelmanager_proxy = mprx["InnerModelManagerProxy"]
        self.laser_proxy = mprx["LaserProxy"]
        self.omnirobot_proxy = mprx["OmniRobotProxy"]

        self.ui = Ui_guiDlg()
        self.ui.setupUi(self)
        self.show()

        self.mutex = QtCore.QMutex(QtCore.QMutex.Recursive)
        self.Period = 30
        self.timer = QtCore.QTimer(self)


    @QtCore.Slot()
    def killYourSelf(self):
        rDebug("Killing myself")
        self.kill.emit()

    # \brief Change compute period
    # @param per Period in ms
    @QtCore.Slot(int)
    def setPeriod(self, p):
        print("Period changed", p)
        self.Period = p
        self.timer.start(self.Period)
