#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu December  05 15:28 2019
Lastupdate on Thu December  05 16:15 2019


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

from AssessmentGroup_v101 import Ui_AssessmentGroup


class Ui_Modules(object):
    def setupUi(self, Modules):
        Modules.setObjectName("Modules")
        Modules.resize(822, 610)
        self.pushButton_6 = QtWidgets.QPushButton(Modules)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 570, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(Modules)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 570, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(Modules)
        self.lineEdit_2.setGeometry(QtCore.QRect(-10, 0, 831, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.line = QtWidgets.QFrame(Modules)
        self.line.setGeometry(QtCore.QRect(0, 550, 821, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget = QtWidgets.QTabWidget(Modules)
        self.tabWidget.setGeometry(QtCore.QRect(0, 30, 821, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 0, 107, 30))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.openWindow1)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab)
        self.pushButton_10.setGeometry(QtCore.QRect(130, 0, 107, 30))
        self.pushButton_10.setObjectName("pushButton_10")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 30, 811, 451))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab)
        self.pushButton_11.setGeometry(QtCore.QRect(250, 0, 107, 30))
        self.pushButton_11.setObjectName("pushButton_11")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 30, 811, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(130, 0, 107, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 0, 107, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_12.setGeometry(QtCore.QRect(370, 0, 107, 30))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_13.setGeometry(QtCore.QRect(250, 0, 107, 30))
        self.pushButton_13.setObjectName("pushButton_13")
        self.tabWidget.addTab(self.tab_2, "")
        self.Show_Assessment()

        self.retranslateUi(Modules)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Modules)


    def openWindow1(self):
        self.window1 = QtWidgets.QMainWindow()
        self.ui1 = Ui_AssessmentGroup()
        self.ui1.setupUi(self.window1)
        self.window1.show()              


    def Add_Attachments(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        CourseName = self.lineEdit_3.text()
        CourseCode = self.lineEdit_4.text()
        CourseDuration = self.lineEdit_5.text()
        CourseContent = self.lineEdit_6.text()


        self.cur.execute('''
            INSERT INTO Training SET CourseName=%s, CourseCode=%s, CourseDuration=%s, CourseContent=%s
        ''', (
        CourseName, CourseCode, CourseDuration, CourseContent))

        self.db.commit()
        print("Course Details Add")          
        


    def Show_Assessment(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        sql = ''' SELECT Description FROM Module '''
        self.cur.execute(sql)
        data = self.cur.fetchall()

        self.tableWidget_2.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)


    def retranslateUi(self, Modules):
        _translate = QtCore.QCoreApplication.translate
        Modules.setWindowTitle(_translate("Modules", "ProTemp Modules"))
        Modules.setToolTip(_translate("Modules", "<html><head/><body><p>Test</p></body></html>"))
        Modules.setWhatsThis(_translate("Modules", "<html><head/><body><p>Test</p></body></html>"))
        self.pushButton_6.setText(_translate("Modules", "Cancel"))
        self.pushButton_6.setShortcut(_translate("Modules", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("Modules", "Ok"))
        self.lineEdit_2.setText(_translate("Modules", "  Modules"))
        self.pushButton_9.setText(_translate("Modules", "Add"))
        self.pushButton_10.setText(_translate("Modules", "Update"))
        self.pushButton_10.setShortcut(_translate("Modules", "Ctrl+Q"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Modules", "Description"))
        self.pushButton_11.setText(_translate("Modules", "Delete"))
        self.pushButton_11.setShortcut(_translate("Modules", "Ctrl+Q"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Modules", "Assessment"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Modules", "FileName"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Modules", "Description"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Modules", "Modified Date"))
        self.pushButton_7.setText(_translate("Modules", "Update"))
        self.pushButton_7.setShortcut(_translate("Modules", "Ctrl+Q"))
        self.pushButton_8.setText(_translate("Modules", "Add"))
        self.pushButton_12.setText(_translate("Modules", "Open"))
        self.pushButton_12.setShortcut(_translate("Modules", "Ctrl+Q"))
        self.pushButton_13.setText(_translate("Modules", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Modules", "Attachments"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Modules = QtWidgets.QWidget()
    ui = Ui_Modules()
    ui.setupUi(Modules)
    Modules.show()
    sys.exit(app.exec_())

