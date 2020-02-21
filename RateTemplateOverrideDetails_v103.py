#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed December  04 13:28 2019
Lastupdate on Wed December  04 13:28 2019


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


class Ui_RateTemplateOverrideDetails(object):
    def setupUi(self, RateTemplateOverrideDetails):
        RateTemplateOverrideDetails.setObjectName("RateTemplateOverrideDetails")
        RateTemplateOverrideDetails.resize(1167, 599)
        self.pushButton_6 = QtWidgets.QPushButton(RateTemplateOverrideDetails)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 550, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(RateTemplateOverrideDetails)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 550, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Add_RateTemplateOverrideDetails)
        self.lineEdit_2 = QtWidgets.QLineEdit(RateTemplateOverrideDetails)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 1171, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 131, 18))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(RateTemplateOverrideDetails)
        self.line.setGeometry(QtCore.QRect(0, 530, 1171, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 121, 18))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(RateTemplateOverrideDetails)
        self.pushButton.setGeometry(QtCore.QRect(480, 80, 31, 31))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("find-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(RateTemplateOverrideDetails)
        self.comboBox.setGeometry(QtCore.QRect(170, 80, 301, 32))
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_4.setGeometry(QtCore.QRect(590, 90, 121, 18))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(RateTemplateOverrideDetails)
        self.pushButton_2.setGeometry(QtCore.QRect(1060, 80, 31, 31))
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_2 = QtWidgets.QComboBox(RateTemplateOverrideDetails)
        self.comboBox_2.setGeometry(QtCore.QRect(750, 80, 301, 32))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_5 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_5.setGeometry(QtCore.QRect(590, 50, 121, 18))
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(RateTemplateOverrideDetails)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 40, 31, 31))
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(RateTemplateOverrideDetails)
        self.pushButton_4.setGeometry(QtCore.QRect(1100, 40, 31, 31))
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(RateTemplateOverrideDetails)
        self.pushButton_7.setGeometry(QtCore.QRect(520, 80, 31, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(RateTemplateOverrideDetails)
        self.pushButton_8.setGeometry(QtCore.QRect(1100, 80, 31, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.lineEdit = QtWidgets.QLineEdit(RateTemplateOverrideDetails)
        self.lineEdit.setGeometry(QtCore.QRect(422, 140, 131, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label.setGeometry(QtCore.QRect(10, 150, 141, 18))
        self.label.setObjectName("label")
        self.lineEdit_5 = QtWidgets.QLineEdit(RateTemplateOverrideDetails)
        self.lineEdit_5.setGeometry(QtCore.QRect(422, 180, 131, 32))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_6.setGeometry(QtCore.QRect(10, 190, 291, 18))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(RateTemplateOverrideDetails)
        self.lineEdit_6.setGeometry(QtCore.QRect(1002, 180, 131, 32))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(RateTemplateOverrideDetails)
        self.lineEdit_7.setGeometry(QtCore.QRect(1002, 140, 131, 32))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_7 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_7.setGeometry(QtCore.QRect(590, 150, 151, 18))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_8.setGeometry(QtCore.QRect(590, 190, 301, 18))
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(RateTemplateOverrideDetails)
        self.lineEdit_8.setGeometry(QtCore.QRect(1002, 280, 131, 32))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(RateTemplateOverrideDetails)
        self.lineEdit_9.setGeometry(QtCore.QRect(422, 280, 131, 32))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(RateTemplateOverrideDetails)
        self.lineEdit_10.setGeometry(QtCore.QRect(422, 240, 131, 32))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_9 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_9.setGeometry(QtCore.QRect(590, 250, 151, 18))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_10.setGeometry(QtCore.QRect(10, 250, 151, 18))
        self.label_10.setObjectName("label_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(RateTemplateOverrideDetails)
        self.lineEdit_11.setGeometry(QtCore.QRect(1002, 240, 131, 32))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_11 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_11.setGeometry(QtCore.QRect(10, 290, 291, 18))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_12.setGeometry(QtCore.QRect(590, 290, 301, 18))
        self.label_12.setObjectName("label_12")
        self.lineEdit_12 = QtWidgets.QLineEdit(RateTemplateOverrideDetails)
        self.lineEdit_12.setGeometry(QtCore.QRect(1000, 480, 131, 32))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(RateTemplateOverrideDetails)
        self.lineEdit_13.setGeometry(QtCore.QRect(1000, 380, 131, 32))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(RateTemplateOverrideDetails)
        self.lineEdit_14.setGeometry(QtCore.QRect(420, 380, 131, 32))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(RateTemplateOverrideDetails)
        self.lineEdit_15.setGeometry(QtCore.QRect(420, 440, 131, 32))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(RateTemplateOverrideDetails)
        self.lineEdit_16.setGeometry(QtCore.QRect(420, 340, 131, 32))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_13 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_13.setGeometry(QtCore.QRect(588, 350, 151, 18))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_14.setGeometry(QtCore.QRect(8, 350, 141, 18))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_15.setGeometry(QtCore.QRect(588, 490, 351, 18))
        self.label_15.setObjectName("label_15")
        self.lineEdit_17 = QtWidgets.QLineEdit(RateTemplateOverrideDetails)
        self.lineEdit_17.setGeometry(QtCore.QRect(1000, 340, 131, 32))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_16 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_16.setGeometry(QtCore.QRect(8, 390, 291, 18))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_17.setGeometry(QtCore.QRect(8, 490, 341, 18))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_18.setGeometry(QtCore.QRect(588, 390, 301, 18))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_19.setGeometry(QtCore.QRect(8, 450, 191, 18))
        self.label_19.setObjectName("label_19")
        self.lineEdit_18 = QtWidgets.QLineEdit(RateTemplateOverrideDetails)
        self.lineEdit_18.setGeometry(QtCore.QRect(1000, 440, 131, 32))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_20 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_20.setGeometry(QtCore.QRect(588, 450, 211, 18))
        self.label_20.setObjectName("label_20")
        self.lineEdit_19 = QtWidgets.QLineEdit(RateTemplateOverrideDetails)
        self.lineEdit_19.setGeometry(QtCore.QRect(420, 480, 131, 32))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_21 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_21.setGeometry(QtCore.QRect(590, 550, 561, 21))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(RateTemplateOverrideDetails)
        self.label_22.setGeometry(QtCore.QRect(590, 570, 561, 21))
        self.label_22.setObjectName("label_22")
        self.comboBox_3 = QtWidgets.QComboBox(RateTemplateOverrideDetails)
        self.comboBox_3.setGeometry(QtCore.QRect(170, 40, 341, 32))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(RateTemplateOverrideDetails)
        self.comboBox_4.setGeometry(QtCore.QRect(750, 40, 341, 32))
        self.comboBox_4.setObjectName("comboBox_4")
        self.pushButton_2.clicked.connect(self.Client_Combobox)
        self.pushButton_3.clicked.connect(self.Client_Combobox)
        self.pushButton_4.clicked.connect(self.Candidate_Combobox)
        self.pushButton.clicked.connect(self.Department_Combobox)
        #self.pushButton_5.clicked.connect(self.Add_RateTemplateOverrideDetails)
        #self.Candidate_Show_Qualifications()
        self.Department_Combobox()
        #self.Client_Combobox()

        self.retranslateUi(RateTemplateOverrideDetails)
        QtCore.QMetaObject.connectSlotsByName(RateTemplateOverrideDetails)


#Who
    def Candidate_Combobox(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017', db='medx', use_unicode=True,
                               charset='utf8')
        self.cur = self.db.cursor()
              
        self.cur.execute(''' SELECT CONCAT(CandidateID, ", ",FirstName, ", ",LastName) AS FullName from Candidate_live''')
        data = self.cur.fetchall()
        
        for candidate in data :
            self.comboBox_4.addItem(candidate[0])        


#Where
    def Client_Combobox(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017', db='medx', use_unicode=True,
                               charset='utf8')
        self.cur = self.db.cursor()
              
        self.cur.execute(''' SELECT CompanyName FROM client ''')
        data = self.cur.fetchall()
        
        for client in data :
            self.comboBox_3.addItem(client[0])        
            
            
    def Department_Combobox(self):
        ClientID = self.comboBox.currentIndex()
        #print(ClientID)
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017', db='medx', use_unicode=True,
                               charset='utf8')
        self.cur = self.db.cursor()
              
        sql = ''' SELECT Description FROM ClientDepartment WHERE ClientID = %s '''
        self.cur.execute(sql , [(ClientID)])
        data = self.cur.fetchall()
        self.comboBox_2.clear()
        
        for department in data :
            self.comboBox_2.addItem(department[0])        


    def Candidate_Qualifcation_Combobox(self):
        CandidateID = self.comboBox_2.currentIndex()
        CandidateID = int(CandidateID) + 1
        #print(CandidateID)
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017', db='medx', use_unicode=True,
                               charset='utf8')
        self.cur = self.db.cursor()
              
        sql = ''' SELECT LastName FROM Candidate_live WHERE CandidateID = %s '''
        self.cur.execute(sql , [(CandidateID)])
        data = self.cur.fetchall()
        print(data)
        self.comboBox_2.clear()
        
        for qualifcation in data :
            self.comboBox_2.addItem(qualifcation[0])



    def Add_RateTemplateOverrideDetails(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        ClientID = self.comboBox_3.currentText()
        DepartmentID = self.comboBox.currentText()
        CandidateID = self.comboBox_4.currentText()
        QualificationID = self.comboBox_2.currentText()
        NormalDayRate = self.lineEdit.text()
        NormalDayCommissionPercentage = self.lineEdit_5.text()
        NormalNightRate = self.lineEdit_7.text()
        NormalNightCommissionPercentage = self.lineEdit_6.text()
        SaturdayDayRate = self.lineEdit_10.text()
        SaturdayDayCommissionPercentage = self.lineEdit_9.text()
        SaturdayNightRate = self.lineEdit_11.text()
        SaturdayNightCommissionPercentage = self.lineEdit_8.text()
        SundayDayRate = self.lineEdit_16.text()
        SundayDayCommissionPercentage = self.lineEdit_14.text()
        SundayNightRate = self.lineEdit_17.text()
        SundayNightCommissionPercentage = self.lineEdit_13.text()
        PublicHolidayDayRate = self.lineEdit_15.text()
        PublicHolidayDayCommissionPercentage = self.lineEdit_19.text()
        PublicHolidayNightRate = self.lineEdit_18.text()
        PublicHolidayNightCommissionPercentage = self.lineEdit_12.text()
        ClientDepartmentID = self.comboBox.currentText()

        self.cur.execute('''
            INSERT INTO RateTemplateOverride SET ClientID=%s, DepartmentID=%s, CandidateID=%s, QualificationID=%s, NormalDayRate=%s, NormalDayCommissionPercentage=%s, NormalNightRate=%s, NormalNightCommissionPercentage=%s, SaturdayDayRate=%s, SaturdayDayCommissionPercentage=%s, SaturdayNightRate=%s, SaturdayNightCommissionPercentage=%s, SundayDayRate=%s, SundayDayCommissionPercentage=%s,  SundayNightRate=%s,  SundayNightCommissionPercentage=%s,  PublicHolidayDayRate=%s,  PublicHolidayDayCommissionPercentage=%s,  PublicHolidayNightRate=%s,  PublicHolidayNightCommissionPercentage=%s, ClientDepartmentID=%s
        ''', (
        ClientID, DepartmentID, CandidateID, QualificationID, NormalDayRate, NormalDayCommissionPercentage, NormalNightRate, NormalNightCommissionPercentage, SaturdayDayRate, SaturdayDayCommissionPercentage, SaturdayNightRate, SaturdayNightCommissionPercentage, SundayDayRate, SundayDayCommissionPercentage,  SundayNightRate,  SundayNightCommissionPercentage,  PublicHolidayDayRate,  PublicHolidayDayCommissionPercentage,  PublicHolidayNightRate,  PublicHolidayNightCommissionPercentage, ClientDepartmentID))

        self.db.commit()
        print("Rate Template Override Details Add")  


    def retranslateUi(self, RateTemplateOverrideDetails):
        _translate = QtCore.QCoreApplication.translate
        RateTemplateOverrideDetails.setWindowTitle(_translate("RateTemplateOverrideDetails", "ProTemp Activity Type Details"))
        RateTemplateOverrideDetails.setToolTip(_translate("RateTemplateOverrideDetails", "<html><head/><body><p>Test</p></body></html>"))
        RateTemplateOverrideDetails.setWhatsThis(_translate("RateTemplateOverrideDetails", "<html><head/><body><p>Test</p></body></html>"))
        self.pushButton_6.setText(_translate("RateTemplateOverrideDetails", "Cancel"))
        self.pushButton_6.setShortcut(_translate("RateTemplateOverrideDetails", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("RateTemplateOverrideDetails", "Ok"))
        self.lineEdit_2.setText(_translate("RateTemplateOverrideDetails", "Rate Template Override Details"))
        self.label_2.setText(_translate("RateTemplateOverrideDetails", "Department:"))
        self.label_3.setText(_translate("RateTemplateOverrideDetails", "Client:"))
        self.label_4.setText(_translate("RateTemplateOverrideDetails", "Qualification:"))
        self.label_5.setText(_translate("RateTemplateOverrideDetails", "Candidate:"))
        self.pushButton_7.setText(_translate("RateTemplateOverrideDetails", "X"))
        self.pushButton_8.setText(_translate("RateTemplateOverrideDetails", "X"))
        self.lineEdit.setText(_translate("RateTemplateOverrideDetails", " 0,000"))
        self.label.setText(_translate("RateTemplateOverrideDetails", "Normal Day Rate:"))
        self.lineEdit_5.setText(_translate("RateTemplateOverrideDetails", " 0,000"))
        self.label_6.setText(_translate("RateTemplateOverrideDetails", "Normal Day Commission Percentage:"))
        self.lineEdit_6.setText(_translate("RateTemplateOverrideDetails", " 0,000"))
        self.lineEdit_7.setText(_translate("RateTemplateOverrideDetails", " 0,000"))
        self.label_7.setText(_translate("RateTemplateOverrideDetails", "Normal Night Rate:"))
        self.label_8.setText(_translate("RateTemplateOverrideDetails", "Normal Night Commission Percentage:"))
        self.lineEdit_8.setText(_translate("RateTemplateOverrideDetails", " 0,000"))
        self.lineEdit_9.setText(_translate("RateTemplateOverrideDetails", " 0,000"))
        self.lineEdit_10.setText(_translate("RateTemplateOverrideDetails", " 0,000"))
        self.label_9.setText(_translate("RateTemplateOverrideDetails", "Saterday Night Rate:"))
        self.label_10.setText(_translate("RateTemplateOverrideDetails", "Saterday Day Rate:"))
        self.lineEdit_11.setText(_translate("RateTemplateOverrideDetails", " 0,000"))
        self.label_11.setText(_translate("RateTemplateOverrideDetails", "Saterday Day Commission Percentage:"))
        self.label_12.setText(_translate("RateTemplateOverrideDetails", "Saterday Night Commission Percentage:"))
        self.lineEdit_12.setText(_translate("RateTemplateOverrideDetails", " 0,000"))
        self.lineEdit_13.setText(_translate("RateTemplateOverrideDetails", " 0,000"))
        self.lineEdit_14.setText(_translate("RateTemplateOverrideDetails", " 0,000"))
        self.lineEdit_15.setText(_translate("RateTemplateOverrideDetails", " 0,000"))
        self.lineEdit_16.setText(_translate("RateTemplateOverrideDetails", " 0,000"))
        self.label_13.setText(_translate("RateTemplateOverrideDetails", "Sunday Night Rate:"))
        self.label_14.setText(_translate("RateTemplateOverrideDetails", "Sunday Day Rate:"))
        self.label_15.setText(_translate("RateTemplateOverrideDetails", "Public Holiday Night Commission Percentage:"))
        self.lineEdit_17.setText(_translate("RateTemplateOverrideDetails", " 0,000"))
        self.label_16.setText(_translate("RateTemplateOverrideDetails", "Sunday Day Commission Percentage:"))
        self.label_17.setText(_translate("RateTemplateOverrideDetails", "Public Holiday Day Commission Percentage:"))
        self.label_18.setText(_translate("RateTemplateOverrideDetails", "Sunday Night Commission Percentage:"))
        self.label_19.setText(_translate("RateTemplateOverrideDetails", "Public Holiday Day Rate:"))
        self.lineEdit_18.setText(_translate("RateTemplateOverrideDetails", " 0,000"))
        self.label_20.setText(_translate("RateTemplateOverrideDetails", "Public Holiday Night Rate:"))
        self.lineEdit_19.setText(_translate("RateTemplateOverrideDetails", " 0,000"))
        self.label_21.setText(_translate("RateTemplateOverrideDetails", "Rates and Commision Percentages that are 0 will be ignored and"))
        self.label_22.setText(_translate("RateTemplateOverrideDetails", "the values will be retrieved from either the Rate Template 1 or 2."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RateTemplateOverrideDetails = QtWidgets.QWidget()
    ui = Ui_RateTemplateOverrideDetails()
    ui.setupUi(RateTemplateOverrideDetails)
    RateTemplateOverrideDetails.show()
    sys.exit(app.exec_())

