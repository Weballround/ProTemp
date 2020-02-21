#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Thu November  21 09:41 2018

Last Updated Thu January  06 16:07 2020

@author: pierreb
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import socket



def ConCon():
    mydb = pymysql.connect(
    host="129.232.195.18",
    user="pierreb",
    passwd="Springboks2017"
    )

    print(mydb)

    return True

