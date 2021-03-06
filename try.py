# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'waitinglist.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
# from regform import Ui_registerform
import regform
from amu_database import getContent, getListSize, getDetails, deletePat
from PyQt5.QtCore import QTimer, QTime, Qt
import time


class Ui_waitlist(object):
    def addPatient(self):
        self.window = QtWidgets.QGroupBox()
        self.ui = regform.Ui_registerform()
        self.ui.setupUi(self.window, waitlist)
        self.window.show()
    
    def timing(self, seconds):
        mins, secs = divmod(seconds, 60)
        hours, minutes = divmod(mins, 60)
        return int(hours), int(minutes), int(secs)

    def getTimeElapsed(self, starttime, row):
        global timenow
        timenow= int(time.time())
        t= QtWidgets.QLabel()
        timeelapsed= timenow-starttime
        hours, mins, secs= self.timing(timeelapsed)
        timeelapsed= '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        t.setText(timeelapsed)
        self.tableWidget.setCellWidget(row, 4, t)
    
    # def displayList(self):
        # size= getListSize() # from here, this is the function to update the waitlist from registrations saved in the database
        # self.tableWidget.setRowCount(size) #setting the table row size
        # row= 0 
        # listnow= getContent() # get the waitlist in the database as a list
        # for patient in listnow: #looping through each row of waitlist and add it to the table
        #     self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(("Name: {} {} \nAge: {} \nGender: {}").format(patient[0], patient[1], patient[2],patient[3])))
        #     self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(patient[4]))
        #     self.tableWidget.setRowHeight(row, 70)
        #     checkBox = QtWidgets.QCheckBox()
        #     checkBox.setGeometry(QtCore.QRect(260, 230, 21, 20))
        #     checkBox.setChecked(patient[6])
        #     btn = QtWidgets.QPushButton()
        #     btn.setText("Delete")
        #     dest= QtWidgets.QComboBox()
        #     dest.setFocusPolicy(QtCore.Qt.StrongFocus)
        #     dest.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        #     dest.setEditable(False)
        #     dest.addItem("Select")
        #     dest.addItem("Discharge Lounge")
        #     dest.addItem("Downstream Ward")
        #     ward= QtWidgets.QLineEdit()
        #     ward.setPlaceholderText("ward location")
        #     self.w= QtWidgets.QWidget()
        #     self.w.layout = QtWidgets.QVBoxLayout()
        #     self.w.layout.addWidget(dest)
        #     self.w.layout.addWidget(ward)
        #     self.w.setLayout(self.w.layout)
    
        #     self.tableWidget.setCellWidget(row, 2, checkBox)
        #     self.tableWidget.setCellWidget(row, 3, self.w)
        #     row = row+1
    
    def setupUi(self, waitlist):
        waitlist.setObjectName("waitlist")
        waitlist.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(waitlist)
        self.centralwidget.setObjectName("centralwidget")
        self.newpatient = QtWidgets.QPushButton(self.centralwidget)
        self.newpatient.setGeometry(QtCore.QRect(632, 30, 131, 32))
        self.newpatient.setObjectName("newpatient")
        self.delpatient = QtWidgets.QPushButton(self.centralwidget)
        self.delpatient.setGeometry(QtCore.QRect(510, 30, 113, 32))
        self.delpatient.setObjectName("delpatient")
        # self.delpatient.clicked.connect(self.deletePatient)
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(290, 30, 171, 51))
        self.title.setStyleSheet("font: 25pt \"Avenir Next\";")
        self.title.setObjectName("title")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 90, 731, 441))
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.setColumnWidth(0,190)
        self.tableWidget.setColumnWidth(1,190)
        self.tableWidget.setColumnWidth(2,100)
        self.tableWidget.setColumnWidth(3,120)
        self.tableWidget.setColumnWidth(4,125)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) # does not allow editing to the table
        waitlist.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(waitlist)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        waitlist.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(waitlist)
        self.statusbar.setObjectName("statusbar")
        waitlist.setStatusBar(self.statusbar)
        size= getListSize() # from here, this is the function to update the waitlist from registrations saved in the database
        self.tableWidget.setRowCount(size) #setting the table row size
        row= 0 
        listnow= getContent() # get the waitlist in the database as a list
        for patient in listnow: #looping through each row of waitlist and add it to the table
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(("Name: {} {} \nAge: {} \nGender: {}").format(patient[0], patient[1], patient[2],patient[3])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(patient[4]))
            self.tableWidget.setRowHeight(row, 70)
            checkBox = QtWidgets.QCheckBox()
            checkBox.setGeometry(QtCore.QRect(260, 230, 21, 20))
            checkBox.setChecked(patient[6])
            btn = QtWidgets.QPushButton()
            btn.setText("Delete")
            dest= QtWidgets.QComboBox()
            dest.setFocusPolicy(QtCore.Qt.StrongFocus)
            dest.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
            dest.setEditable(False)
            dest.addItem("Select")
            dest.addItem("Discharge Lounge")
            dest.addItem("Downstream Ward")
            ward= QtWidgets.QLineEdit()
            ward.setPlaceholderText("ward location")
            self.w= QtWidgets.QWidget()
            self.w.layout = QtWidgets.QVBoxLayout()
            self.w.layout.addWidget(dest)
            self.w.layout.addWidget(ward)
            self.w.setLayout(self.w.layout)
    
            self.tableWidget.setCellWidget(row, 2, checkBox)
            self.tableWidget.setCellWidget(row, 3, self.w)
            row = row+1

        self.newpatient.clicked.connect(self.addPatient)

        self.retranslateUi(waitlist)
        QtCore.QMetaObject.connectSlotsByName(waitlist)


    def retranslateUi(self, waitlist):
        _translate = QtCore.QCoreApplication.translate
        waitlist.setWindowTitle(_translate("waitlist", "Waiting List"))
        self.newpatient.setText(_translate("waitlist", "Add New Patient"))
        self.delpatient.setText(_translate("waitlist","Delete Patient"))
        self.title.setText(_translate("waitlist", "Waiting List"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("waitlist", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("waitlist", "Diagnosis"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("waitlist", "Isolation"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("waitlist", "discharge summary"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("waitlist", "Timer"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    waitlist = QtWidgets.QMainWindow()
    ui = Ui_waitlist()
    ui.setupUi(waitlist)
    waitlist.show()
    sys.exit(app.exec_())
