#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed December  05 12:28 2019
Lastupdate on Wed December  05 13:51 2019


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


class Ui_ShiftTypeDetails(object):
    def setupUi(self, ShiftTypeDetails):
        ShiftTypeDetails.setObjectName("ShiftTypeDetails")
        ShiftTypeDetails.resize(603, 278)
        self.pushButton_6 = QtWidgets.QPushButton(ShiftTypeDetails)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 240, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(ShiftTypeDetails)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 240, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(ShiftTypeDetails)
        self.lineEdit_2.setGeometry(QtCore.QRect(-10, 0, 641, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(ShiftTypeDetails)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 40, 341, 30))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(ShiftTypeDetails)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 161, 18))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(ShiftTypeDetails)
        self.line.setGeometry(QtCore.QRect(0, 220, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(ShiftTypeDetails)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 121, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ShiftTypeDetails)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 161, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(ShiftTypeDetails)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 161, 18))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(ShiftTypeDetails)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 80, 121, 30))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(ShiftTypeDetails)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 120, 121, 30))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(ShiftTypeDetails)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 160, 121, 30))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.Update_ShiftTypeDetails()

        self.retranslateUi(ShiftTypeDetails)
        QtCore.QMetaObject.connectSlotsByName(ShiftTypeDetails)


    def Update_ShiftTypeDetails(self):
        #ShiftTypeID = '1'
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017', db='medx', use_unicode=True,
                               charset='utf8')
        self.cur = self.db.cursor()

        ShiftTypeID__sql = ''' SELECT Description FROM ShiftTypeID_Workspace '''
        ShiftTypeID_Workspace_test = self.cur.execute(ShiftTypeID__sql)
        data1 = self.cur.fetchone()
        #print(data1[0])
              
        sql = ''' SELECT * FROM ShiftType WHERE Description = %s '''
        self.cur.execute(sql , [(data1)])
        data = self.cur.fetchone()
        #print(data)
        
        self.lineEdit_3.setText(str(data[1]))
        self.lineEdit_4.setText(str(data[2]))
        self.lineEdit_5.setText(str(data[3]))
        self.lineEdit_6.setText(str(data[4]))


        self.db.close()


    def retranslateUi(self, ShiftTypeDetails):
        _translate = QtCore.QCoreApplication.translate
        ShiftTypeDetails.setWindowTitle(_translate("ShiftTypeDetails", "ProTemp Activity Type Details"))
        ShiftTypeDetails.setToolTip(_translate("ShiftTypeDetails", "<html><head/><body><p>Test</p></body></html>"))
        ShiftTypeDetails.setWhatsThis(_translate("ShiftTypeDetails", "<html><head/><body><p>Test</p></body></html>"))
        self.pushButton_6.setText(_translate("ShiftTypeDetails", "Cancel"))
        self.pushButton_6.setShortcut(_translate("ShiftTypeDetails", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("ShiftTypeDetails", "Ok"))
        self.lineEdit_2.setText(_translate("ShiftTypeDetails", "  Shift Type Details"))
        self.label_2.setText(_translate("ShiftTypeDetails", "Unpaid Start:"))
        self.label_3.setText(_translate("ShiftTypeDetails", "Description:"))
        self.label_4.setText(_translate("ShiftTypeDetails", "Start:"))
        self.label_5.setText(_translate("ShiftTypeDetails", "End:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShiftTypeDetails = QtWidgets.QWidget()
    ui = Ui_ShiftTypeDetails()
    ui.setupUi(ShiftTypeDetails)
    ShiftTypeDetails.show()
    sys.exit(app.exec_())

