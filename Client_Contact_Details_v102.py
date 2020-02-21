from PyQt5 import QtCore, QtGui, QtWidgets, uic
import pymysql
import sys
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import qApp
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, \
    QTableWidget, QTableWidgetItem, QMessageBox, QHBoxLayout, QLineEdit, QLabel, QGridLayout, QHeaderView
from Qualification_add import Ui_Form


class Ui_ClientContactDetails(object):
    def setupUi(self, ClientContactDetails):
        ClientContactDetails.setObjectName("ClientContactDetails")
        ClientContactDetails.resize(799, 660)
        self.pushButton_6 = QtWidgets.QPushButton(ClientContactDetails)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 620, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(ClientContactDetails)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 620, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(ClientContactDetails)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 881, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.line = QtWidgets.QFrame(ClientContactDetails)
        self.line.setGeometry(QtCore.QRect(0, 600, 801, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit_16 = QtWidgets.QLineEdit(ClientContactDetails)
        self.lineEdit_16.setGeometry(QtCore.QRect(190, 280, 241, 20))
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_16 = QtWidgets.QLabel(ClientContactDetails)
        self.label_16.setGeometry(QtCore.QRect(20, 280, 131, 16))
        self.label_16.setObjectName("label_16")
        self.lineEdit_13 = QtWidgets.QLineEdit(ClientContactDetails)
        self.lineEdit_13.setGeometry(QtCore.QRect(190, 160, 241, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(ClientContactDetails)
        self.lineEdit_14.setGeometry(QtCore.QRect(190, 220, 241, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_14 = QtWidgets.QLabel(ClientContactDetails)
        self.label_14.setGeometry(QtCore.QRect(20, 220, 131, 16))
        self.label_14.setObjectName("label_14")
        self.label_13 = QtWidgets.QLabel(ClientContactDetails)
        self.label_13.setGeometry(QtCore.QRect(20, 160, 141, 16))
        self.label_13.setObjectName("label_13")
        self.label_4 = QtWidgets.QLabel(ClientContactDetails)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_10 = QtWidgets.QLabel(ClientContactDetails)
        self.label_10.setGeometry(QtCore.QRect(20, 250, 121, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit_4 = QtWidgets.QLineEdit(ClientContactDetails)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 100, 241, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(ClientContactDetails)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 70, 241, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_1 = QtWidgets.QLabel(ClientContactDetails)
        self.label_1.setGeometry(QtCore.QRect(20, 40, 47, 13))
        self.label_1.setObjectName("label_1")
        self.dateEdit_10 = QtWidgets.QDateEdit(ClientContactDetails)
        self.dateEdit_10.setGeometry(QtCore.QRect(190, 250, 241, 22))
        self.dateEdit_10.setCalendarPopup(True)
        self.dateEdit_10.setObjectName("dateEdit_10")
        self.label_2 = QtWidgets.QLabel(ClientContactDetails)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_15 = QtWidgets.QLabel(ClientContactDetails)
        self.label_15.setGeometry(QtCore.QRect(20, 130, 141, 16))
        self.label_15.setObjectName("label_15")
        self.lineEdit_15 = QtWidgets.QLineEdit(ClientContactDetails)
        self.lineEdit_15.setGeometry(QtCore.QRect(190, 130, 241, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_17 = QtWidgets.QLabel(ClientContactDetails)
        self.label_17.setGeometry(QtCore.QRect(20, 190, 121, 16))
        self.label_17.setObjectName("label_17")
        self.lineEdit_17 = QtWidgets.QLineEdit(ClientContactDetails)
        self.lineEdit_17.setGeometry(QtCore.QRect(190, 190, 241, 20))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_18 = QtWidgets.QLabel(ClientContactDetails)
        self.label_18.setGeometry(QtCore.QRect(20, 310, 111, 16))
        self.label_18.setObjectName("label_18")
        self.lineEdit_18 = QtWidgets.QLineEdit(ClientContactDetails)
        self.lineEdit_18.setGeometry(QtCore.QRect(190, 310, 241, 20))
        self.lineEdit_18.setText("")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_19 = QtWidgets.QLabel(ClientContactDetails)
        self.label_19.setGeometry(QtCore.QRect(20, 340, 111, 16))
        self.label_19.setObjectName("label_19")
        self.checkBox = QtWidgets.QCheckBox(ClientContactDetails)
        self.checkBox.setGeometry(QtCore.QRect(190, 340, 113, 29))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.comboBox = QtWidgets.QComboBox(ClientContactDetails)
        self.comboBox.setGeometry(QtCore.QRect(190, 40, 241, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_5.clicked.connect(self.InsertData)

        self.retranslateUi(ClientContactDetails)
        QtCore.QMetaObject.connectSlotsByName(ClientContactDetails)

    def retranslateUi(self, ClientContactDetails):
        _translate = QtCore.QCoreApplication.translate
        ClientContactDetails.setWindowTitle(_translate("ClientContactDetails", "ProTemp"))
        self.pushButton_6.setText(_translate("ClientContactDetails", "Cancel"))
        self.pushButton_5.setText(_translate("ClientContactDetails", "Ok"))
        self.lineEdit_2.setText(_translate("ClientContactDetails", "Client Contact Details"))
        self.label_16.setText(_translate("ClientContactDetails", "Email Address:"))
        self.label_14.setText(_translate("ClientContactDetails", "Telephone Fax:"))
        self.label_13.setText(_translate("ClientContactDetails", "Telephone Work:"))
        self.label_4.setText(_translate("ClientContactDetails", "Last Name:"))
        self.label_10.setText(_translate("ClientContactDetails", "Date of Birth:"))
        self.label_1.setText(_translate("ClientContactDetails", "Title:"))
        self.dateEdit_10.setDisplayFormat(_translate("ClientContactDetails", "dd MMMM yyyy"))
        self.label_2.setText(_translate("ClientContactDetails", "First Name:"))
        self.label_15.setText(_translate("ClientContactDetails", "Telephone Home:"))
        self.label_17.setText(_translate("ClientContactDetails", "Telephone Cell:"))
        self.label_18.setText(_translate("ClientContactDetails", "Designation:"))
        self.label_19.setText(_translate("ClientContactDetails", "Primary:"))
        self.comboBox.setItemText(0, _translate("ClientContactDetails", "Ms"))
        self.comboBox.setItemText(1, _translate("ClientContactDetails", "Mrs"))
        self.comboBox.setItemText(2, _translate("ClientContactDetails", "Mr"))


    def InsertData(self):
        con = pymysql.connect(host='129.232.195.18',
                             user='pierreb',
                             password='Springboks2017',                             
                             db='medx',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        with con:
                cur = con.cursor()
                cur.execute("INSERT INTO ClientContact(Title, FirstName, LastName, TelephoneHome, TelephoneWork, TelephoneCell, TelephoneFax, DateOfBirth, EmailAddress, Designation)"
                            "VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(''.join(self.lineEdit_3.text()),
                                                                                    ''.join(self.lineEdit_3.text()),
                                                                                    ''.join(self.lineEdit_4.text()),
                                                                                    ''.join(self.lineEdit_15.text()),
                                                                                    ''.join(self.lineEdit_13.text()),
                                                                                    ''.join(self.lineEdit_17.text()),
                                                                                    ''.join(self.lineEdit_14.text()),
                                                                                    ''.join(self.dateEdit_10.text()),
                                                                                    ''.join(self.lineEdit_16.text()),
                                                                                    ''.join(self.lineEdit_18.text())))
        print("Client Contact Details Added Successfully")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClientContactDetails = QtWidgets.QWidget()
    ui = Ui_ClientContactDetails()
    ui.setupUi(ClientContactDetails)
    ClientContactDetails.show()
    sys.exit(app.exec_())
