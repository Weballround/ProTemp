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

class Ui_Training(object):
    def setupUi(self, Training):
        Training.setObjectName("Training")
        Training.resize(822, 610)
        self.pushButton_6 = QtWidgets.QPushButton(Training)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 570, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(Training)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 570, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Add_Course)
        self.lineEdit_2 = QtWidgets.QLineEdit(Training)
        self.lineEdit_2.setGeometry(QtCore.QRect(-10, 0, 831, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.line = QtWidgets.QFrame(Training)
        self.line.setGeometry(QtCore.QRect(0, 550, 821, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget = QtWidgets.QTabWidget(Training)
        self.tabWidget.setGeometry(QtCore.QRect(0, 30, 821, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 128, 131, 20))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 111, 18))
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 80, 601, 30))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(170, 120, 601, 361))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 0, 601, 30))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 40, 601, 30))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 121, 18))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 131, 18))
        self.label_2.setObjectName("label_2")
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
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Training)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Training)


    def Add_Course(self):
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
        


    def Show_Modules(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        sql = ''' SELECT Description FROM Function '''
        self.cur.execute(sql)
        data = self.cur.fetchall()

        self.tableWidget.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)



    def retranslateUi(self, Training):
        _translate = QtCore.QCoreApplication.translate
        Training.setWindowTitle(_translate("Training", "ProTemp Activity Type Details"))
        Training.setToolTip(_translate("Training", "<html><head/><body><p>Test</p></body></html>"))
        Training.setWhatsThis(_translate("Training", "<html><head/><body><p>Test</p></body></html>"))
        self.pushButton_6.setText(_translate("Training", "Cancel"))
        self.pushButton_6.setShortcut(_translate("Training", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("Training", "Ok"))
        self.lineEdit_2.setText(_translate("Training", "  Training"))
        self.label_5.setText(_translate("Training", "Course Content:"))
        self.label_4.setText(_translate("Training", "Duration:"))
        self.label_3.setText(_translate("Training", "Course Name:"))
        self.label_2.setText(_translate("Training", "Course Code:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Training", "General"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Training", "Module"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Training", "Module Id"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Training", "Module Description"))
        self.pushButton_7.setText(_translate("Training", "Delete"))
        self.pushButton_7.setShortcut(_translate("Training", "Ctrl+Q"))
        self.pushButton_8.setText(_translate("Training", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Training", "Modules"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Training = QtWidgets.QWidget()
    ui = Ui_Training()
    ui.setupUi(Training)
    Training.show()
    sys.exit(app.exec_())

