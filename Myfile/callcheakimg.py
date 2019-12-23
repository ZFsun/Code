import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from cheakimg_ui import *
import shutil
import os
import datetime

CurFolder = os.getcwd()
DefaultImFolder = CurFolder
NowTime = datetime.datetime.now()
Month = str(NowTime.month).zfill(2)
Day = str(NowTime.day).zfill(2)
Hour = str(NowTime.hour).zfill(2)
Minute = str(NowTime.minute).zfill(2)


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        ################定义相关变量并初始化################
        self.ImFolder = ''  # 图片文件夹路径
        self.ImNameSet = []  # 图片集合
        self.CurImId = 0  # 当前显示图在集合中的编号
        self.CopyImFolder = ''  # Copy图片存放的文件夹

    #########选择图片文件夹#########
    def OpenDirBntClicked(self):
        ImFolder = QtWidgets.QFileDialog.getExistingDirectory(None, "select folder", DefaultImFolder)  # 这个语句有些邪门
        if ImFolder != '':
            ImNameSet = os.listdir(ImFolder)
            ImNameSet.sort()
            ImPath = os.path.join(ImFolder, ImNameSet[0])
            pix = QtGui.QPixmap(ImPath)
            self.ImShowLabel.setPixmap(pix)

            self.ImFolder = ImFolder
            self.ImNameSet = ImNameSet
            self.CurImId = 0
            _, SelectFolderName = os.path.split(ImFolder)
            CopyImFolderName = 'From{}CopyIm_{}-{}-{}-{}'.format(SelectFolderName, Month, Day, Hour, Minute)
            self.CopyImFolder = os.path.join(CurFolder, CopyImFolderName)

            _translate = QtCore.QCoreApplication.translate
            CurWinTitle = "看图工具1.0                                                " + \
                          "                                                             " + \
                          SelectFolderName + '\\' + ImNameSet[0]
            self.MainWindow.setWindowTitle(_translate("MainWindow", CurWinTitle))
        else:
            print('请重新选择文件夹')

    #########显示下一张图片 #########
    def NextImBntClicked(self):
        ImFolder = self.ImFolder
        ImNameSet = self.ImNameSet
        CurImId = self.CurImId
        ImNum = len(ImNameSet)
        if CurImId < ImNum - 1:  # 不可循环看图
            ImPath = os.path.join(ImFolder, ImNameSet[CurImId + 1])
            pix = QtGui.QPixmap(ImPath)
            self.ImShowLabel.setPixmap(pix)
            self.CurImId = CurImId + 1

            _, SelectFolderName = os.path.split(ImFolder)
            _translate = QtCore.QCoreApplication.translate
            CurWinTitle = "审查图片                                                " + \
                          "                                                             " + \
                          SelectFolderName + '\\' + ImNameSet[CurImId + 1]
            self.MainWindow.setWindowTitle(_translate("MainWindow", CurWinTitle))

    #########显示前一张图片 #########
    def PreImBntClicked(self):
        ImFolder = self.ImFolder
        ImNameSet = self.ImNameSet
        CurImId = self.CurImId
        ImNum = len(ImNameSet)
        if CurImId > 0:  # 第一张图片没有前一张
            ImPath = os.path.join(ImFolder, ImNameSet[CurImId - 1])
            pix = QtGui.QPixmap(ImPath)
            self.ImShowLabel.setPixmap(pix)
            self.CurImId = CurImId - 1

            _, SelectFolderName = os.path.split(ImFolder)
            _translate = QtCore.QCoreApplication.translate
            CurWinTitle = "看图工具1.0                                                " + \
                          "                                                             " + \
                          SelectFolderName + '\\' + ImNameSet[CurImId - 1]
            self.MainWindow.setWindowTitle(_translate("MainWindow", CurWinTitle))
        if self.CurImId < 0:
            self.CurImId = 0

    #########copy 当前图片函数 #########
    def CopyCurImBntClicked(self):
        ImFolder = self.ImFolder
        ImNameSet = self.ImNameSet
        CurImId = self.CurImId
        ImPath = os.path.join(ImFolder, ImNameSet[CurImId])
        CopyImFolder = self.CopyImFolder
        if not os.path.isdir(CopyImFolder):
            os.makedirs(CopyImFolder)
        shutil.copy(ImPath, CopyImFolder)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
