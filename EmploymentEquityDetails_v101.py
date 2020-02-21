from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pymysql


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import sys
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import qApp
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, \
    QTableWidget, QTableWidgetItem, QMessageBox, QHBoxLayout, QLineEdit, QLabel, QGridLayout, QHeaderView


class Ui_EmploymentEquityDetails(object):
    def setupUi(self, EmploymentEquityDetails):
        EmploymentEquityDetails.setObjectName("EmploymentEquityDetails")
        EmploymentEquityDetails.resize(591, 201)
        self.pushButton_6 = QtWidgets.QPushButton(EmploymentEquityDetails)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 160, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(EmploymentEquityDetails)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 160, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Add_EmploymentEquityDetails)
        self.lineEdit_2 = QtWidgets.QLineEdit(EmploymentEquityDetails)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 591, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(EmploymentEquityDetails)
        self.lineEdit.setGeometry(QtCore.QRect(180, 40, 341, 30))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(EmploymentEquityDetails)
        self.line.setGeometry(QtCore.QRect(0, 140, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(EmploymentEquityDetails)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 121, 18))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(EmploymentEquityDetails)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 80, 131, 30))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(EmploymentEquityDetails)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 121, 18))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(EmploymentEquityDetails)
        QtCore.QMetaObject.connectSlotsByName(EmploymentEquityDetails)


    def Add_EmploymentEquityDetails(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        description = self.lineEdit.text()
        Code = self.lineEdit_3.text()
        Deleted = "False"


        self.cur.execute('''
            INSERT INTO EmploymentEquity SET Description=%s, Code=%s ,Deleted=%s
        ''', (
        description, Code, Deleted))

        self.db.commit()
        print("Employment Equity Add")


    def retranslateUi(self, EmploymentEquityDetails):
        _translate = QtCore.QCoreApplication.translate
        EmploymentEquityDetails.setWindowTitle(_translate("EmploymentEquityDetails", "ProTemp"))
        EmploymentEquityDetails.setToolTip(_translate("EmploymentEquityDetails", "<html><head/><body><p>Test</p></body></html>"))
        EmploymentEquityDetails.setWhatsThis(_translate("EmploymentEquityDetails", "<html><head/><body><p>Test</p></body></html>"))
        self.pushButton_6.setText(_translate("EmploymentEquityDetails", "Cancel"))
        self.pushButton_6.setShortcut(_translate("EmploymentEquityDetails", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("EmploymentEquityDetails", "Ok"))
        self.lineEdit_2.setText(_translate("EmploymentEquityDetails", "Employment Equity Details"))
        self.label_3.setText(_translate("EmploymentEquityDetails", "Description:"))
        self.label_4.setText(_translate("EmploymentEquityDetails", "Code:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmploymentEquityDetails = QtWidgets.QWidget()
    ui = Ui_EmploymentEquityDetails()
    ui.setupUi(EmploymentEquityDetails)
    EmploymentEquityDetails.show()
    sys.exit(app.exec_())

