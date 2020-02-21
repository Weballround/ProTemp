from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import sys


from Qualification123 import Ui_Qualification
from Candidate_SANC_Details import Ui_CandidateSANCDetails
from Candidate_Indemnity_Details import Ui_Candidate_Indemnity_Details
from Candidate_Expirations_Details import Ui_CandidateExpirationsDetails
from Linked_Client_Details import Ui_LinkedClientDetails
from Candidate_Activity_Details import Ui_CandidateActivityDetails
from Attachment import Ui_Attachment
from Candidate_Training_Details import Ui_CandidateTrainingDetails


class Ui_ClientFolderDetails(object):
    def setupUi(self, ClientFolderDetails):
        ClientFolderDetails.setObjectName("ClientFolderDetails")
        ClientFolderDetails.resize(591, 229)
        self.pushButton_6 = QtWidgets.QPushButton(ClientFolderDetails)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 170, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(ClientFolderDetails)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 170, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Add_ClientFolderDetails)
        self.lineEdit_2 = QtWidgets.QLineEdit(ClientFolderDetails)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 591, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(ClientFolderDetails)
        self.lineEdit.setGeometry(QtCore.QRect(180, 40, 341, 30))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(ClientFolderDetails)
        self.line.setGeometry(QtCore.QRect(0, 150, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(ClientFolderDetails)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 121, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ClientFolderDetails)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 161, 18))
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(ClientFolderDetails)
        self.checkBox.setGeometry(QtCore.QRect(180, 90, 103, 22))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.clickBox)

        self.retranslateUi(ClientFolderDetails)
        QtCore.QMetaObject.connectSlotsByName(ClientFolderDetails)


    def clickBox(self, state):

        if state == QtCore.Qt.Checked:
            IsActive = 'True'
        else:
            IsActive = 'False'

        print(IsActive)


    def Add_ClientFolderDetails(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        description = self.lineEdit.text()
        #print(IsActive)
        IsActive = "False"
        Deleted = "False"


        self.cur.execute('''
            INSERT INTO ClientFolder SET Description=%s ,IsActive=%s ,Deleted=%s
        ''', (
        description, IsActive, Deleted))

        self.db.commit()
        print("Client Folder Details Add")


    def retranslateUi(self, ClientFolderDetails):
        _translate = QtCore.QCoreApplication.translate
        ClientFolderDetails.setWindowTitle(_translate("ClientFolderDetails", "ProTemp"))
        ClientFolderDetails.setToolTip(_translate("ClientFolderDetails", "<html><head/><body><p>Test</p></body></html>"))
        ClientFolderDetails.setWhatsThis(_translate("ClientFolderDetails", "<html><head/><body><p>Test</p></body></html>"))
        self.pushButton_6.setText(_translate("ClientFolderDetails", "Cancel"))
        self.pushButton_6.setShortcut(_translate("ClientFolderDetails", "Ctrl+Q"))
        self.pushButton_5.setText(_translate("ClientFolderDetails", "Ok"))
        self.lineEdit_2.setText(_translate("ClientFolderDetails", "Client Folder Details"))
        self.label_3.setText(_translate("ClientFolderDetails", "Description:"))
        self.label_4.setText(_translate("ClientFolderDetails", "Is Active:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClientFolderDetails = QtWidgets.QWidget()
    ui = Ui_ClientFolderDetails()
    ui.setupUi(ClientFolderDetails)
    ClientFolderDetails.show()
    sys.exit(app.exec_())

