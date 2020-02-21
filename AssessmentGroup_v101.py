#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri December  06 15:00 2019
Lastupdate on Fri December  06 15:45 2019


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
from Assessment_v101 import Ui_Assessment


class Ui_AssessmentGroup(object):
    def setupUi(self, AssessmentGroup):
        AssessmentGroup.setObjectName("AssessmentGroup")
        AssessmentGroup.resize(812, 570)
        self.pushButton_6 = QtWidgets.QPushButton(AssessmentGroup)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 530, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(AssessmentGroup)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 530, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(AssessmentGroup)
        self.lineEdit_2.setGeometry(QtCore.QRect(-10, 0, 831, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.line = QtWidgets.QFrame(AssessmentGroup)
        self.line.setGeometry(QtCore.QRect(0, 510, 821, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_9 = QtWidgets.QPushButton(AssessmentGroup)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 30, 107, 30))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.openWindow1)
        self.pushButton_11 = QtWidgets.QPushButton(AssessmentGroup)
        self.pushButton_11.setGeometry(QtCore.QRect(250, 30, 107, 30))
        self.pushButton_11.setObjectName("pushButton_11")
        self.tableWidget_2 = QtWidgets.QTableWidget(AssessmentGroup)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 60, 811, 451))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.pushButton_10 = QtWidgets.QPushButton(AssessmentGroup)
        self.pushButton_10.setGeometry(QtCore.QRect(130, 30, 107, 30))
        self.pushButton_10.setObjectName("pushButton_10")
        self.Show_Modules()

        self.retranslateUi(AssessmentGroup)
        QtCore.QMetaObject.connectSlotsByName(AssessmentGroup)


    def openWindow1(self):
        self.window1 = QtWidgets.QMainWindow()
        self.ui1 = Ui_Assessment()
        self.ui1.setupUi(self.window1)
        self.window1.show()                  


    def Show_Modules(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        sql = ''' SELECT Question, MethodId FROM ModuleAssessmentQuestion '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        print(data)

        self.tableWidget_2.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)
                    

    def retranslateUi(self, AssessmentGroup):
        _translate = QtCore.QCoreApplication.translate
        AssessmentGroup.setWindowTitle(_translate("AssessmentGroup", "ProTemp Assessment Group"))
        AssessmentGroup.setToolTip(_translate("AssessmentGroup", "<html><head/><body><p>Test</p></body></html>"))
        AssessmentGroup.setWhatsThis(_translate("AssessmentGroup", "<html><head/><body><p>Test</p></body></html>"))
        self.pushButton_6.setText(_translate("AssessmentGroup", "Cancel"))
        self.pushButton_6.setShortcut(_translate("AssessmentGroup", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("AssessmentGroup", "Ok"))
        self.lineEdit_2.setText(_translate("AssessmentGroup", "  Assessment Group"))
        self.pushButton_9.setText(_translate("AssessmentGroup", "Add"))
        self.pushButton_11.setText(_translate("AssessmentGroup", "Delete"))
        self.pushButton_11.setShortcut(_translate("AssessmentGroup", "Ctrl+Q"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("AssessmentGroup", "Question"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("AssessmentGroup", "Method"))
        self.pushButton_10.setText(_translate("AssessmentGroup", "Update"))
        self.pushButton_10.setShortcut(_translate("AssessmentGroup", "Ctrl+Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AssessmentGroup = QtWidgets.QWidget()
    ui = Ui_AssessmentGroup()
    ui.setupUi(AssessmentGroup)
    AssessmentGroup.show()
    sys.exit(app.exec_())

