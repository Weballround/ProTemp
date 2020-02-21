#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu November  21 10:41 2019
Updated on Thu November 28 12:40 2019

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
from ActivityTypeGroups_v102 import Ui_ActivityTypeGroups

class Ui_ActivityTypeDetails(object):
    def setupUi(self, ActivityTypeDetails):
        ActivityTypeDetails.setObjectName("ActivityTypeDetails")
        ActivityTypeDetails.resize(591, 207)
        self.pushButton_6 = QtWidgets.QPushButton(ActivityTypeDetails)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 170, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(ActivityTypeDetails)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 170, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Add_ActivityType)
        self.lineEdit_2 = QtWidgets.QLineEdit(ActivityTypeDetails)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 591, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(ActivityTypeDetails)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 40, 341, 30))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(ActivityTypeDetails)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 161, 18))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(ActivityTypeDetails)
        self.line.setGeometry(QtCore.QRect(0, 150, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(ActivityTypeDetails)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 121, 18))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(ActivityTypeDetails)
        self.pushButton.setGeometry(QtCore.QRect(490, 80, 31, 31))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("find-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openWindow1)
        self.comboBox = QtWidgets.QComboBox(ActivityTypeDetails)
        self.comboBox.setGeometry(QtCore.QRect(180, 80, 301, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")

        self.retranslateUi(ActivityTypeDetails)
        QtCore.QMetaObject.connectSlotsByName(ActivityTypeDetails)


    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ActivityTypeGroups()
        self.ui.setupUi(self.window)
        self.window.show()          


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


    def retranslateUi(self, ActivityTypeDetails):
        _translate = QtCore.QCoreApplication.translate
        ActivityTypeDetails.setWindowTitle(_translate("ActivityTypeDetails", "ProTemp Activity Type Details"))
        ActivityTypeDetails.setToolTip(_translate("ActivityTypeDetails", "<html><head/><body><p>Test</p></body></html>"))
        ActivityTypeDetails.setWhatsThis(_translate("ActivityTypeDetails", "<html><head/><body><p>Test</p></body></html>"))
        self.pushButton_6.setText(_translate("ActivityTypeDetails", "Cancel"))
        self.pushButton_6.setShortcut(_translate("ActivityTypeDetails", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("ActivityTypeDetails", "Ok"))
        self.lineEdit_2.setText(_translate("ActivityTypeDetails", "Actvity Type Details"))
        self.label_2.setText(_translate("ActivityTypeDetails", "Activity Type Group:"))
        self.label_3.setText(_translate("ActivityTypeDetails", "Description:"))
        self.comboBox.setItemText(0, _translate("ActivityTypeDetails", "-1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ActivityTypeDetails = QtWidgets.QWidget()
    ui = Ui_ActivityTypeDetails()
    ui.setupUi(ActivityTypeDetails)
    ActivityTypeDetails.show()
    sys.exit(app.exec_())

