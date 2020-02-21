from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class Ui_Candidate_Indemnity_Details(object):
    def setupUi3(self, Candidate_Indemnity_Details):
        Candidate_Indemnity_Details.setObjectName("Candidate_Indemnity_Details")
        Candidate_Indemnity_Details.resize(591, 207)
        self.pushButton_6 = QtWidgets.QPushButton(Candidate_Indemnity_Details)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 170, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(Candidate_Indemnity_Details)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 170, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Indemnity_Add)
        self.lineEdit_2 = QtWidgets.QLineEdit(Candidate_Indemnity_Details)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 591, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Candidate_Indemnity_Details)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 80, 191, 30))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(Candidate_Indemnity_Details)
        self.label.setGeometry(QtCore.QRect(30, 130, 121, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Candidate_Indemnity_Details)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 121, 18))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Candidate_Indemnity_Details)
        self.line.setGeometry(QtCore.QRect(0, 150, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(Candidate_Indemnity_Details)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 121, 18))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Candidate_Indemnity_Details)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 40, 191, 30))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.dateEdit = QtWidgets.QDateEdit(Candidate_Indemnity_Details)
        self.dateEdit.setGeometry(QtCore.QRect(200, 120, 181, 28))
        self.dateEdit.setObjectName("dateEdit")
        #self.pushButton_6.clicked.connect(app.quit)

        self.retranslateUi(Candidate_Indemnity_Details)
        QtCore.QMetaObject.connectSlotsByName(Candidate_Indemnity_Details)


    def Indemnity_Add(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        company = self.lineEdit_4.text()
        policy_number = self.lineEdit_3.text()
        expirydate = self.dateEdit.text()


        self.cur.execute('''
            INSERT INTO CandidateIndemnity SET Company=%s ,PolicyNumber=%s ,ExpiryDate=%s
        ''', (
        company, policy_number, expirydate))

        self.db.commit()


    def retranslateUi(self, Candidate_Indemnity_Details):
        _translate = QtCore.QCoreApplication.translate
        Candidate_Indemnity_Details.setWindowTitle(_translate("Candidate_Indemnity_Details", "ProTemp"))
        self.pushButton_6.setText(_translate("Candidate_Indemnity_Details", "Cancel"))
        self.pushButton_5.setText(_translate("Candidate_Indemnity_Details", "Ok"))
        self.lineEdit_2.setText(_translate("Candidate_Indemnity_Details", "Candidate Imndemnity Details"))
        self.label.setText(_translate("Candidate_Indemnity_Details", "Expiry Date:"))
        self.label_2.setText(_translate("Candidate_Indemnity_Details", " Policy Number:"))
        self.label_3.setText(_translate("Candidate_Indemnity_Details", "Company:"))
        self.dateEdit.setDisplayFormat(_translate("Candidate_Indemnity_Details", "dd MMMM yyyy"))
        self.pushButton_6.setShortcut(_translate("Candidate_Indemnity_Details", "Ctrl+Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Candidate_Indemnity_Details = QtWidgets.QWidget()
    ui = Ui_Candidate_Indemnity_Details()
    ui.setupUi3(Candidate_Indemnity_Details)
    Candidate_Indemnity_Details.show()
    sys.exit(app.exec_())
