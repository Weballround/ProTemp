#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed August  29 12:45 2019

Last Updated Tue December  17 14:09 2019

@author: pierreb
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class Ui_LinkedClientDetails(object):
    def setupUi(self, LinkedClientDetails):
        LinkedClientDetails.setObjectName("LinkedClientDetails")
        LinkedClientDetails.resize(591, 207)
        self.pushButton_6 = QtWidgets.QPushButton(LinkedClientDetails)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 170, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(LinkedClientDetails)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 170, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Linked_Client_Details)
        self.lineEdit_2 = QtWidgets.QLineEdit(LinkedClientDetails)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 591, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(LinkedClientDetails)
        self.label.setGeometry(QtCore.QRect(20, 130, 251, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(LinkedClientDetails)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 141, 18))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(LinkedClientDetails)
        self.line.setGeometry(QtCore.QRect(0, 150, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(LinkedClientDetails)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 121, 18))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(LinkedClientDetails)
        self.pushButton.setGeometry(QtCore.QRect(480, 40, 31, 30))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(LinkedClientDetails)
        self.checkBox.setGeometry(QtCore.QRect(260, 80, 113, 29))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.lineEdit_5 = QtWidgets.QLineEdit(LinkedClientDetails)
        self.lineEdit_5.setGeometry(QtCore.QRect(260, 120, 321, 30))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.comboBox = QtWidgets.QComboBox(LinkedClientDetails)
        self.comboBox.setGeometry(QtCore.QRect(260, 40, 211, 28))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(LinkedClientDetails)
        QtCore.QMetaObject.connectSlotsByName(LinkedClientDetails)

    def retranslateUi(self, LinkedClientDetails):
        _translate = QtCore.QCoreApplication.translate
        LinkedClientDetails.setWindowTitle(_translate("LinkedClientDetails", "ProTemp"))
        self.pushButton_6.setText(_translate("LinkedClientDetails", "Cancel"))
        self.pushButton_5.setText(_translate("LinkedClientDetails", "Ok"))
        self.lineEdit_2.setText(_translate("LinkedClientDetails", "Linked Client Details"))
        self.label.setText(_translate("LinkedClientDetails", "Candidate integration Code:"))
        self.label_2.setText(_translate("LinkedClientDetails", "Is Preferred Client:"))
        self.label_3.setText(_translate("LinkedClientDetails", "Client:"))
        self.pushButton.setText(_translate("LinkedClientDetails", "F"))
        self.Client_Combobox()


    def Client_Combobox(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT Code FROM ClientDepartment ''')
        data = self.cur.fetchall()

        for client in data:
            self.comboBox.addItem(client[0])


    def Linked_Client_Details(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        company = self.comboBox.text()
        policy_number = self.checkBox.text()
        expirydate = self.lineEdit_2.text()


        self.cur.execute('''
            INSERT INTO CandidateIndemnity SET Company=%s ,PolicyNumber=%s ,ExpiryDate=%s
        ''', (
        company, policy_number, expirydate))

        self.db.commit()        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LinkedClientDetails = QtWidgets.QWidget()
    ui = Ui_LinkedClientDetails()
    ui.setupUi(LinkedClientDetails)
    LinkedClientDetails.show()
    sys.exit(app.exec_())
