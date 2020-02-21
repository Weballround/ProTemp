#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu November  26 11:15 2019

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

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BankDetails(object):
    def setupUi(self, BankDetails):
        BankDetails.setObjectName("BankDetails")
        BankDetails.resize(591, 138)
        self.pushButton_6 = QtWidgets.QPushButton(BankDetails)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 100, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(BankDetails)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 100, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Add_Bank)
        self.lineEdit_2 = QtWidgets.QLineEdit(BankDetails)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 591, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(BankDetails)
        self.lineEdit.setGeometry(QtCore.QRect(180, 40, 341, 30))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(BankDetails)
        self.line.setGeometry(QtCore.QRect(0, 80, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(BankDetails)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 121, 18))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(BankDetails)
        QtCore.QMetaObject.connectSlotsByName(BankDetails)




    def Add_Bank(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        description = self.lineEdit.text()
        Deleted = "False"


        self.cur.execute('''
            INSERT INTO Bank SET Description=%s ,Deleted=%s
        ''', (
        description, Deleted))

        self.db.commit()
        print("Bank Add")


    def retranslateUi(self, BankDetails):
        _translate = QtCore.QCoreApplication.translate
        BankDetails.setWindowTitle(_translate("BankDetails", "ProTemp"))
        BankDetails.setToolTip(_translate("BankDetails", "<html><head/><body><p>Test</p></body></html>"))
        BankDetails.setWhatsThis(_translate("BankDetails", "<html><head/><body><p>Test</p></body></html>"))
        self.pushButton_6.setText(_translate("BankDetails", "Cancel"))
        self.pushButton_6.setShortcut(_translate("BankDetails", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("BankDetails", "Ok"))
        self.lineEdit_2.setText(_translate("BankDetails", "Bank Details"))
        self.label_3.setText(_translate("BankDetails", "Description:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BankDetails = QtWidgets.QWidget()
    ui = Ui_BankDetails()
    ui.setupUi(BankDetails)
    BankDetails.show()
    sys.exit(app.exec_())

