#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue November  26 14:30 2019


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
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QVBoxLayout, QPushButton, \
    QTableWidget, QTableWidgetItem, QMessageBox, QHBoxLayout, QLineEdit, QLabel, QGridLayout, QHeaderView

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CandidateCategoryDetails(object):
    def setupUi(self, CandidateCategoryDetails):
        CandidateCategoryDetails.setObjectName("CandidateCategoryDetails")
        CandidateCategoryDetails.resize(591, 191)
        self.pushButton_6 = QtWidgets.QPushButton(CandidateCategoryDetails)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 150, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(CandidateCategoryDetails)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 150, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Add_CandidateCategoryDetails)
        self.lineEdit_2 = QtWidgets.QLineEdit(CandidateCategoryDetails)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 591, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(CandidateCategoryDetails)
        self.lineEdit.setGeometry(QtCore.QRect(180, 40, 341, 30))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(CandidateCategoryDetails)
        self.line.setGeometry(QtCore.QRect(0, 130, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(CandidateCategoryDetails)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 121, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(CandidateCategoryDetails)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 161, 18))
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(CandidateCategoryDetails)
        self.checkBox.setGeometry(QtCore.QRect(180, 90, 103, 22))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.clickBox)

        self.retranslateUi(CandidateCategoryDetails)
        QtCore.QMetaObject.connectSlotsByName(CandidateCategoryDetails)


    def clickBox(self, state):

        if state == QtCore.Qt.Checked:
            IsNursingCategory = 'True'
        else:
            IsNursingCategory = 'False'

        print(IsNursingCategory)


    def Add_CandidateCategoryDetails(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        description = self.lineEdit.text()
        print(IsNursingCategory)
        IsNursingCategory = clickBox.IsNursingCategory
        Deleted = "False"


        self.cur.execute('''
            INSERT INTO CandidateCategory SET Description=%s ,IsNursingCategory=%s ,Deleted=%s
        ''', (
        description, IsNursingCategory, Deleted))

        self.db.commit()
        print("Candidate Category Add")


    def retranslateUi(self, CandidateCategoryDetails):
        _translate = QtCore.QCoreApplication.translate
        CandidateCategoryDetails.setWindowTitle(_translate("CandidateCategoryDetails", "ProTemp"))
        CandidateCategoryDetails.setToolTip(_translate("CandidateCategoryDetails", "<html><head/><body><p>Test</p></body></html>"))
        CandidateCategoryDetails.setWhatsThis(_translate("CandidateCategoryDetails", "<html><head/><body><p>Test</p></body></html>"))
        self.pushButton_6.setText(_translate("CandidateCategoryDetails", "Cancel"))
        self.pushButton_6.setShortcut(_translate("CandidateCategoryDetails", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("CandidateCategoryDetails", "Ok"))
        self.lineEdit_2.setText(_translate("CandidateCategoryDetails", "Candidate Category Details"))
        self.label_3.setText(_translate("CandidateCategoryDetails", "Description:"))
        self.label_4.setText(_translate("CandidateCategoryDetails", "Is Nursing Category:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CandidateCategoryDetails = QtWidgets.QWidget()
    ui = Ui_CandidateCategoryDetails()
    ui.setupUi(CandidateCategoryDetails)
    CandidateCategoryDetails.show()
    sys.exit(app.exec_())

