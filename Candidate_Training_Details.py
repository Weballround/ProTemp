from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class Ui_CandidateTrainingDetails(object):
    def setupUi(self, CandidateTrainingDetails):
        CandidateTrainingDetails.setObjectName("CandidateTrainingDetails")
        CandidateTrainingDetails.resize(800, 487)
        self.pushButton_6 = QtWidgets.QPushButton(CandidateTrainingDetails)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 450, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(CandidateTrainingDetails)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 450, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(CandidateTrainingDetails)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 881, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(CandidateTrainingDetails)
        self.label.setGeometry(QtCore.QRect(20, 210, 141, 18))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(CandidateTrainingDetails)
        self.line.setGeometry(QtCore.QRect(0, 430, 801, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.dateEdit = QtWidgets.QDateEdit(CandidateTrainingDetails)
        self.dateEdit.setGeometry(QtCore.QRect(190, 200, 591, 28))
        self.dateEdit.setObjectName("dateEdit")
        self.label_2 = QtWidgets.QLabel(CandidateTrainingDetails)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 141, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(CandidateTrainingDetails)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 141, 18))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(CandidateTrainingDetails)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 120, 551, 28))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(CandidateTrainingDetails)
        self.comboBox_3.setGeometry(QtCore.QRect(190, 40, 551, 28))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_4 = QtWidgets.QLabel(CandidateTrainingDetails)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 141, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(CandidateTrainingDetails)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 141, 18))
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(CandidateTrainingDetails)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 120, 31, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(CandidateTrainingDetails)
        self.pushButton_3.setGeometry(QtCore.QRect(750, 40, 31, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(CandidateTrainingDetails)
        self.textEdit.setGeometry(QtCore.QRect(20, 280, 761, 131))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(CandidateTrainingDetails)
        self.lineEdit.setGeometry(QtCore.QRect(190, 80, 551, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(CandidateTrainingDetails)
        self.label_6.setGeometry(QtCore.QRect(20, 250, 141, 18))
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(CandidateTrainingDetails)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 160, 591, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.Client_Combobox()
        self.Department_Combobox()


        self.retranslateUi(CandidateTrainingDetails)
        QtCore.QMetaObject.connectSlotsByName(CandidateTrainingDetails)


    def Client_Combobox(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT Code FROM ClientDepartment ''')
        data = self.cur.fetchall()

        for client in data:
            self.comboBox_2.addItem(client[0])


    def Department_Combobox(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT DISTINCT Description FROM ClientDepartment ''')
        data = self.cur.fetchall()

        for department in data:
            self.comboBox_3.addItem(department[0])



    def retranslateUi(self, CandidateTrainingDetails):
        _translate = QtCore.QCoreApplication.translate
        CandidateTrainingDetails.setWindowTitle(_translate("CandidateTrainingDetails", "ProTemp"))
        self.pushButton_6.setText(_translate("CandidateTrainingDetails", "Cancel"))
        self.pushButton_5.setText(_translate("CandidateTrainingDetails", "Ok"))
        self.lineEdit_2.setText(_translate("CandidateTrainingDetails", "Candidate Training Details"))
        self.label.setText(_translate("CandidateTrainingDetails", "Course Date:"))
        self.dateEdit.setDisplayFormat(_translate("CandidateTrainingDetails", "dd MMMM yyyy "))
        self.label_2.setText(_translate("CandidateTrainingDetails", "Courese Code:"))
        self.label_3.setText(_translate("CandidateTrainingDetails", "Duration:"))
        self.label_4.setText(_translate("CandidateTrainingDetails", "Client:"))
        self.label_5.setText(_translate("CandidateTrainingDetails", "Course Name:"))
        self.pushButton_2.setText(_translate("CandidateTrainingDetails", "F"))
        self.pushButton_3.setText(_translate("CandidateTrainingDetails", "F"))
        self.label_6.setText(_translate("CandidateTrainingDetails", "Content:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CandidateTrainingDetails = QtWidgets.QWidget()
    ui = Ui_CandidateTrainingDetails()
    ui.setupUi(CandidateTrainingDetails)
    CandidateTrainingDetails.show()
    sys.exit(app.exec_())
