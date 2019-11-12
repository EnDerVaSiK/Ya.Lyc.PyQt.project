# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'man_set.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Manual_SettingsWindow(object):
    def setupUi(self, Manual_SettingsWindow):
        Manual_SettingsWindow.setObjectName("Manual_SettingsWindow")
        Manual_SettingsWindow.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(Manual_SettingsWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 0, 325, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rm_col = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rm_col.setFont(font)
        self.rm_col.setObjectName("rm_col")
        self.verticalLayout.addWidget(self.rm_col)
        self.red_col = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.red_col.setFont(font)
        self.red_col.setObjectName("red_col")
        self.verticalLayout.addWidget(self.red_col)
        self.green_col = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.green_col.setFont(font)
        self.green_col.setObjectName("green_col")
        self.verticalLayout.addWidget(self.green_col)
        self.blue_col = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.blue_col.setFont(font)
        self.blue_col.setObjectName("blue_col")
        self.verticalLayout.addWidget(self.blue_col)
        self.manual_col = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.manual_col.setFont(font)
        self.manual_col.setObjectName("manual_col")
        self.verticalLayout.addWidget(self.manual_col)
        self.acceptbtn = QtWidgets.QPushButton(Manual_SettingsWindow)
        self.acceptbtn.setGeometry(QtCore.QRect(150, 260, 93, 28))
        self.acceptbtn.setObjectName("acceptbtn")

        self.retranslateUi(Manual_SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(Manual_SettingsWindow)

    def retranslateUi(self, Manual_SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        Manual_SettingsWindow.setWindowTitle(_translate("Manual_SettingsWindow", "Свои настройки"))
        self.rm_col.setText(_translate("Manual_SettingsWindow", "Случайно изменять цвет кнопки"))
        self.red_col.setText(_translate("Manual_SettingsWindow", "Сделать кнопку красной"))
        self.green_col.setText(_translate("Manual_SettingsWindow", "Сделать кнопку зеленой"))
        self.blue_col.setText(_translate("Manual_SettingsWindow", "Сделать кнопку синей"))
        self.manual_col.setText(_translate("Manual_SettingsWindow", "Выбрать цвет самому"))
        self.acceptbtn.setText(_translate("Manual_SettingsWindow", "Принять"))
