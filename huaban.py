# coding: utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time


class SimpleDrawingBoard(QWidget):
    win = ''
    wins = []

    @classmethod
    def showWin(cls):
        # 关闭原窗口，创建新窗口
        # cls.win = cls()
        # cls.win.show()

        # 聚焦到已有窗口
        if not cls.win:
            cls.win = cls()
            cls.win.show()
        else:
            cls.win.activateWindow()

        # 新建窗口，不关闭原窗口
        # cls.wins.append(cls())
        # cls.wins[-1].show()

    def __init__(self, parent=None):
        super(SimpleDrawingBoard, self).__init__(parent)

        self.setWindowTitle(u"简易画板")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.size = (1080, 720)
        self.resize(*self.size)

        self.canvasSize = (950, 720)
        self.sizeOffset = [a - b for a, b in zip(self.size, self.canvasSize)]
        self.canvas = QPixmap(*self.canvasSize)
        self.canvas.fill(Qt.white)
        self.tempCanvas = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.isDrawing = False
        self.currentTool = u'铅笔'
        self.penSize = 5

        self.initUI()

    def initUI(self):
        # 工具
        self.toolsLabel = QLabel(u'工具')
        self.toolsComboBox = QComboBox()
        self.toolsComboBox.activated.connect(self.toolsComboBox_activated)
        self.toolsComboBox.addItem(u'铅笔')
        self.toolsComboBox.addItem(u'矩形')
        self.toolsComboBox.addItem(u'清空画布')
        self.toolsComboBox.addItem(u'橡皮擦')

        self.penSizeLabel = QLabel(u'画笔粗细')
        self.penSizeSpinBox = QSpinBox()
        self.penSizeSpinBox.setValue(self.penSize)
        self.penSizeSpinBox.valueChanged.connect(self.penSizeSpinBox_valueChanged)

        mainLayout = QVBoxLayout(self)

        toolbarLayout = QGridLayout()
        toolbarLayout.setSpacing(20)
        # toolbarLayout.setContentsMargins(0, 0, 0, 0) #设置边缘
        toolbarLayout.addWidget(self.toolsLabel, 0, 0, 1, 1)
        toolbarLayout.addWidget(self.toolsComboBox, 1, 0, 1, 1)
        self.toolsComboBox.setFixedWidth(100)  # 下拉框尺寸
        toolbarLayout.addWidget(self.penSizeLabel, 2, 0, 1, 1)
        toolbarLayout.addWidget(self.penSizeSpinBox, 3, 0, 1, 1)
        # toolbarLayout.addWidget(self.placeholder3, 4, 0, 1, 1)

        toolbarLayout.setAlignment(Qt.AlignLeft)

        mainLayout.addLayout(toolbarLayout)
        mainLayout.addStretch(1)

    def toolsComboBox_activated(self):
        # 设置当前工具
        self.currentTool = self.toolsComboBox.currentText()
        print
        u'当前工具: {}'.format(self.currentTool)

    def penSizeSpinBox_valueChanged(self):
        # 设置画笔粗细
        self.penSize = self.penSizeSpinBox.value()

    def paintEvent(self, event):

        if self.currentTool == u'铅笔':

            pp = QPainter(self.canvas)
            pen = QPen(QColor(0, 0, 0), self.penSize)
            pp.setPen(pen)
            if self.lastPoint != self.endPoint:
                pp.drawLine(self.lastPoint - QPoint(*self.sizeOffset), self.endPoint - QPoint(*self.sizeOffset))
            painter = QPainter(self)
            painter.drawPixmap(self.sizeOffset[0], self.sizeOffset[1], self.canvas)
            self.lastPoint = self.endPoint

        elif self.currentTool == u'矩形':
            painter = QPainter(self)
            x = self.lastPoint.x()
            y = self.lastPoint.y()
            w = self.endPoint.x() - x
            h = self.endPoint.y() - y

            if self.isDrawing:
                self.tempCanvas = self.canvas.copy()
                pp = QPainter(self.tempCanvas)
                pen = QPen(Qt.black, self.penSize)
                pp.setPen(pen)
                pp.drawRect(x - self.sizeOffset[0], y - self.sizeOffset[1], w, h)
                painter.drawPixmap(self.sizeOffset[0], self.sizeOffset[1], self.tempCanvas)
            else:
                pp = QPainter(self.canvas)
                pen = QPen(Qt.black, self.penSize)
                pp.setPen(pen)
                pp.drawRect(x - self.sizeOffset[0], y - self.sizeOffset[1], w, h)
                painter.drawPixmap(self.sizeOffset[0], self.sizeOffset[1], self.canvas)
                self.lastPoint = self.endPoint


        elif self.currentTool == u'清空画布':
            self.canvas.fill(Qt.white)
            painter = QPainter(self)
            painter.drawPixmap(self.sizeOffset[0], self.sizeOffset[1], self.canvas)
            self.lastPoint = self.endPoint

        elif self.currentTool == u'橡皮擦':
            pp = QPainter(self.canvas)
            pen = QPen(Qt.white, self.penSize)
            pp.setPen(pen)
            if self.lastPoint != self.endPoint:
                pp.drawLine(self.lastPoint - QPoint(*self.sizeOffset), self.endPoint - QPoint(*self.sizeOffset))
            self.lastPoint = self.endPoint
            painter = QPainter(self)
            painter.drawPixmap(self.sizeOffset[0], self.sizeOffset[1], self.canvas)

    def mousePressEvent(self, event):
        # 按下左键
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint
            print(u'进入忘我之境, 祭起 {}'.format(self.currentTool))
            self.startTime = time.time()
            self.isDrawing = True

    def mouseMoveEvent(self, event):
        if self.isDrawing == True:
            self.update()
            self.endPoint = event.pos()

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.isDrawing = False
            self.endTime = time.time()
            print(u'出境。此次行功总计 {} 瞬'.format(round(self.endTime - self.startTime, 2)))
            self.endPoint = event.pos()
            self.update()


if __name__ == '__main__':

    # SimpleDrawingBoard.showWin()
    # app = QApplication.instance() or QApplication(sys.argv)
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    SimpleDrawingBoard.showWin()
    app.exec_()