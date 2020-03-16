from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow


class PanelCourse(QMainWindow):
    def __init__(self):
        super(PanelCourse, self).__init__()
        self.setGeometry(0, 0, 850, 650)

        # Font
        self.font = QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(9)
        self.setFont(self.font)

        # Search Bar
        self.searchBar = QtWidgets.QLineEdit(self)
        self.searchBar.setGeometry(QtCore.QRect(30, 30, 270, 30))
        self.searchBar.setClearButtonEnabled(True)

        # Search Button
        self.search = QtWidgets.QPushButton(self)
        self.search.setGeometry(QtCore.QRect(330, 30, 130, 30))
        self.search.setText("Search")

        # Course List
        self.courseList = QtWidgets.QTreeWidget(self)
        self.courseList.setGeometry(QtCore.QRect(30, 90, 360, 450))
        self.courseList.headerItem().setText(0, "1")

        # Selected Course List
        self.courseSelected = QtWidgets.QTreeWidget(self)
        self.courseSelected.setGeometry(QtCore.QRect(440, 90, 380, 450))
        self.courseSelected.headerItem().setText(0, "1")

        # Add Button
        self.add = QtWidgets.QPushButton(self)
        self.add.setGeometry(QtCore.QRect(240, 560, 150, 50))
        self.add.setText("Add")

        # Remove Button
        self.remove = QtWidgets.QPushButton(self)
        self.remove.setGeometry(QtCore.QRect(440, 560, 150, 50))
        self.remove.setText("Remove")

        # Next Button
        self.next = QtWidgets.QPushButton(self)
        self.next.setGeometry(QtCore.QRect(700, 580, 120, 50))
        self.next.setText("Next")

        #####
