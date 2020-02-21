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

class Ui_DepartmentCategoryDetails(object):
    def setupUi(self, DepartmentCategoryDetails):
        DepartmentCategoryDetails.setObjectName("DepartmentCategoryDetails")
        DepartmentCategoryDetails.resize(591, 138)
        self.pushButton_6 = QtWidgets.QPushButton(DepartmentCategoryDetails)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 100, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(DepartmentCategoryDetails)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 100, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Add_DepartmentCategoryDetails)
        self.lineEdit_2 = QtWidgets.QLineEdit(DepartmentCategoryDetails)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 591, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(DepartmentCategoryDetails)
        self.lineEdit.setGeometry(QtCore.QRect(180, 40, 341, 30))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(DepartmentCategoryDetails)
        self.line.setGeometry(QtCore.QRect(0, 80, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(DepartmentCategoryDetails)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 121, 18))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(DepartmentCategoryDetails)
        QtCore.QMetaObject.connectSlotsByName(DepartmentCategoryDetails)


    def Add_DepartmentCategoryDetails(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        description = self.lineEdit.text()
        Deleted = "False"


        self.cur.execute('''
            INSERT INTO ClientDepartmentCategory SET Description=%s ,Deleted=%s
        ''', (
        description, Deleted))

        self.db.commit()
        print("Department Category Add")


    def retranslateUi(self, DepartmentCategoryDetails):
        _translate = QtCore.QCoreApplication.translate
        DepartmentCategoryDetails.setWindowTitle(_translate("DepartmentCategoryDetails", "ProTemp"))
        DepartmentCategoryDetails.setToolTip(_translate("DepartmentCategoryDetails", "<html><head/><body><p>Test</p></body></html>"))
        DepartmentCategoryDetails.setWhatsThis(_translate("DepartmentCategoryDetails", "<html><head/><body><p>Test</p></body></html>"))
        self.pushButton_6.setText(_translate("DepartmentCategoryDetails", "Cancel"))
        self.pushButton_6.setShortcut(_translate("DepartmentCategoryDetails", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("DepartmentCategoryDetails", "Ok"))
        self.lineEdit_2.setText(_translate("DepartmentCategoryDetails", "Department Category Details"))
        self.label_3.setText(_translate("DepartmentCategoryDetails", "Description:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DepartmentCategoryDetails = QtWidgets.QWidget()
    ui = Ui_DepartmentCategoryDetails()
    ui.setupUi(DepartmentCategoryDetails)
    DepartmentCategoryDetails.show()
    sys.exit(app.exec_())

