# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GameWindow(object):
    def setupUi(self, GameWindow):
        GameWindow.setObjectName("GameWindow")
        GameWindow.resize(500, 400)
        GameWindow.setMinimumSize(QtCore.QSize(500, 400))
        GameWindow.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(GameWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.beginbtn = QtWidgets.QPushButton(self.centralwidget)
        self.beginbtn.setGeometry(QtCore.QRect(10, 50, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.beginbtn.setFont(font)
        self.beginbtn.setObjectName("beginbtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.runner = QtWidgets.QPushButton(self.centralwidget)
        self.runner.setGeometry(QtCore.QRect(200, 100, 150, 150))
        self.runner.setText("")
        self.runner.setObjectName("runner")
        self.dark = QtWidgets.QRadioButton(self.centralwidget)
        self.dark.setEnabled(True)
        self.dark.setGeometry(QtCore.QRect(10, 120, 111, 20))
        self.dark.setCheckable(True)
        self.dark.setChecked(False)
        self.dark.setObjectName("dark")
        GameWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GameWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menumenuAbout = QtWidgets.QMenu(self.menubar)
        self.menumenuAbout.setObjectName("menumenuAbout")
        GameWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GameWindow)
        self.statusbar.setObjectName("statusbar")
        GameWindow.setStatusBar(self.statusbar)
        self.Menu_Difficulty = QtWidgets.QAction(GameWindow)
        self.Menu_Difficulty.setObjectName("Menu_Difficulty")
        self.Manual_Settings = QtWidgets.QAction(GameWindow)
        self.Manual_Settings.setObjectName("Manual_Settings")
        self.About_program = QtWidgets.QAction(GameWindow)
        self.About_program.setObjectName("About_program")
        self.menuMenu.addAction(self.Menu_Difficulty)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.Manual_Settings)
        self.menumenuAbout.addAction(self.About_program)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menumenuAbout.menuAction())

        self.retranslateUi(GameWindow)
        QtCore.QMetaObject.connectSlotsByName(GameWindow)

    # def black_style(self, GameWindow):
    #     GameWindow.setStyleSheet('background-color: black')

    def retranslateUi(self, GameWindow):
        _translate = QtCore.QCoreApplication.translate
        self.beginbtn.setText(_translate("GameWindow", "Старт"))
        self.label.setText(_translate("GameWindow", "00:20"))
        self.dark.setText(_translate("GameWindow", "Темная тема"))
        self.menuMenu.setTitle(_translate("GameWindow", "Меню"))
        self.menumenuAbout.setTitle(_translate("GameWindow", "Справка"))
        self.Menu_Difficulty.setText(_translate("GameWindow", "Сложность"))
        self.Manual_Settings.setText(_translate("GameWindow", "Свои настройки"))
        self.About_program.setText(_translate("GameWindow", "О программе"))
