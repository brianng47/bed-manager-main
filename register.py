# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from amu_database import addtowaitlist, getLast


class Ui_regform1(object):
    def addedPatient(self, reg_win, wait_win):
        # print(self.genderBox.currentText())
        # print(self.ageBox.text())
        addtowaitlist(self.first.text(), self.last.text(), self.ageBox.text(), self.genderBox.currentText(), self.diagnosis.toPlainText())
        print(getLast(1))
        wait_win.show()
        reg_win.hide()

    def setupUi(self, regform1):
        regform1.setObjectName("regform1")
        regform1.resize(609, 501)
        self.name = QtWidgets.QLabel(regform1)
        self.name.setGeometry(QtCore.QRect(49, 30, 71, 20))
        self.name.setObjectName("name")
        self.firstEdit = QtWidgets.QLineEdit(regform1)
        self.firstEdit.setGeometry(QtCore.QRect(120, 30, 411, 21))
        self.firstEdit.setObjectName("firstEdit")
        self.last = QtWidgets.QLabel(regform1)
        self.last.setGeometry(QtCore.QRect(50, 70, 71, 16))
        self.last.setObjectName("last")
        self.lastEdit = QtWidgets.QLineEdit(regform1)
        self.lastEdit.setGeometry(QtCore.QRect(120, 70, 411, 21))
        self.lastEdit.setObjectName("lastEdit")
        self.age = QtWidgets.QLabel(regform1)
        self.age.setGeometry(QtCore.QRect(50, 110, 60, 16))
        self.age.setObjectName("age")
        self.ageBox = QtWidgets.QSpinBox(regform1)
        self.ageBox.setGeometry(QtCore.QRect(120, 110, 48, 24))
        self.ageBox.setObjectName("ageBox")
        self.gender = QtWidgets.QLabel(regform1)
        self.gender.setGeometry(QtCore.QRect(50, 150, 60, 16))
        self.gender.setObjectName("gender")
        self.genderBox = QtWidgets.QComboBox(regform1)
        self.genderBox.setGeometry(QtCore.QRect(120, 150, 104, 26))
        self.genderBox.setObjectName("genderBox")
        self.diagtext = QtWidgets.QLabel(regform1)
        self.diagtext.setGeometry(QtCore.QRect(50, 190, 121, 16))
        self.diagtext.setObjectName("diagtext")
        self.diagnosis = QtWidgets.QTextEdit(regform1)
        self.diagnosis.setGeometry(QtCore.QRect(50, 220, 501, 221))
        self.diagnosis.setObjectName("diagnosis")
        self.pushButton = QtWidgets.QPushButton(regform1, clicked = lambda: self.addedPatient(registerform, waitlist))
        self.pushButton.setGeometry(QtCore.QRect(240, 450, 113, 32))
        self.pushButton.setShortcut("")
        self.pushButton.setObjectName("pushButton")
        self.genderBox.addItem("Select")
        self.genderBox.addItem("Male")
        self.genderBox.addItem("Female")

        self.retranslateUi(regform1)
        QtCore.QMetaObject.connectSlotsByName(regform1)

    def retranslateUi(self, regform1):
        _translate = QtCore.QCoreApplication.translate
        regform1.setWindowTitle(_translate("regform1", "New Patient Registration"))
        self.name.setText(_translate("regform1", "First name:"))
        self.last.setText(_translate("regform1", "Last name:"))
        self.age.setText(_translate("regform1", "Age:"))
        self.gender.setText(_translate("regform1", "Gender:"))
        self.diagtext.setText(_translate("regform1", "Top-line Diagnosis"))
        self.pushButton.setText(_translate("regform1", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    regform1 = QtWidgets.QWidget()
    ui = Ui_regform1()
    ui.setupUi(regform1)
    regform1.show()
    sys.exit(app.exec_())
