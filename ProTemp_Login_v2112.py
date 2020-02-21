#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Thu November  21 09:41 2018

Last Updated Wed February 05 15:26 2020

@author: pierreb
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import sys
import DB_manager
import timeit
from datetime import datetime

from mainmenu_v2117 import Ui_ProTemp


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(396, 209)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("badfavicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login.setWindowIcon(icon)
        self.lineEdit = QtWidgets.QLineEdit(login)
        self.lineEdit.setGeometry(QtCore.QRect(110, 20, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(login)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 70, 171, 30))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 74, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(login)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 291, 20))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(login)
        self.pushButton.setGeometry(QtCore.QRect(140, 120, 107, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Handel_Login)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "ProTemp Login v2.1.12 alfa"))
        self.lineEdit_2.setText(_translate("login", ""))
        self.label.setText(_translate("login", "Username"))
        self.label_2.setText(_translate("login", "Password"))
        self.pushButton.setText(_translate("login", "Login"))
        self.pushButton.setShortcut(_translate("login", "Return"))

#GUI END        

    def DB_test(self, database):
        database = 'medx'
        tableName = 'Department'
        UserName = self.lineEdit.text()
        Password = self.lineEdit_2.text()
        self.dbu = DB_manager.DatabaseUtility(database, tableName)
        
        table = self.dbu.GetTable()
        
        print(table[0])

        sql = "SELECT * FROM User "

        data = self.dbu.cursor.execute(sql)
        data1 = self.dbu.cursor.fetchall()
        print(data1)

        

    def Handel_Login(self):
        database = 'medx'
        UserName = self.lineEdit.text()
        Password = self.lineEdit_2.text()
        self.dbu = DB_manager.DatabaseUtility(database, tableName)

        sql = ''' SELECT * FROM User '''

        data1 = self.dbu.cursor.execute(sql)
        data = self.dbu.cursor.fetchall()
        #print(data)
        for row in data:
            if UserName == row[1] and Password == row[2]:
                print('user match')
                
                self.user_manage()
                print("Hello ", UserName)
                sql_user = ''' SELECT UserID FROM User WHERE UserName = %s '''
                self.dbu.cursor.execute(sql_user, [(UserName)])
                data_user = self.dbu.cursor.fetchone()   
                print(data_user[0])  
                date1 = datetime.now().strftime("%y-%m-%d")
                time = datetime.now().strftime("%H:%M")
                #sql_workspace = ''' INSERT INTO Coordinator_Workspace SET date = %s , UserID = %s '''
                sql_workspace = ''' INSERT INTO Coordinator_Workspace SET time = %s , date = %s , UserID = %s '''
                #self.dbu.cursor.execute(sql_workspace, [data_user[0]]) 
                self.dbu.cursor.execute(sql_workspace, [time, date1, data_user[0]]) 

                #self.db.commit()
                self.dbu.cnx.commit()
                self.openWindow1()
                sql = ''' SELECT * FROM User WHERE UserName = %s '''
                self.dbu.cursor.execute(sql, [(UserName)])
                data = self.dbu.cursor.fetchone()   
                print(data[0])    
                print(socket.gethostname())

            else:
                self.label_3.setText('Please check Username and Password')


    def user_manage(self):
        UserName = self.lineEdit.text()


        sql = ''' SELECT * FROM User WHERE UserName = %s '''
        self.dbu.cursor.execute(sql, [(UserName)])
        data = self.dbu.cursor.fetchone()   
        print(data[0:1])             


    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui1 = Ui_ProTemp()
        self.ui1.setupUi(self.window)
        self.window.show()


    def Coordinator_Audit(self):
        self.db = pymysql.connect(host='129.232.195.18', port=3306, user='root', password='',
                                  db='medx', use_unicode=True,
                                  charset='utf8')
        self.cur = self.db.cursor()


        self.cur.execute( '''  select UserID from Coordinator_Workspace ORDER BY id DESC LIMIT 1 ''')
        user_active = self.cur.fetchone()
        print("Printed immediately.")
        time.sleep(2.4)
        print("Printed after 2.4 seconds.")        
        print("Coordinator_Audit")
        print(user_active[0])        


if __name__ == "__main__":

    #db = 'myFirstDB'
    tableName = 'User'


    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QWidget()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
