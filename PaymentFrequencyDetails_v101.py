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


class Ui_PaymentFrequencyDetails(object):
    def setupUi(self, PaymentFrequencyDetails):
        PaymentFrequencyDetails.setObjectName("PaymentFrequencyDetails")
        PaymentFrequencyDetails.resize(591, 224)
        self.pushButton_6 = QtWidgets.QPushButton(PaymentFrequencyDetails)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 180, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(PaymentFrequencyDetails)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 180, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Add_PaymentFrequencyDetails)
        self.lineEdit_2 = QtWidgets.QLineEdit(PaymentFrequencyDetails)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 591, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(PaymentFrequencyDetails)
        self.lineEdit.setGeometry(QtCore.QRect(220, 40, 361, 30))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(PaymentFrequencyDetails)
        self.line.setGeometry(QtCore.QRect(0, 160, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(PaymentFrequencyDetails)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 121, 18))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(PaymentFrequencyDetails)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 80, 131, 30))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(PaymentFrequencyDetails)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 121, 18))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(PaymentFrequencyDetails)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 120, 131, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(PaymentFrequencyDetails)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 201, 18))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(PaymentFrequencyDetails)
        QtCore.QMetaObject.connectSlotsByName(PaymentFrequencyDetails)


    def Add_PaymentFrequencyDetails(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        description = self.lineEdit.text()
        PayrollCode = self.lineEdit_3.text()
        PayrollTransactionCode = self.lineEdit_4.text()
        Deleted = "False"


        self.cur.execute('''
            INSERT INTO PaymentFrequency SET Description=%s, PayrollCode=%s ,PayrollTransactionCode=%s ,Deleted=%s
        ''', (
        description, PayrollCode, PayrollTransactionCode, Deleted))

        self.db.commit()
        print("Payment Frequency Details Add")



    def retranslateUi(self, PaymentFrequencyDetails):
        _translate = QtCore.QCoreApplication.translate
        PaymentFrequencyDetails.setWindowTitle(_translate("PaymentFrequencyDetails", "ProTemp"))
        PaymentFrequencyDetails.setToolTip(_translate("PaymentFrequencyDetails", "<html><head/><body><p>Test</p></body></html>"))
        PaymentFrequencyDetails.setWhatsThis(_translate("PaymentFrequencyDetails", "<html><head/><body><p>Test</p></body></html>"))
        self.pushButton_6.setText(_translate("PaymentFrequencyDetails", "Cancel"))
        self.pushButton_6.setShortcut(_translate("PaymentFrequencyDetails", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("PaymentFrequencyDetails", "Ok"))
        self.lineEdit_2.setText(_translate("PaymentFrequencyDetails", "Payment Frequency Details"))
        self.label_3.setText(_translate("PaymentFrequencyDetails", "Description:"))
        self.label_4.setText(_translate("PaymentFrequencyDetails", "Payroll Code:"))
        self.lineEdit_4.setText(_translate("PaymentFrequencyDetails", "501"))
        self.label_5.setText(_translate("PaymentFrequencyDetails", "Payroll Transaction Code:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PaymentFrequencyDetails = QtWidgets.QWidget()
    ui = Ui_PaymentFrequencyDetails()
    ui.setupUi(PaymentFrequencyDetails)
    PaymentFrequencyDetails.show()
    sys.exit(app.exec_())

