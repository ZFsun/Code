# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1312, 835)
        self.ImgShow = QtWidgets.QWidget(MainWindow)
        self.ImgShow.setGeometry(QtCore.QRect(10, 10, 751, 741))
        self.ImgShow.setObjectName("ImgShow")
        self.SaveDir = QtWidgets.QPushButton(MainWindow)
        self.SaveDir.setGeometry(QtCore.QRect(240, 770, 93, 28))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../labelme/labelme/icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveDir.setIcon(icon)
        self.SaveDir.setObjectName("SaveDir")
        self.OpenDir = QtWidgets.QPushButton(MainWindow)
        self.OpenDir.setGeometry(QtCore.QRect(90, 770, 93, 28))
        self.OpenDir.setIcon(icon)
        self.OpenDir.setObjectName("OpenDir")
        self.LastImg = QtWidgets.QPushButton(MainWindow)
        self.LastImg.setGeometry(QtCore.QRect(390, 770, 93, 28))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../labelme/labelme/icons/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LastImg.setIcon(icon1)
        self.LastImg.setObjectName("LastImg")
        self.NextImg = QtWidgets.QPushButton(MainWindow)
        self.NextImg.setGeometry(QtCore.QRect(540, 770, 93, 28))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../labelme/labelme/icons/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NextImg.setIcon(icon2)
        self.NextImg.setObjectName("NextImg")
        self.EnlargeImg = QtWidgets.QWidget(MainWindow)
        self.EnlargeImg.setGeometry(QtCore.QRect(790, 10, 501, 471))
        self.EnlargeImg.setObjectName("EnlargeImg")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(850, 570, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(850, 620, 72, 15))
        self.label_2.setObjectName("label_2")
        self.SaveImg = QtWidgets.QPushButton(MainWindow)
        self.SaveImg.setGeometry(QtCore.QRect(680, 770, 93, 28))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../labelme/labelme/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveImg.setIcon(icon3)
        self.SaveImg.setObjectName("SaveImg")
        self.spinBox = QtWidgets.QSpinBox(MainWindow)
        self.spinBox.setGeometry(QtCore.QRect(930, 570, 46, 22))
        self.spinBox.setMaximum(10)
        self.spinBox.setProperty("value", 5)
        self.spinBox.setObjectName("spinBox")
        self.comboBox = QtWidgets.QComboBox(MainWindow)
        self.comboBox.setGeometry(QtCore.QRect(930, 610, 87, 22))
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.SaveDir.setText(_translate("MainWindow", "保存路径"))
        self.OpenDir.setText(_translate("MainWindow", "打开目录"))
        self.LastImg.setText(_translate("MainWindow", "上一张"))
        self.NextImg.setText(_translate("MainWindow", "下一张"))
        self.label.setText(_translate("MainWindow", "粗细"))
        self.label_2.setText(_translate("MainWindow", "颜色"))
        self.SaveImg.setText(_translate("MainWindow", "保存"))
