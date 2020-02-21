#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri December  06 09:30 2019
Lastupdate on Mon December  09 13:45 2019


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

class Ui_Invoice(object):
    def setupUi(self, Invoice):
        Invoice.setObjectName("Invoice")
        Invoice.resize(1319, 697)
        self.pushButton_6 = QtWidgets.QPushButton(Invoice)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 660, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(Invoice)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 660, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(Invoice)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 1331, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(Invoice)
        self.lineEdit.setGeometry(QtCore.QRect(150, 40, 1121, 30))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Invoice)
        self.label.setGeometry(QtCore.QRect(20, 50, 131, 18))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Invoice)
        self.line.setGeometry(QtCore.QRect(0, 640, 1331, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget = QtWidgets.QTabWidget(Invoice)
        self.tabWidget.setGeometry(QtCore.QRect(20, 70, 1291, 581))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1281, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(1170, 450, 113, 32))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(1170, 480, 113, 32))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(1170, 510, 113, 32))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(1090, 460, 74, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(1090, 490, 74, 18))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(1090, 520, 74, 18))
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(140, 10, 1131, 41))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(140, 50, 1131, 41))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 101, 18))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 101, 18))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton = QtWidgets.QPushButton(Invoice)
        self.pushButton.setGeometry(QtCore.QRect(1280, 40, 31, 34))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Invoice)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Invoice)


    def Add_Template(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        Description = self.lineEdit.text()
        #ActiveplainTextEdit = self.plainTextEdit.currentText()
        #Template = self.plainTextEdit.appendPlainText(str())
        TemplateCategoryId = 1
        Deleted = 'False'


        self.cur.execute('''
            INSERT INTO Template SET Description=%s, TemplateCategoryId=%s, Deleted=%s
        ''', (
        Description, TemplateCategoryId, Deleted))

        self.db.commit()
        print("Template Add")    


    def retranslateUi(self, Invoice):
        _translate = QtCore.QCoreApplication.translate
        Invoice.setWindowTitle(_translate("Invoice", "Invoice"))
        self.pushButton_6.setText(_translate("Invoice", "Cancel"))
        self.pushButton_5.setText(_translate("Invoice", "Ok"))
        self.lineEdit_2.setText(_translate("Invoice", " Invoice (Open)"))
        self.label.setText(_translate("Invoice", "Company Name:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Invoice", "Description"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Invoice", "Amount"))
        self.label_4.setText(_translate("Invoice", "<html><head/><body><p align=\"right\">Subtotal:</p></body></html>"))
        self.label_5.setText(_translate("Invoice", "<html><head/><body><p align=\"right\">VAT:</p></body></html>"))
        self.label_6.setText(_translate("Invoice", "<html><head/><body><p align=\"right\">Total:</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Invoice", "Details"))
        self.plainTextEdit.setPlainText(_translate("Invoice", "Please pay invoice within 30 days from Invoice date to prevent an interest charge of 2% per month"))
        self.plainTextEdit_2.setPlainText(_translate("Invoice", "EFFEKTIEWE VERPLEEGSORG ONS TROTS EFFECTIVE / NURSING CARE OUR PRIDE"))
        self.label_3.setText(_translate("Invoice", "Footer Note:"))
        self.label_2.setText(_translate("Invoice", "Header Note:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Invoice", "Header / Footer"))
        self.pushButton.setText(_translate("Invoice", "?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Invoice = QtWidgets.QWidget()
    ui = Ui_Invoice()
    ui.setupUi(Invoice)
    Invoice.show()
    sys.exit(app.exec_())

