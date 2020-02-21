#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed July  9 13:40:54 2019

Last Updated Fri February 03 14:13 2020

@author: pierreb
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from clickatell.http import Http
import pymysql
import sys


class Ui_BookingDetails(object):
    def setupUi(self, BookingDetails):
        BookingDetails.setObjectName("BookingDetails")
        BookingDetails.resize(648, 693)
        self.centralwidget = QtWidgets.QWidget(BookingDetails)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 621, 641))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 400, 54, 17))
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(0, 280, 611, 121))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit_2.setGeometry(QtCore.QRect(130, 10, 221, 22))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 54, 17))
        self.label_6.setObjectName("label_6")
        self.label_18 = QtWidgets.QLabel(self.frame_2)
        self.label_18.setGeometry(QtCore.QRect(470, 2, 111, 17))
        self.label_18.setObjectName("label_18")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(370, 80, 211, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_20 = QtWidgets.QLabel(self.frame_2)
        self.label_20.setGeometry(QtCore.QRect(290, 90, 81, 17))
        self.label_20.setObjectName("label_20")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(10, 90, 101, 17))
        self.label_11.setObjectName("label_11")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 50, 211, 21))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(0, 0, 71, 22))
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(100, 0, 71, 22))
        self.radioButton_4.setObjectName("radioButton_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_3.setGeometry(QtCore.QRect(130, 80, 111, 31))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_6.setGeometry(QtCore.QRect(70, 6, 41, 21))
        self.radioButton_6.setChecked(True)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 6, 51, 22))
        self.radioButton_5.setObjectName("radioButton_5")
        self.timeEdit = QtWidgets.QTimeEdit(self.frame_2)
        self.timeEdit.setGeometry(QtCore.QRect(130, 40, 51, 22))
        self.timeEdit.setTime(QtCore.QTime(7, 0, 0))
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.frame_2)
        self.timeEdit_2.setGeometry(QtCore.QRect(210, 40, 51, 22))
        self.timeEdit_2.setTime(QtCore.QTime(19, 0, 0))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(190, 44, 16, 16))
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 40, 41, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_21 = QtWidgets.QLabel(self.frame_2)
        self.label_21.setGeometry(QtCore.QRect(270, 44, 31, 17))
        self.label_21.setObjectName("label_21")
        self.frame_3 = QtWidgets.QFrame(self.tab)
        self.frame_3.setGeometry(QtCore.QRect(0, 410, 601, 61))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(10, 33, 121, 17))
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(180, 10, 91, 16))
        self.label_12.setObjectName("label_12")
        self.label_23 = QtWidgets.QLabel(self.frame_3)
        self.label_23.setGeometry(QtCore.QRect(180, 33, 91, 16))
        self.label_23.setObjectName("label_23")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 271, 54, 17))
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(10, 470, 54, 17))
        self.label_10.setObjectName("label_10")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(0, 180, 611, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(570, 10, 31, 29))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("find-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 50, 31, 29))
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(130, 10, 431, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 50, 431, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 54, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 101, 17))
        self.label_5.setObjectName("label_5")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(10, 171, 54, 17))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(10, 32, 54, 17))
        self.label_14.setObjectName("label_14")
        self.frame_4 = QtWidgets.QFrame(self.tab)
        self.frame_4.setGeometry(QtCore.QRect(0, 40, 611, 131))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_7.setGeometry(QtCore.QRect(570, 10, 31, 29))
        self.pushButton_7.setText("")
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_8.setGeometry(QtCore.QRect(570, 50, 31, 29))
        self.pushButton_8.setText("")
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setObjectName("pushButton_8")
        self.comboBox_6 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_6.setGeometry(QtCore.QRect(130, 10, 431, 25))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_7 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_7.setGeometry(QtCore.QRect(130, 50, 431, 25))
        self.comboBox_7.setObjectName("comboBox_7")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 91, 17))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(10, 50, 101, 17))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_4)
        self.label_17.setGeometry(QtCore.QRect(10, 90, 111, 17))
        self.label_17.setObjectName("label_17")
        self.comboBox_8 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_8.setGeometry(QtCore.QRect(130, 90, 431, 25))
        self.comboBox_8.setObjectName("comboBox_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_9.setGeometry(QtCore.QRect(570, 90, 31, 29))
        self.pushButton_9.setText("")
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(10, 8, 171, 17))
        self.label_19.setObjectName("label_19")
        self.comboBox_9 = QtWidgets.QComboBox(self.tab)
        self.comboBox_9.setGeometry(QtCore.QRect(130, 5, 431, 25))
        self.comboBox_9.setObjectName("comboBox_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab)
        self.pushButton_10.setGeometry(QtCore.QRect(570, 4, 31, 29))
        self.pushButton_10.setText("")
        self.pushButton_10.setIcon(icon)
        self.pushButton_10.setObjectName("pushButton_10")
        self.frame_5 = QtWidgets.QFrame(self.tab)
        self.frame_5.setGeometry(QtCore.QRect(0, 480, 751, 101))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.dateEdit_4 = QtWidgets.QDateEdit(self.frame_5)
        self.dateEdit_4.setGeometry(QtCore.QRect(110, 10, 261, 22))
        self.dateEdit_4.setCalendarPopup(True)
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.label_22 = QtWidgets.QLabel(self.frame_5)
        self.label_22.setGeometry(QtCore.QRect(40, 70, 61, 17))
        self.label_22.setObjectName("label_22")
        self.textEdit = QtWidgets.QTextEdit(self.frame_5)
        self.textEdit.setGeometry(QtCore.QRect(110, 40, 481, 51))
        self.textEdit.setObjectName("textEdit")
        self.checkBox = QtWidgets.QCheckBox(self.frame_5)
        self.checkBox.setGeometry(QtCore.QRect(10, 10, 121, 29))
        self.checkBox.setObjectName("checkBox")
        self.label_24 = QtWidgets.QLabel(self.frame_5)
        self.label_24.setGeometry(QtCore.QRect(20, 70, 21, 17))
        self.label_24.setObjectName("label_24")
        self.timeEdit_3 = QtWidgets.QTimeEdit(self.frame_5)
        self.timeEdit_3.setGeometry(QtCore.QRect(470, 10, 118, 22))
        self.timeEdit_3.setObjectName("timeEdit_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(390, 300, 211, 21))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(100, 0, 81, 22))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(0, 0, 71, 22))
        self.radioButton.setToolTipDuration(5)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 10, 791, 701))
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 635, 87, 29))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 635, 87, 29))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 681, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(0, 68, 204);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        BookingDetails.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BookingDetails)
        self.statusbar.setObjectName("statusbar")
        BookingDetails.setStatusBar(self.statusbar)

        self.retranslateUi(BookingDetails)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BookingDetails)

    def retranslateUi(self, BookingDetails):
        _translate = QtCore.QCoreApplication.translate
        BookingDetails.setWindowTitle(_translate("BookingDetails", "Booking Details"))
        self.label_3.setText(_translate("BookingDetails", "What"))
        self.label_6.setText(_translate("BookingDetails", "Date:"))
        self.label_18.setText(_translate("BookingDetails", "Normal Day:"))
        self.label_20.setText(_translate("BookingDetails", "Booking Ref Nr:"))
        self.label_11.setText(_translate("BookingDetails", "Confirmed:"))
        self.radioButton_3.setText(_translate("BookingDetails", "Da&ily"))
        self.radioButton_4.setText(_translate("BookingDetails", "&Monthly"))
        self.radioButton_6.setText(_translate("BookingDetails", "No"))
        self.radioButton_5.setText(_translate("BookingDetails", "&Yes"))
        self.label.setText(_translate("BookingDetails", "to"))
        self.lineEdit_3.setText(_translate("BookingDetails", "12.00"))
        self.label_21.setText(_translate("BookingDetails", "Hours:"))
        self.label_9.setText(_translate("BookingDetails", "Candidate Rate"))
        self.label_8.setText(_translate("BookingDetails", "Client Rate:"))
        self.label_12.setText(_translate("BookingDetails", "_"))
        self.label_23.setText(_translate("BookingDetails", "_"))
        self.label_2.setText(_translate("BookingDetails", "When"))
        self.label_10.setText(_translate("BookingDetails", "Notify"))
        self.label_4.setText(_translate("BookingDetails", "Client:"))
        self.label_5.setText(_translate("BookingDetails", "Department:"))
        self.label_13.setText(_translate("BookingDetails", "Where"))
        self.label_14.setText(_translate("BookingDetails", "Who"))
        self.label_15.setText(_translate("BookingDetails", "Candidate:"))
        self.label_16.setText(_translate("BookingDetails", "Catagory:"))
        self.label_17.setText(_translate("BookingDetails", "Qualifcation:"))
        self.label_19.setText(_translate("BookingDetails", "Fil Vacancy:"))
        self.dateEdit_4.setDisplayFormat(_translate("BookingDetails", "dddd dd MMMM yyyy"))
        self.label_22.setText(_translate("BookingDetails", "chars left"))
        self.checkBox.setText(_translate("BookingDetails", "Reminder:"))
        self.label_24.setText(_translate("BookingDetails", "160"))
        self.radioButton_2.setText(_translate("BookingDetails", "&Night"))
        self.radioButton.setToolTip(_translate("BookingDetails", "Day3"))
        self.radioButton.setWhatsThis(_translate("BookingDetails", "Day2"))
        self.radioButton.setText(_translate("BookingDetails", "&Day"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("BookingDetails", "General"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("BookingDetails", "Notes"))
        self.pushButton_6.setText(_translate("BookingDetails", "Cancel"))
        self.pushButton_5.setText(_translate("BookingDetails", "Ok"))
        self.lineEdit.setText(_translate("BookingDetails", "    Booking Details"))


        #END GUI
        
        self.Vacancy_Combobox()
        self.Client_Combobox()
        self.Candidate_Combobox()
        self.Catagory_Combobox()
        #self.Client_Rate_Combobox()
        #self.Candidate_Rate_Combobox()
        self.radioButton.clicked.connect(self.CheckButtons)
        self.radioButton_2.clicked.connect(self.CheckButtons1)
        self.radioButton_3.clicked.connect(self.CheckButtons2)
        self.radioButton_4.clicked.connect(self.CheckButtons3)
        self.dateEdit_2.setDate(QtCore.QDate.currentDate()) #setting date to current date
        self.dateEdit_4.setDate(QtCore.QDate.currentDate())
        self.timeEdit_3.setTime(QtCore.QTime.currentTime())

        #self.InsertData()
        dateTest = self.dateEdit_2.date().addYears(1)
        #self.Candidate_Show_Qualifications()
        self.pushButton_9.clicked.connect(self.Candidate_Qualifcation_Combobox)
        self.pushButton.clicked.connect(self.Department_Combobox)
        self.pushButton_5.clicked.connect(self.InsertData)
        #ClientID = self.comboBox.currentIndex()


        #self.msgBox_noStaff = QMessageBox(QMessageBox.Information, "Try Again！", "No Results", QMessageBox.Ok)
        

    def Vacancy_Combobox(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017', db='medx', use_unicode=True,
                               charset='utf8')
        self.cur = self.db.cursor()
              
        self.cur.execute(''' SELECT CONCAT(BookingID, ", ",BookingDate, ", ",CandidateCategoryID) AS FullName from Booking2''')
        data = self.cur.fetchall()
        
        for vacancy in data :
            self.comboBox_9.addItem(vacancy[0])


#Who
    def Candidate_Combobox(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017', db='medx', use_unicode=True,
                               charset='utf8')
        self.cur = self.db.cursor()
              
        self.cur.execute(''' SELECT * from Candidate_live''')
        data = self.cur.fetchall()
        
        for candidate in data :
            self.comboBox_6.addItem(candidate[12])


    def Catagory_Combobox(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017', db='medx', use_unicode=True,
                               charset='utf8')
        self.cur = self.db.cursor()
              
        self.cur.execute(''' SELECT Description from Qualification''')
        data = self.cur.fetchall()
                
        for catagory in data :
            self.comboBox_7.addItem(catagory[0])


    def Candidate_Qualifcation_Combobox(self):
        CandidateID = self.comboBox_6.currentIndex()
        CandidateID = int(CandidateID) + 1
        #print(CandidateID)
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017', db='medx', use_unicode=True,
                               charset='utf8')
        self.cur = self.db.cursor()
              
        sql = ''' SELECT CandidateID FROM Candidate_live WHERE CandidateID = %s '''
        self.cur.execute(sql , [(CandidateID)])
        data = self.cur.fetchall()

        candidate_id = (data[0])
        print("candidate_id")
        print(candidate_id)
        print("data")
        print(data)
        sql2 = ''' SELECT QualificationID FROM CandidateQualification WHERE CandidateID = %s '''
        get_qualifcation_code = self.cur.execute(sql2 , [(candidate_id)])
        data2 = self.cur.fetchall()
        print("data2")
        print(data2)

        qualifcation_code = (data2[0])
        print("qualifcation_code")
        print(qualifcation_code)

        #get_qualifcation_code2 = self.cur.execute(sql3 , [(qualifcation_code)])

        self.comboBox_8.clear()
        print("data3 start")

        for qualifcation_code in data2:
            print(1)
            sql3 = ''' SELECT Description FROM Qualification WHERE Code = %s '''
            #sql3 = ''' SELECT Description FROM Qualification WHERE Code = %s '''            
            get_qualifcation_code2 = self.cur.execute(sql3 , [(qualifcation_code)])
            data3 = self.cur.fetchone()

            print(data3[0])
            
            self.comboBox_8.addItem(str(data3[0]))

        #for qualifcation_code in data3 :
        #    self.comboBox_8.addItem(str(qualifcation_code[0]))

        print("Test3")
        print(data2)



#Where
    def Client_Combobox(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017', db='medx', use_unicode=True,
                               charset='utf8')
        self.cur = self.db.cursor()
              
        self.cur.execute(''' SELECT CompanyName FROM client ''')
        data = self.cur.fetchall()
        
        for client in data :
            self.comboBox.addItem(client[0])
            
            
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
            

#When   
    def CheckButtons(self):
        myradioButton = "day_shift"
        if self.radioButton.text():
            print('myradioButton_Hello is Checked')
            self.lineEdit_2.setText("myradioButton")
            self.label_18.setText("Normal Day")
                    
        #else:
         #   print('Else Test')
    
    
    def CheckButtons1(self):
        if self.radioButton_2.text():
            print('myradioButton_2 is Checked')
            self.lineEdit_2.setText("myradioButton_2")
            self.label_18.setText("Normal Night")
            
            
            
    def CheckButtons2(self):
        if self.radioButton_3.text():
            print('myradioButton_3 is Checked')
            self.lineEdit_2.setText("myradioButton_3")

    
    
    def CheckButtons3(self):
        if self.radioButton_4.text():
            print('myradioButton_4 is Checked')
            self.lineEdit_2.setText("myradioButton_3")
        
#What
    def Client_Rate_Combobox(self):
        ClientID = self.comboBox.currentIndex()
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017', db='medx', use_unicode=True,
                               charset='utf8')
        self.cur = self.db.cursor()
              
        sql = ''' SELECT RateTemplate1ID FROM client WHERE ClientID = %s '''
        client_rate = self.cur.execute(sql , [(ClientID)])
        print(data)
        self.label_12.setText(str(data))
        #data = str(self.cur.label_12())#date needs to lose","
        #print(data)
        #for client_rate in data :
            #self.label_12.setText(client_rate[0])
            
            
    def Candidate_Rate_Combobox(self):
        ClientID = self.comboBox.currentIndex()
        #print(ClientID)
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017', db='medx', use_unicode=True,
                               charset='utf8')
        self.cur = self.db.cursor()
              
        sql = ''' SELECT Description FROM ClientDepartment WHERE ClientID = %s '''
        self.cur.execute(sql , [(ClientID)])
        data = self.cur.label_12()
        self.label_23.clear()
        
        for candidate_rate in data :
            #self.label_23.settext(candidate_rate[0])
            self.label_23.setText(candidate_rate[0])


    def Smssing(self):
        username = 'pierre@weballround.co.za'
        password = 'Afj;vn@10'
        apikey = 'ClMitdv4RUCZAVRr3mAuaQ=='
        desnr = '+27814777563'
        #message = "Hello World 16:07"
        message = self.textEdit.toPlainText()

        clickatell = Http(username, password, apikey)
        response = clickatell.sendMessage([desnr], message)

        print(response) #Returns the headers with all the messages


        for entry in response:
            print(entry) #Returns all the message details per message
            print(entry["id"])
            print(entry["destination"])
            print(entry["error"])
            print(entry["errorCode"])
            print("hello world")



    def InsertData(self):
        conn = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017', db='medx', use_unicode=True,
                               charset='utf8')
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.cur = self.db.cursor()
        cur.execute("INSERT INTO Booking(ClientID, BookingDate, CandidateID, CandidateCategoryID, QualificationID, DepartmentID, Day, BookingReferenceNumber, Night, Daily, Confirmed)"
                    "VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(''.join(self.comboBox.currentText()),
                                                                            ''.join(self.comboBox_9.currentText()),
                                                                            ''.join(self.comboBox_6.currentText()),
                                                                            ''.join(self.comboBox_7.currentText()),
                                                                            ''.join(self.comboBox_8.currentText()),
                                                                            ''.join(self.comboBox_2.currentText()),
                                                                            ''.join(self.radioButton_3.text()),
                                                                            ''.join(self.lineEdit_2.text()),
                                                                            ''.join(self.radioButton_2.text()),
                                                                            ''.join(self.radioButton_3.text()),
                                                                            ''.join(self.dateEdit_2.text())))

        cur.execute("INSERT INTO smsmessagestore4(TelephoneCell, Body, TrackingNumber, LogDateTime, ResultState, LastStatus, LastStatusQueried, IsRead, Deleted, UserID, CandidateID, ParentID, IsReceived, ProviderId, ToBeDelivered)"
                            "VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(''.join(self.textEdit.toPlainText()),
                                                                                    ''.join(self.lineEdit_2.text()),
                                                                                    ''.join(self.lineEdit_2.text()),
                                                                                    ''.join(self.lineEdit_2.text()),
                                                                                    ''.join(self.lineEdit_2.text()),
                                                                                    ''.join(self.lineEdit_2.text()),
                                                                                    ''.join(self.lineEdit_2.text()),
                                                                                    ''.join(self.lineEdit_2.text()),
                                                                                    ''.join(self.lineEdit_2.text()),
                                                                                    ''.join(self.lineEdit_2.text()),
                                                                                    ''.join(self.lineEdit_2.text()),
                                                                                    ''.join(self.lineEdit_2.text()),
                                                                                    ''.join(self.lineEdit_2.text()),
                                                                                    ''.join(self.textEdit.toPlainText()),
                                                                                    ''.join(self.timeEdit_3.text())))

        self.Smssing()
        print("Candidate Booking Successfully")
        
        cur.close()
        conn.close()
     

#print(ClientVacancy.CheckButtons[(myradioButton)])        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BookingDetails = QtWidgets.QMainWindow()
    ui = Ui_BookingDetails()
    ui.setupUi(BookingDetails)
    BookingDetails.show()
    sys.exit(app.exec_())
