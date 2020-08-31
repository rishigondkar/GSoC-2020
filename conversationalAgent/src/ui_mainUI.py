# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
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


class Ui_guiDlg(object):
    def setupUi(self, guiDlg):
        if not guiDlg.objectName():
            guiDlg.setObjectName(u"guiDlg")
        guiDlg.resize(399, 300)
        guiDlg.setStyleSheet(u"")
        self.rasa_server = QPushButton(guiDlg)
        self.rasa_server.setObjectName(u"rasa_server")
        self.rasa_server.setGeometry(QRect(260, 60, 71, 31))
        self.action_server = QPushButton(guiDlg)
        self.action_server.setObjectName(u"action_server")
        self.action_server.setGeometry(QRect(260, 130, 71, 31))
        self.label = QLabel(guiDlg)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 60, 121, 21))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QLabel(guiDlg)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 130, 131, 21))
        self.label_2.setFont(font)
        self.kill_all = QPushButton(guiDlg)
        self.kill_all.setObjectName(u"kill_all")
        self.kill_all.setGeometry(QRect(150, 190, 100, 31))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.kill_all.setFont(font1)
        self.label_3 = QLabel(guiDlg)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 240, 191, 21))
        self.label_3.setFont(font)
        self.rasa_dialog = QPushButton(guiDlg)
        self.rasa_dialog.setObjectName(u"rasa_dialog")
        self.rasa_dialog.setGeometry(QRect(260, 230, 71, 31))

        self.retranslateUi(guiDlg)

        QMetaObject.connectSlotsByName(guiDlg)
    # setupUi

    def retranslateUi(self, guiDlg):
        guiDlg.setWindowTitle(QCoreApplication.translate("guiDlg", u"conversationalAgent", None))
        self.rasa_server.setText("")
        self.action_server.setText("")
        self.label.setText(QCoreApplication.translate("guiDlg", u"RASA Server", None))
        self.label_2.setText(QCoreApplication.translate("guiDlg", u"Actions Server", None))
        self.kill_all.setText(QCoreApplication.translate("guiDlg", u"Kill All", None))
        self.label_3.setText(QCoreApplication.translate("guiDlg", u"Open Rasa Dialog Box", None))
        self.rasa_dialog.setText(QCoreApplication.translate("guiDlg", u"Open", None))
    # retranslateUi

