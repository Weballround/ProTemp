#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu November  28 14:33 2019

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
from ActivityTypeGroupDetails_v103 import Ui_ActivityTypeGroupDetails    

class Ui_PayingHoursDetails(object):
    def setupUi(self, PayingHoursDetails):
        PayingHoursDetails.setObjectName("PayingHoursDetails")
        PayingHoursDetails.resize(588, 490)
        self.pushButton_6 = QtWidgets.QPushButton(PayingHoursDetails)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 450, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(PayingHoursDetails)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 450, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Add_PayingHours)
        self.lineEdit_2 = QtWidgets.QLineEdit(PayingHoursDetails)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 591, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(PayingHoursDetails)
        self.lineEdit.setGeometry(QtCore.QRect(180, 40, 341, 30))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(PayingHoursDetails)
        self.line.setGeometry(QtCore.QRect(0, 430, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(PayingHoursDetails)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 121, 18))
        self.label_3.setObjectName("label_3")
        self.tabWidget = QtWidgets.QTabWidget(PayingHoursDetails)
        self.tabWidget.setGeometry(QtCore.QRect(0, 80, 591, 351))
        self.tabWidget.setObjectName("tabWidget")
        self.Day = QtWidgets.QWidget()
        self.Day.setObjectName("Day")
        self.tableWidget = QtWidgets.QTableWidget(self.Day)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 581, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tabWidget.addTab(self.Day, "")
        self.Night = QtWidgets.QWidget()
        self.Night.setObjectName("Night")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.Night)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 581, 311))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.tabWidget.addTab(self.Night, "")
        self.Show_PayingHoursDetailDay()
        self.Show_PayingHoursDetailNight()

        self.retranslateUi(PayingHoursDetails)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PayingHoursDetails)


    def Add_PayingHours(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        description = self.lineEdit.text()
        deleted = "False"


        self.cur.execute('''
            INSERT INTO PayingHours SET Description=%s, Deleted=%s
        ''', (
        description, deleted))

        self.db.commit()
        print("Paying Hours Add")        


    def Show_PayingHoursDetailDay(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        sql = ''' SELECT QualificationID, PayingHours FROM PayingHoursDetail '''
        self.cur.execute(sql)
        data = self.cur.fetchall()

        self.tableWidget.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)


    def Show_PayingHoursDetailNight(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        sql = ''' SELECT QualificationID, PayingHours FROM PayingHoursDetail '''
        self.cur.execute(sql)
        data = self.cur.fetchall()

        self.tableWidget_2.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position) 




    def Show_PayingHoursDetails_Night(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        sql = ''' SELECT QualificationID, PayingHours, FROM PayingHoursDetail '''
        self.cur.execute(sql)
        data = self.cur.fetchall()

        self.tableWidget_2.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)          


    def retranslateUi(self, PayingHoursDetails):
        _translate = QtCore.QCoreApplication.translate
        PayingHoursDetails.setWindowTitle(_translate("PayingHoursDetails", "ProTemp"))
        PayingHoursDetails.setToolTip(_translate("PayingHoursDetails", "<html><head/><body><p>Test</p></body></html>"))
        PayingHoursDetails.setWhatsThis(_translate("PayingHoursDetails", "<html><head/><body><p>Test</p></body></html>"))
        self.pushButton_6.setText(_translate("PayingHoursDetails", "Cancel"))
        self.pushButton_6.setShortcut(_translate("PayingHoursDetails", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("PayingHoursDetails", "Ok"))
        self.lineEdit_2.setText(_translate("PayingHoursDetails", "Paying Hours Details"))
        self.label_3.setText(_translate("PayingHoursDetails", "Description:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("PayingHoursDetails", "Qualification"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("PayingHoursDetails", "Hours"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Day), _translate("PayingHoursDetails", "Day"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("PayingHoursDetails", "Qualification"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("PayingHoursDetails", "Hours"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Night), _translate("PayingHoursDetails", "Night"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PayingHoursDetails = QtWidgets.QWidget()
    ui = Ui_PayingHoursDetails()
    ui.setupUi(PayingHoursDetails)
    PayingHoursDetails.show()
    sys.exit(app.exec_())

