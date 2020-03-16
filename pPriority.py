from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow


class PanelPriority(QMainWindow):
    def __init__(self):
        super(PanelPriority, self).__init__()
        self.setGeometry(0, 0, 850, 650)

        # Font
        self.fontB = QtGui.QFont()
        self.fontB.setFamily("Arial")
        self.fontB.setPointSize(9)
        self.fontB.setBold(True)
        self.fontB.setWeight(75)

        self.font = QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(9)
        self.font.setBold(False)
        ###########

        # Previous Button
        self.previous = QtWidgets.QPushButton(self)
        self.previous.setGeometry(QtCore.QRect(550, 580, 120, 50))
        self.previous.setFont(self.font)
        self.previous.setText("Previous")

        # Next Button
        self.submit = QtWidgets.QPushButton(self)
        self.submit.setGeometry(QtCore.QRect(700, 580, 120, 50))
        self.submit.setFont(self.fontB)
        self.submit.setText("Submit")

        #
