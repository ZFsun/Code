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
        MainWindow.resize(1348, 858)
        self.SaveDir = QtWidgets.QPushButton(MainWindow)
        self.SaveDir.setGeometry(QtCore.QRect(240, 770, 93, 28))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../labelme/labelme/icons/save-as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveDir.setIcon(icon)
        self.SaveDir.setObjectName("SaveDir")
        self.OpenDir = QtWidgets.QPushButton(MainWindow)
        self.OpenDir.setGeometry(QtCore.QRect(90, 770, 93, 28))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../labelme/labelme/icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OpenDir.setIcon(icon1)
        self.OpenDir.setObjectName("OpenDir")
        self.LastImg = QtWidgets.QPushButton(MainWindow)
        self.LastImg.setGeometry(QtCore.QRect(390, 770, 93, 28))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../labelme/labelme/icons/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LastImg.setIcon(icon2)
        self.LastImg.setObjectName("LastImg")
        self.NextImg = QtWidgets.QPushButton(MainWindow)
        self.NextImg.setGeometry(QtCore.QRect(540, 770, 93, 28))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../labelme/labelme/icons/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NextImg.setIcon(icon3)
        self.NextImg.setObjectName("NextImg")
        self.EnlargeImg = QtWidgets.QWidget(MainWindow)
        self.EnlargeImg.setGeometry(QtCore.QRect(790, 10, 501, 471))
        self.EnlargeImg.setObjectName("EnlargeImg")
        self.PenThicknessLabel = QtWidgets.QLabel(MainWindow)
        self.PenThicknessLabel.setGeometry(QtCore.QRect(850, 570, 72, 15))
        self.PenThicknessLabel.setObjectName("PenThicknessLabel")
        self.PenColorLabel = QtWidgets.QLabel(MainWindow)
        self.PenColorLabel.setGeometry(QtCore.QRect(850, 620, 72, 15))
        self.PenColorLabel.setObjectName("PenColorLabel")
        self.SaveImg = QtWidgets.QPushButton(MainWindow)
        self.SaveImg.setGeometry(QtCore.QRect(680, 770, 93, 28))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../labelme/labelme/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveImg.setIcon(icon4)
        self.SaveImg.setObjectName("SaveImg")
        self.PenThicknessSpinBox = QtWidgets.QSpinBox(MainWindow)
        self.PenThicknessSpinBox.setGeometry(QtCore.QRect(930, 570, 46, 22))
        self.PenThicknessSpinBox.setMaximum(10)
        self.PenThicknessSpinBox.setProperty("value", 5)
        self.PenThicknessSpinBox.setObjectName("PenThicknessSpinBox")
        self.PenColorComboBox = QtWidgets.QComboBox(MainWindow)
        self.PenColorComboBox.setGeometry(QtCore.QRect(930, 610, 87, 22))
        self.PenColorComboBox.setCurrentText("")
        self.PenColorComboBox.setObjectName("PenColorComboBox")
        self.ImgShowLabel = QtWidgets.QLabel(MainWindow)
        self.ImgShowLabel.setGeometry(QtCore.QRect(20, 10, 741, 691))
        self.ImgShowLabel.setText("")
        self.ImgShowLabel.setScaledContents(True)
        self.ImgShowLabel.setObjectName("ImgShowLabel")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.SaveDir.setText(_translate("MainWindow", "保存路径"))
        self.OpenDir.setText(_translate("MainWindow", "打开目录"))
        self.LastImg.setText(_translate("MainWindow", "上一张"))
        self.NextImg.setText(_translate("MainWindow", "下一张"))
        self.PenThicknessLabel.setText(_translate("MainWindow", "粗细"))
        self.PenColorLabel.setText(_translate("MainWindow", "颜色"))
        self.SaveImg.setText(_translate("MainWindow", "保存"))
