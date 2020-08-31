# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rasaUI.ui'
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


class Ui_rasaWindow(object):
    def setupUi(self, rasaWindow):
        if not rasaWindow.objectName():
            rasaWindow.setObjectName(u"rasaWindow")
        rasaWindow.resize(449, 359)
        self.centralwidget = QWidget(rasaWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.rasa_train = QPushButton(self.centralwidget)
        self.rasa_train.setObjectName(u"rasa_train")
        self.rasa_train.setGeometry(QRect(280, 80, 111, 41))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rasa_train.setFont(font)
        self.rasa_interactive = QPushButton(self.centralwidget)
        self.rasa_interactive.setObjectName(u"rasa_interactive")
        self.rasa_interactive.setGeometry(QRect(280, 140, 111, 41))
        self.rasa_interactive.setFont(font)
        self.rasa_shell = QPushButton(self.centralwidget)
        self.rasa_shell.setObjectName(u"rasa_shell")
        self.rasa_shell.setGeometry(QRect(280, 200, 111, 41))
        self.rasa_visualize = QPushButton(self.centralwidget)
        self.rasa_visualize.setObjectName(u"rasa_visualize")
        self.rasa_visualize.setGeometry(QRect(280, 260, 111, 41))
        self.action_server = QPushButton(self.centralwidget)
        self.action_server.setObjectName(u"action_server")
        self.action_server.setGeometry(QRect(315, 20, 41, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 20, 131, 41))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 80, 131, 41))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_2.setFont(font2)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 140, 131, 41))
        self.label_3.setFont(font2)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 200, 131, 41))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 260, 131, 41))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)
        #rasaWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(rasaWindow)

        QMetaObject.connectSlotsByName(rasaWindow)
    # setupUi

    def retranslateUi(self, rasaWindow):
        rasaWindow.setWindowTitle(QCoreApplication.translate("rasaWindow", u"Rasa_Dialog_Box", None))
        self.rasa_train.setText(QCoreApplication.translate("rasaWindow", u"Rasa Train", None))
        self.rasa_interactive.setText(QCoreApplication.translate("rasaWindow", u"Rasa Interactive", None))
        self.rasa_shell.setText(QCoreApplication.translate("rasaWindow", u"Rasa Shell", None))
        self.rasa_visualize.setText(QCoreApplication.translate("rasaWindow", u"Rasa Visualize", None))
        self.action_server.setText("")
        self.label.setText(QCoreApplication.translate("rasaWindow", u"Rasa Action Server", None))
        self.label_2.setText(QCoreApplication.translate("rasaWindow", u"Train Rasa Model", None))
        self.label_3.setText(QCoreApplication.translate("rasaWindow", u"Start interactive\n"
" learning session", None))
        self.label_4.setText(QCoreApplication.translate("rasaWindow", u"Test Rasa in Shell", None))
        self.label_5.setText(QCoreApplication.translate("rasaWindow", u"Visualize Stories", None))
    # retranslateUi

