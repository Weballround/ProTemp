from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from Qualification123 import Ui_Qualification


class Ui_Client_Department_Details(object):
    def setupUi(self, Client_Department_Details):
        Client_Department_Details.setObjectName("Client_Department_Details")
        Client_Department_Details.resize(889, 685)
        self.centralwidget = QtWidgets.QWidget(Client_Department_Details)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 871, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 620, 107, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Details_Add)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 620, 107, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 30, 861, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(190, 40, 561, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 80, 561, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 120, 561, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(190, 160, 561, 30))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(190, 200, 431, 30))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 50, 101, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 111, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 111, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 141, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(30, 210, 111, 18))
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 200, 21, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(680, 200, 21, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab, "")
        self.Tab_2 = QtWidgets.QWidget()
        self.Tab_2.setObjectName("Tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.Tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 781, 461))
        self.tableWidget.setMaximumSize(QtCore.QSize(841, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton = QtWidgets.QPushButton(self.Tab_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 107, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openWindow1)
        self.pushButton_3 = QtWidgets.QPushButton(self.Tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 10, 107, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.Tab_2, "")
        Client_Department_Details.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Client_Department_Details)
        self.statusbar.setObjectName("statusbar")
        Client_Department_Details.setStatusBar(self.statusbar)

        self.retranslateUi(Client_Department_Details)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Client_Department_Details)


    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui1 = Ui_Qualification()
        self.ui1.setupUi(self.window)
        self.window.show()


    def Details_Add(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='pierreb', password='Springboks2017',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()

        description = self.lineEdit.text()
        system_code = self.lineEdit_3.text()
        payroll_code = self.lineEdit_4.text()
        integration_code = self.lineEdit_5.text()
        category  = self.lineEdit_6.text()


        self.cur.execute('''
            INSERT INTO ClientDepartment SET Description=%s ,Code=%s ,PayrollCode=%s ,IntegrationCode=%s ,ClientDepartmentCategoryID=%s
        ''', (
        description, system_code, payroll_code, integration_code, category))

        self.db.commit()


    def retranslateUi(self, Client_Department_Details):
        _translate = QtCore.QCoreApplication.translate
        Client_Department_Details.setWindowTitle(_translate("Client_Department_Details", "Client Department Details"))
        self.lineEdit_2.setText(_translate("Client_Department_Details", " Client Department Details"))
        self.pushButton_5.setText(_translate("Client_Department_Details", "Ok"))
        self.pushButton_6.setText(_translate("Client_Department_Details", "Cancel"))
        self.pushButton_6.setShortcut(_translate("Client_Department_Details", "Ctrl+Q"))
        self.label.setText(_translate("Client_Department_Details", "Description:"))
        self.label_2.setText(_translate("Client_Department_Details", "System Code:"))
        self.label_3.setText(_translate("Client_Department_Details", "Payroll Code:"))
        self.label_4.setText(_translate("Client_Department_Details", "Integration Code:"))
        self.label_5.setText(_translate("Client_Department_Details", "Category:"))
        self.pushButton_2.setText(_translate("Client_Department_Details", "X"))
        self.pushButton_4.setText(_translate("Client_Department_Details", "X"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Client_Department_Details", "General"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Client_Department_Details", "Description"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Client_Department_Details", "Code"))
        self.pushButton.setText(_translate("Client_Department_Details", "Add"))
        self.pushButton_3.setText(_translate("Client_Department_Details", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_2), _translate("Client_Department_Details", "Qualifications"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Client_Department_Details = QtWidgets.QMainWindow()
    ui = Ui_Client_Department_Details()
    ui.setupUi(Client_Department_Details)
    Client_Department_Details.show()
    sys.exit(app.exec_())
