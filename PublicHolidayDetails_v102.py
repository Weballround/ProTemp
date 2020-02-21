#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed December  04 08:42 2019
Lastupdate on Wed December  04 08:49 2019


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
from PyQt5.QtCore import Qt, QModelIndex, QDate
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, \
    QTableWidget, QTableWidgetItem, QMessageBox, QHBoxLayout, QLineEdit, QLabel, QGridLayout, QHeaderView


class Ui_PublicHolidayDetails(object):
    def setupUi(self, PublicHolidayDetails):
        PublicHolidayDetails.setObjectName("PublicHolidayDetails")
        PublicHolidayDetails.resize(591, 207)
        self.pushButton_6 = QtWidgets.QPushButton(PublicHolidayDetails)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 170, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(PublicHolidayDetails)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 170, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Add_PublicHolidayDetails)
        self.lineEdit_2 = QtWidgets.QLineEdit(PublicHolidayDetails)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 591, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(PublicHolidayDetails)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 80, 341, 30))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(PublicHolidayDetails)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 161, 18))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(PublicHolidayDetails)
        self.line.setGeometry(QtCore.QRect(0, 150, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(PublicHolidayDetails)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 121, 18))
        self.label_3.setObjectName("label_3")
        now = QDate.currentDate()
        self.dateEdit = QtWidgets.QDateEdit(PublicHolidayDetails)
        self.dateEdit.setGeometry(QtCore.QRect(180, 40, 171, 32))
        self.dateEdit.setDate(QtCore.QDate(now))
        self.dateEdit.setObjectName("dateEdit")

        self.retranslateUi(PublicHolidayDetails)
        QtCore.QMetaObject.connectSlotsByName(PublicHolidayDetails)


    def Add_PublicHolidayDetails(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        PublicHolidayID = self.dateEdit.text()
        Description = self.lineEdit_3.text()
        deleted = "False"
        

        self.cur.execute('''
            INSERT INTO PublicHoliday SET PublicHolidayID=%s, Description=%s
        ''', (
        PublicHolidayID, Description))

        self.db.commit()
        print("Public Holiday Details Add")  


    def retranslateUi(self, PublicHolidayDetails):
        _translate = QtCore.QCoreApplication.translate
        PublicHolidayDetails.setWindowTitle(_translate("PublicHolidayDetails", "ProTemp Activity Type Details"))
        PublicHolidayDetails.setToolTip(_translate("PublicHolidayDetails", "<html><head/><body><p>Test</p></body></html>"))
        PublicHolidayDetails.setWhatsThis(_translate("PublicHolidayDetails", "<html><head/><body><p>Test</p></body></html>"))
        self.pushButton_6.setText(_translate("PublicHolidayDetails", "Cancel"))
        self.pushButton_6.setShortcut(_translate("PublicHolidayDetails", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("PublicHolidayDetails", "Ok"))
        self.lineEdit_2.setText(_translate("PublicHolidayDetails", "Public Holiday Details"))
        self.label_2.setText(_translate("PublicHolidayDetails", "Date:"))
        self.label_3.setText(_translate("PublicHolidayDetails", "Description:"))
        self.dateEdit.setDisplayFormat(_translate("PublicHolidayDetails", "yyyy/MM/dd"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PublicHolidayDetails = QtWidgets.QWidget()
    ui = Ui_PublicHolidayDetails()
    ui.setupUi(PublicHolidayDetails)
    PublicHolidayDetails.show()
    sys.exit(app.exec_())

