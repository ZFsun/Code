# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScanImTool.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1193, 747)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.OpenDirBnt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.OpenDirBnt.setFont(font)
        self.OpenDirBnt.setIconSize(QtCore.QSize(20, 20))
        self.OpenDirBnt.setObjectName("OpenDirBnt")
        self.verticalLayout.addWidget(self.OpenDirBnt)
        self.PreImBnt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PreImBnt.setFont(font)
        self.PreImBnt.setObjectName("PreImBnt")
        self.verticalLayout.addWidget(self.PreImBnt)
        self.NextImBnt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.NextImBnt.setFont(font)
        self.NextImBnt.setObjectName("NextImBnt")
        self.verticalLayout.addWidget(self.NextImBnt)
        self.CopyCurImBnt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.CopyCurImBnt.setFont(font)
        self.CopyCurImBnt.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.CopyCurImBnt.setFlat(False)
        self.CopyCurImBnt.setObjectName("CopyCurImBnt")
        self.verticalLayout.addWidget(self.CopyCurImBnt)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.ImShowLabel = QtWidgets.QLabel(self.centralwidget)
        self.ImShowLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ImShowLabel.setText("")
        self.ImShowLabel.setObjectName("ImShowLabel")
        self.horizontalLayout.addWidget(self.ImShowLabel)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 8)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1193, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ################button按钮点击事件回调函数################
        self.OpenDirBnt.clicked.connect(self.OpenDirBntClicked)
        self.NextImBnt.clicked.connect(self.NextImBntClicked)
        self.PreImBnt.clicked.connect(self.PreImBntClicked)
        self.CopyCurImBnt.clicked.connect(self.CopyCurImBntClicked)

        self.MainWindow = MainWindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图片查看器"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p>t</p></body></html>"))
        self.OpenDirBnt.setText(_translate("MainWindow", "打开目录"))
        self.PreImBnt.setText(_translate("MainWindow", "上一张图"))
        self.NextImBnt.setText(_translate("MainWindow", "下一张图"))
        self.CopyCurImBnt.setText(_translate("MainWindow", "拷贝当前图"))
        self.ImShowLabel.setToolTip(_translate("MainWindow", "Image Show Region"))
