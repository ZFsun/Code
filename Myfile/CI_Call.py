import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from CI import Ui_MainWindow
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

        # 按键信号与回调函数连接
        self.OpenDir.clicked.connect(self.OpenDirBntClicked)

    #########选择图片文件夹#########
    def OpenDirBntClicked(self):
        ImFolder = QtWidgets.QFileDialog.getExistingDirectory(None, "select folder", DefaultImFolder)  # 这个语句有些邪门
        if ImFolder != '':
            ImNameSet = os.listdir(ImFolder)
            ImNameSet.sort()
            ImPath = os.path.join(ImFolder, ImNameSet[0])
            pix = QtGui.QPixmap(ImPath)
            self.ImShow.setPixmap(pix)

            self.ImFolder = ImFolder
            self.ImNameSet = ImNameSet
            self.CurImId = 0
            _, SelectFolderName = os.path.split(ImFolder)
            CopyImFolderName = 'From{}CopyIm_{}-{}-{}-{}'.format(SelectFolderName, Month, Day, Hour, Minute)
            self.CopyImFolder = os.path.join(CurFolder, CopyImFolderName)

            _translate = QtCore.QCoreApplication.translate
            CurWinTitle = "检测工具                                                " + \
                          "                                                             " + \
                          SelectFolderName + '\\' + ImNameSet[0]
            self.MainWindow.setWindowTitle(_translate("MainWindow", CurWinTitle))
        else:
            print('请重新选择文件夹')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
