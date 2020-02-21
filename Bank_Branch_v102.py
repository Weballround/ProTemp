#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue November  26 12:16 2019

Last Update Tue November  26 12:33 2019

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

class Ui_BankBranch(object):
    def setupUi(self, BankBranch):
        BankBranch.setObjectName("BankBranch")
        BankBranch.resize(591, 207)
        self.pushButton_6 = QtWidgets.QPushButton(BankBranch)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 170, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(BankBranch)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 170, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Add_BankBranch)
        self.lineEdit_2 = QtWidgets.QLineEdit(BankBranch)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 591, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(BankBranch)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 80, 341, 30))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(BankBranch)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 161, 18))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(BankBranch)
        self.line.setGeometry(QtCore.QRect(0, 150, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(BankBranch)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 121, 18))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(BankBranch)
        self.comboBox.setGeometry(QtCore.QRect(180, 40, 301, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(BankBranch)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 121, 18))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(BankBranch)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 120, 341, 30))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.List_Bank()

        self.retranslateUi(BankBranch)
        QtCore.QMetaObject.connectSlotsByName(BankBranch)


    def List_Bank(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017', db='medx', use_unicode=True,
                               charset='utf8')
        self.cur = self.db.cursor()
              
        self.cur.execute(''' SELECT Description From Bank ''')
        data = self.cur.fetchall()
        
        for bank in data :
            self.comboBox.addItem(bank[0])        


    def Add_BankBranch(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        description = self.lineEdit_3.text()
        BankID = self.comboBox.currentText()
        Code = self.lineEdit_4.text()
        deleted = "False"
        BankBranchID = "1"


        self.cur.execute('''
            INSERT INTO BankBranch SET BankBranchID=%s ,Description=%s ,BankID=%s ,Code=%s ,Deleted=%s
        ''', (
        BankBranchID,description, BankID, Code, deleted))

        self.db.commit()
        print("Bank Branch Add")


    def retranslateUi(self, BankBranch):
        _translate = QtCore.QCoreApplication.translate
        BankBranch.setWindowTitle(_translate("BankBranch", "ProTemp Activity Type Details"))
        BankBranch.setToolTip(_translate("BankBranch", "<html><head/><body><p>Test</p></body></html>"))
        BankBranch.setWhatsThis(_translate("BankBranch", "<html><head/><body><p>Test</p></body></html>"))
        self.pushButton_6.setText(_translate("BankBranch", "Cancel"))
        self.pushButton_6.setShortcut(_translate("BankBranch", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("BankBranch", "Ok"))
        self.lineEdit_2.setText(_translate("BankBranch", "Bank Branch Details"))
        self.label_2.setText(_translate("BankBranch", "Bank:"))
        self.label_3.setText(_translate("BankBranch", "Description:"))
        self.comboBox.setItemText(0, _translate("BankBranch", "Select Bank"))
        self.label_4.setText(_translate("BankBranch", "Code:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BankBranch = QtWidgets.QWidget()
    ui = Ui_BankBranch()
    ui.setupUi(BankBranch)
    BankBranch.show()
    sys.exit(app.exec_())

