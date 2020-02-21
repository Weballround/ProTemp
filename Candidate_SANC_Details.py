from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class Ui_CandidateSANCDetails(object):
    def setupUi3(self, CandidateSANCDetails):
        CandidateSANCDetails.setObjectName("CandidateSANCDetails")
        CandidateSANCDetails.resize(591, 213)
        self.pushButton_6 = QtWidgets.QPushButton(CandidateSANCDetails)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 170, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(CandidateSANCDetails)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 170, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.CandidateSANC_Add)
        self.lineEdit_2 = QtWidgets.QLineEdit(CandidateSANCDetails)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 591, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(CandidateSANCDetails)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 80, 191, 30))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(CandidateSANCDetails)
        self.label.setGeometry(QtCore.QRect(20, 50, 121, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(CandidateSANCDetails)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 121, 18))
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(CandidateSANCDetails)
        self.dateEdit.setGeometry(QtCore.QRect(200, 40, 119, 28))
        self.dateEdit.setObjectName("dateEdit")
        self.line = QtWidgets.QFrame(CandidateSANCDetails)
        self.line.setGeometry(QtCore.QRect(0, 150, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        #self.pushButton_6.clicked.connect(app.quit)


        self.retranslateUi(CandidateSANCDetails)
        QtCore.QMetaObject.connectSlotsByName(CandidateSANCDetails)


    def CandidateSANC_Add(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        yearid = self.dateEdit.text()
        sancreceipt = self.lineEdit_3.text()


        self.cur.execute('''
            INSERT INTO CandidateSANC SET YearID=%s ,SANCReceipt=%s
        ''', (yearid, sancreceipt))

        self.db.commit()



    def retranslateUi(self, CandidateSANCDetails):
        _translate = QtCore.QCoreApplication.translate
        CandidateSANCDetails.setWindowTitle(_translate("CandidateSANCDetails", "Candidate SANC Details"))
        self.pushButton_6.setText(_translate("CandidateSANCDetails", "Cancel"))
        self.pushButton_5.setText(_translate("CandidateSANCDetails", "Ok"))
        self.lineEdit_2.setText(_translate("CandidateSANCDetails", "Candidate SANC Details"))
        self.label.setText(_translate("CandidateSANCDetails", "Year:"))
        self.label_2.setText(_translate("CandidateSANCDetails", " SANC receipt:"))
        self.dateEdit.setDisplayFormat(_translate("CandidateSANCDetails", "yyyy"))
        self.pushButton_6.setShortcut(_translate("CandidateSANCDetails", "Ctrl+Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CandidateSANCDetails = QtWidgets.QWidget()
    ui = Ui_CandidateSANCDetails()
    ui.setupUi3(CandidateSANCDetails)
    CandidateSANCDetails.show()
    sys.exit(app.exec_())
