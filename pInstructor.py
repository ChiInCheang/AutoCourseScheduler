from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow


class PanelInstructor(QMainWindow):
    def __init__(self):
        super(PanelInstructor, self).__init__()
        self.setGeometry(0, 0, 850, 650)

        # Font
        self.font = QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(9)
        self.setFont(self.font)

        self.fontL = QtGui.QFont()
        self.fontL.setFamily("Arial")
        self.fontL.setPointSize(10)
        self.fontL.setBold(True)
        self.fontL.setWeight(75)
        ##########

        # Instructor filter
        self.filter = QtWidgets.QTreeView(self)
        self.filter.setGeometry(QtCore.QRect(30, 90, 790, 450))

        # Next Button
        self.next = QtWidgets.QPushButton(self)
        self.next.setGeometry(QtCore.QRect(700, 580, 120, 50))
        self.next.setText("Next")

        # Previous Button
        self.previous = QtWidgets.QPushButton(self)
        self.previous.setGeometry(QtCore.QRect(550, 580, 120, 50))
        self.previous.setText("Previous")

        # Label "Instructor Filter"
        self.title = QtWidgets.QLabel(self)
        self.title.setGeometry(QtCore.QRect(30, 30, 150, 50))
        self.title.setText("Instructor Filter")
        self.title.setFont(self.fontL)

        #####