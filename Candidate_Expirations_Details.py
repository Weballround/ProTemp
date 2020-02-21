from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class Ui_CandidateExpirationsDetails(object):
    def setupUi(self, CandidateExpirationsDetails):
        CandidateExpirationsDetails.setObjectName("CandidateExpirationsDetails")
        CandidateExpirationsDetails.resize(591, 207)
        self.pushButton_6 = QtWidgets.QPushButton(CandidateExpirationsDetails)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 170, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(CandidateExpirationsDetails)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 170, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Expiration_Add)
        self.lineEdit_2 = QtWidgets.QLineEdit(CandidateExpirationsDetails)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 591, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(CandidateExpirationsDetails)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 80, 191, 30))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(CandidateExpirationsDetails)
        self.label.setGeometry(QtCore.QRect(30, 130, 121, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(CandidateExpirationsDetails)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 161, 18))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(CandidateExpirationsDetails)
        self.line.setGeometry(QtCore.QRect(0, 150, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(CandidateExpirationsDetails)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 121, 18))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(CandidateExpirationsDetails)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 40, 191, 30))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.dateEdit = QtWidgets.QDateEdit(CandidateExpirationsDetails)
        self.dateEdit.setGeometry(QtCore.QRect(200, 120, 181, 28))
        self.dateEdit.setObjectName("dateEdit")
        #self.pushButton_6.clicked.connect(exit)
        #self.pushButton_6.clicked.connect(QtWidgets.qApp.quit)
        #self.pushButton_6.clicked.connect(QtWidgets.qApp.exit)



        self.retranslateUi(CandidateExpirationsDetails)
        QtCore.QMetaObject.connectSlotsByName(CandidateExpirationsDetails)


    def Expiration_Add(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        description = self.lineEdit_4.text()
        referencenumber = self.lineEdit_3.text()
        expirydate = self.dateEdit.text()


        self.cur.execute('''
            INSERT INTO CandidateExpiration SET Description=%s ,ReferenceNumber=%s ,ExpiryDate=%s
        ''', (
        description, referencenumber, expirydate))

        self.db.commit()
        self.thread.quit()



    def retranslateUi(self, CandidateExpirationsDetails):
        _translate = QtCore.QCoreApplication.translate
        CandidateExpirationsDetails.setWindowTitle(_translate("CandidateExpirationsDetails", "ProTemp"))
        self.pushButton_6.setText(_translate("CandidateExpirationsDetails", "Cancel"))
        self.pushButton_6.setShortcut(_translate("CandidateExpirationsDetails", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("CandidateExpirationsDetails", "Ok"))
        self.lineEdit_2.setText(_translate("CandidateExpirationsDetails", "Candidate Expirations Details"))
        self.label.setText(_translate("CandidateExpirationsDetails", "Expiry Date:"))
        self.label_2.setText(_translate("CandidateExpirationsDetails", "Reference Number:"))
        self.label_3.setText(_translate("CandidateExpirationsDetails", "Description:"))
        self.dateEdit.setDisplayFormat(_translate("CandidateExpirationsDetails", "dd MM yyyy "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CandidateExpirationsDetails = QtWidgets.QWidget()
    ui = Ui_CandidateExpirationsDetails()
    ui.setupUi(CandidateExpirationsDetails)
    CandidateExpirationsDetails.show()
    sys.exit(app.exec_())
