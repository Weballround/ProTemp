#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon December  09 09:10 2019
Lastupdate on Mon December  09 10:45 2019


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
    QTableWidget, QTableWidgetItem, QMessageBox, QHBoxLayout, QLineEdit, QLabel, QGridLayout, QHeaderView, QPlainTextEdit

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SmsTemplate(object):
    def setupUi(self, SmsTemplate):
        SmsTemplate.setObjectName("SmsTemplate")
        SmsTemplate.resize(587, 329)
        self.pushButton_6 = QtWidgets.QPushButton(SmsTemplate)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 280, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(SmsTemplate)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 280, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Add_SmsTemplate)
        self.lineEdit_2 = QtWidgets.QLineEdit(SmsTemplate)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 591, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(SmsTemplate)
        self.lineEdit.setGeometry(QtCore.QRect(130, 50, 421, 30))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(SmsTemplate)
        self.label.setGeometry(QtCore.QRect(20, 60, 101, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(SmsTemplate)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 81, 18))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(SmsTemplate)
        self.line.setGeometry(QtCore.QRect(0, 260, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.comboBox = QtWidgets.QComboBox(SmsTemplate)
        self.comboBox.setGeometry(QtCore.QRect(130, 90, 301, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_7 = QtWidgets.QPushButton(SmsTemplate)
        self.pushButton_7.setGeometry(QtCore.QRect(440, 90, 107, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.Add_comboBox_plainTextEdit)
        self.label_3 = QtWidgets.QLabel(SmsTemplate)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 81, 18))
        self.label_3.setObjectName("label_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(SmsTemplate)
        self.plainTextEdit.setGeometry(QtCore.QRect(130, 140, 421, 111))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_4 = QtWidgets.QLabel(SmsTemplate)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 45, 18))
        self.label_4.setObjectName("label_4")
        self.line_2 = QtWidgets.QFrame(SmsTemplate)
        self.line_2.setGeometry(QtCore.QRect(60, 30, 531, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_6.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.line.raise_()
        self.comboBox.raise_()
        self.pushButton_7.raise_()
        self.label_3.raise_()
        self.plainTextEdit.raise_()
        self.label_4.raise_()
        self.line_2.raise_()
        self.pushButton_5.raise_()

        self.retranslateUi(SmsTemplate)
        QtCore.QMetaObject.connectSlotsByName(SmsTemplate)


    def Add_comboBox_plainTextEdit(self):
        ActiveComboBox = self.comboBox.currentText()
        print(ActiveComboBox)
        ActivedBox = self.plainTextEdit.insertPlainText(ActiveComboBox)


    def Add_SmsTemplate(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        Description = self.lineEdit.text()
        #ActiveplainTextEdit = self.plainTextEdit.currentText()
        Template = self.plainTextEdit.appendPlainText(str())
        Deleted = 'False'


        self.cur.execute('''
            INSERT INTO SmsTemplate SET Description=%s, Template=%s, Deleted=%s
        ''', (
        Description, Template, Deleted))

        self.db.commit()
        print("SmsTemplate Add")        


    def retranslateUi(self, SmsTemplate):
        _translate = QtCore.QCoreApplication.translate
        SmsTemplate.setWindowTitle(_translate("SmsTemplate", "Sms Template"))
        self.pushButton_6.setText(_translate("SmsTemplate", "Cancel"))
        self.pushButton_5.setText(_translate("SmsTemplate", "Ok"))
        self.lineEdit_2.setText(_translate("SmsTemplate", " Sms Template"))
        self.label.setText(_translate("SmsTemplate", "Description:"))
        self.label_2.setText(_translate("SmsTemplate", "Tags:"))
        self.comboBox.setItemText(0, _translate("SmsTemplate", "<<First_Name>>"))
        self.comboBox.setItemText(1, _translate("SmsTemplate", "<<Last_Name>>"))
        self.comboBox.setItemText(2, _translate("SmsTemplate", "<<ID_Number>>"))
        self.comboBox.setItemText(3, _translate("SmsTemplate", "<<SANC_Receipt_Number>>"))
        self.comboBox.setItemText(4, _translate("SmsTemplate", "<<Date_Of_Birth>>"))
        self.comboBox.setItemText(5, _translate("SmsTemplate", "<<Cellphone_Number>>"))
        self.pushButton_7.setText(_translate("SmsTemplate", "Insert"))
        self.label_3.setText(_translate("SmsTemplate", "Template:"))
        self.label_4.setText(_translate("SmsTemplate", "<html><head/><body><p><span style=\" color:#0000ff;\">Setup</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SmsTemplate = QtWidgets.QWidget()
    ui = Ui_SmsTemplate()
    ui.setupUi(SmsTemplate)
    SmsTemplate.show()
    sys.exit(app.exec_())

