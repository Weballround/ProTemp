#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed December  05 10:28 2019
Lastupdate on Wed December  05 10:51 2019


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


class Ui_ShiftDetails(object):
    def setupUi(self, ShiftDetails):
        ShiftDetails.setObjectName("ShiftDetails")
        ShiftDetails.resize(597, 185)
        self.pushButton_6 = QtWidgets.QPushButton(ShiftDetails)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 150, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(ShiftDetails)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 150, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(ShiftDetails)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 611, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(ShiftDetails)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 40, 341, 30))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(ShiftDetails)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 161, 18))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(ShiftDetails)
        self.line.setGeometry(QtCore.QRect(0, 130, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(ShiftDetails)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 121, 18))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(ShiftDetails)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 80, 121, 30))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.Update_ShiftDetails()

        self.retranslateUi(ShiftDetails)
        QtCore.QMetaObject.connectSlotsByName(ShiftDetails)


    def Update_ShiftDetails(self):
        ShiftID = '1'
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017', db='medx', use_unicode=True,
                               charset='utf8')
        self.cur = self.db.cursor()
              
              
        sql = ''' SELECT * FROM Shift WHERE ShiftID = %s '''
        self.cur.execute(sql , [(ShiftID)])
        data = self.cur.fetchone()
        #print(data)
        
        self.lineEdit_3.setText(str(data[2]))
        self.lineEdit_4.setText(str(data[3]))


        self.db.close()


    def retranslateUi(self, ShiftDetails):
        _translate = QtCore.QCoreApplication.translate
        ShiftDetails.setWindowTitle(_translate("ShiftDetails", "ProTemp Activity Type Details"))
        ShiftDetails.setToolTip(_translate("ShiftDetails", "<html><head/><body><p>Test</p></body></html>"))
        ShiftDetails.setWhatsThis(_translate("ShiftDetails", "<html><head/><body><p>Test</p></body></html>"))
        self.pushButton_6.setText(_translate("ShiftDetails", "Cancel"))
        self.pushButton_6.setShortcut(_translate("ShiftDetails", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("ShiftDetails", "Ok"))
        self.lineEdit_2.setText(_translate("ShiftDetails", "Shift Details"))
        self.label_2.setText(_translate("ShiftDetails", "Hours In Shift:"))
        self.label_3.setText(_translate("ShiftDetails", "Description:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShiftDetails = QtWidgets.QWidget()
    ui = Ui_ShiftDetails()
    ui.setupUi(ShiftDetails)
    ShiftDetails.show()
    sys.exit(app.exec_())

