#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu November  21 10:41 2019

@author: pierreb
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pymysql


from PyQt5 import QtCore, QtGui, QtWidgets, uic
import pymysql
import sys
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import qApp
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, \
    QTableWidget, QTableWidgetItem, QMessageBox, QHBoxLayout, QLineEdit, QLabel, QGridLayout, QHeaderView
from Qualification_add import Ui_Form


class Ui_Attachment(object):
    def setupUi(self, Attachment):
        Attachment.setObjectName("Activity Type Details")
        Attachment.resize(591, 207)
        self.pushButton_6 = QtWidgets.QPushButton(Attachment)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 170, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(Attachment)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 170, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Add_ActivityType)
        self.lineEdit_2 = QtWidgets.QLineEdit(Attachment)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 591, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Attachment)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 40, 341, 30))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(Attachment)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 161, 18))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Attachment)
        self.line.setGeometry(QtCore.QRect(0, 150, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(Attachment)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 121, 18))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Attachment)
        self.pushButton.setGeometry(QtCore.QRect(490, 80, 51, 30))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Attachment)
        self.comboBox.setGeometry(QtCore.QRect(180, 80, 301, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")

        self.retranslateUi(Attachment)
        QtCore.QMetaObject.connectSlotsByName(Attachment)


    def Add_ActivityType(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        description = self.lineEdit_3.text()
        code = self.comboBox.currentText()
        deleted = "False"


        self.cur.execute('''
            INSERT INTO ActivityType SET Description=%s ,ActivityTypeGroupID=%s ,Deleted=%s
        ''', (
        description, code, deleted))

        self.db.commit()
        print("Activity Type Add")


    def retranslateUi(self, Attachment):
        _translate = QtCore.QCoreApplication.translate
        Attachment.setWindowTitle(_translate("Attachment", "ProTemp"))
        Attachment.setToolTip(_translate("Attachment", "<html><head/><body><p>Test</p></body></html>"))
        Attachment.setWhatsThis(_translate("Attachment", "<html><head/><body><p>Test</p></body></html>"))
        self.pushButton_6.setText(_translate("Attachment", "Cancel"))
        self.pushButton_6.setShortcut(_translate("Attachment", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("Attachment", "Ok"))
        self.lineEdit_2.setText(_translate("Attachment", "Actvity Type Details"))
        self.label_2.setText(_translate("Attachment", "Activity Type Group:"))
        self.label_3.setText(_translate("Attachment", "Description:"))
        self.pushButton.setText(_translate("Attachment", "F"))
        self.comboBox.setItemText(0, _translate("Attachment", "-1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Attachment = QtWidgets.QWidget()
    ui = Ui_Attachment()
    ui.setupUi(Attachment)
    Attachment.show()
    sys.exit(app.exec_())

