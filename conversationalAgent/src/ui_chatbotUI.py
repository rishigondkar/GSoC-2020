# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chatbotUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_interactionWindow(object):
    def setupUi(self, interactionWindow):
        if not interactionWindow.objectName():
            interactionWindow.setObjectName(u"interactionWindow")
        interactionWindow.resize(600, 600)
        self.centralwidget = QWidget(interactionWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.display = QTextEdit(self.centralwidget)
        self.display.setObjectName(u"display")
        self.display.setGeometry(QRect(25, 30, 550, 451))
        self.display.setFocusPolicy(Qt.NoFocus)
        self.send = QPushButton(self.centralwidget)
        self.send.setObjectName(u"send")
        self.send.setGeometry(QRect(490, 490, 80, 41))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.send.setFont(font)
        self.listen = QPushButton(self.centralwidget)
        self.listen.setObjectName(u"listen")
        self.listen.setGeometry(QRect(480, 540, 91, 41))
        font1 = QFont()
        font1.setPointSize(11)
        self.listen.setFont(font1)
        self.speak = QPushButton(self.centralwidget)
        self.speak.setObjectName(u"speak")
        self.speak.setGeometry(QRect(25, 540, 91, 41))
        self.speak.setFont(font1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 8, 91, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(400, 8, 101, 16))
        self.rasa_server = QPushButton(self.centralwidget)
        self.rasa_server.setObjectName(u"rasa_server")
        self.rasa_server.setGeometry(QRect(200, 8, 16, 16))
        self.action_server = QPushButton(self.centralwidget)
        self.action_server.setObjectName(u"action_server")
        self.action_server.setGeometry(QRect(510, 10, 16, 16))
        self.textbox = QLineEdit(self.centralwidget)
        self.textbox.setObjectName(u"textbox")
        self.textbox.setGeometry(QRect(25, 490, 461, 41))
        self.status = QLabel(self.centralwidget)
        self.status.setObjectName(u"status")
        self.status.setGeometry(QRect(128, 550, 171, 20))
        #interactionWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(interactionWindow)

        QMetaObject.connectSlotsByName(interactionWindow)
    # setupUi

    def retranslateUi(self, interactionWindow):
        interactionWindow.setWindowTitle(QCoreApplication.translate("interactionWindow", u"Interaction", None))
        self.send.setText(QCoreApplication.translate("interactionWindow", u"SEND", None))
        self.listen.setText(QCoreApplication.translate("interactionWindow", u"Listen", None))
        self.speak.setText(QCoreApplication.translate("interactionWindow", u"Speak", None))
        self.label.setText(QCoreApplication.translate("interactionWindow", u"RASA Server", None))
        self.label_2.setText(QCoreApplication.translate("interactionWindow", u"Actions Server", None))
        self.rasa_server.setText("")
        self.action_server.setText("")
        self.status.setText("")
    # retranslateUi

