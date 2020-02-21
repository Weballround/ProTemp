#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu November  7 10:41 2019

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

class Ui_ActivityTypeGroupDetails(object):
    def setupUi(self, ActivityTypeGroupDetails):
        ActivityTypeGroupDetails.setObjectName("ActivityTypeGroupDetails")
        ActivityTypeGroupDetails.resize(591, 138)
        self.pushButton_6 = QtWidgets.QPushButton(ActivityTypeGroupDetails)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 100, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(ActivityTypeGroupDetails)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 100, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(ActivityTypeGroupDetails)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 591, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(ActivityTypeGroupDetails)
        self.lineEdit.setGeometry(QtCore.QRect(180, 40, 341, 30))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(ActivityTypeGroupDetails)
        self.line.setGeometry(QtCore.QRect(0, 80, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(ActivityTypeGroupDetails)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 121, 18))
        self.label_3.setObjectName("label_3")
        self.Show_ActivityTypeGroups()

        self.retranslateUi(ActivityTypeGroupDetails)
        QtCore.QMetaObject.connectSlotsByName(ActivityTypeGroupDetails)





    def retranslateUi(self, ActivityTypeGroupDetails):
        _translate = QtCore.QCoreApplication.translate
        ActivityTypeGroupDetails.setWindowTitle(_translate("ActivityTypeGroupDetails", "ProTemp"))
        ActivityTypeGroupDetails.setToolTip(_translate("ActivityTypeGroupDetails", "<html><head/><body><p>Test</p></body></html>"))
        ActivityTypeGroupDetails.setWhatsThis(_translate("ActivityTypeGroupDetails", "<html><head/><body><p>Test</p></body></html>"))
        self.pushButton_6.setText(_translate("ActivityTypeGroupDetails", "Cancel"))
        self.pushButton_6.setShortcut(_translate("ActivityTypeGroupDetails", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("ActivityTypeGroupDetails", "Ok"))
        self.lineEdit_2.setText(_translate("ActivityTypeGroupDetails", "Actvity Type Group Details"))
        self.label_3.setText(_translate("ActivityTypeGroupDetails", "Description:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ActivityTypeGroupDetails = QtWidgets.QWidget()
    ui = Ui_ActivityTypeGroupDetails()
    ui.setupUi(ActivityTypeGroupDetails)
    ActivityTypeGroupDetails.show()
    sys.exit(app.exec_())

