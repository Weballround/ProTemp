#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue January  21 10:41 2019

Last Updated Tue January  18 12:07 2019

@author: pierreb
"""

from clickatell.http import Http
from clickatell import Transport

cellnumber = '0814777563'
message1 = 'It Works!'

clickatell = Http('ClMitdv4RUCZAVRr3mAuaQ==')
response = clickatell.sendMessage(['+27814777563'], "It Works!")
print(cellnumber)
print(message1)
#self.getBalance()
#print(response) #Returns the headers with all the messages

for entry in response['messages']:
    print(entry) #Returns all the message details per message
    #print(entry['apiMessageId'])
    #print(entry['to'])
    #print(entry['accepted'])
    #print(entry['error'])

#    def sendMessage(self, to, message, extra={})
#    def getBalance(self):
#        return