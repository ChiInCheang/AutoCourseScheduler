from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QSpacerItem,QSizePolicy,QTreeWidgetItem
from PyQt5.QtCore import Qt


class PanelCourse(QMainWindow):
    def __init__(self):
        super(PanelCourse, self).__init__()
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 850, 650))
        self.setCentralWidget(self.widget)
        self.layout = QVBoxLayout(self.widget)      # Overall vertical layout

        # Font
        self.font = QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(9)
        self.setFont(self.font)

        # Search Bar
        self.searchBar = QtWidgets.QLineEdit(self.widget)
        self.searchBar.setClearButtonEnabled(True)
        # Search Button
        self.search = QtWidgets.QPushButton(self.widget)
        self.search.setText("Search")
        # Spacer 1
        self.spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # Course List
        self.courseList = QtWidgets.QTreeWidget(self.widget)
        # Selected Course List
        self.courseSelected = QtWidgets.QTreeWidget(self)
        # Spacer 2
        self.spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # Add Button
        self.add = QtWidgets.QPushButton(self)
        self.add.setText("Add")
        # Remove Button
        self.remove = QtWidgets.QPushButton(self)
        self.remove.setText("Remove")
        # Spacer 3
        self.spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # Spacer 4
        self.spacerItem4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # Next Button
        self.next = QtWidgets.QPushButton(self)
        self.next.setText("Next")

        # Horizontal layout 1
        self.hl1 = QHBoxLayout(self.widget)
        self.hl1.addWidget(self.searchBar)
        self.hl1.addWidget(self.search)
        self.hl1.addItem(self.spacerItem1)

        # Horizontal layout 2   (Course Lists)
        self.hl2 = QHBoxLayout(self.widget)
        self.hl2.addWidget(self.courseList)
        self.hl2.addWidget(self.courseSelected)

        # Horizontal layout 3   (Add/Remove Button)
        self.hl3 = QHBoxLayout(self.widget)
        self.hl3.addItem(self.spacerItem2)
        self.hl3.addWidget(self.add)
        self.hl3.addWidget(self.remove)
        self.hl3.addItem(self.spacerItem3)

        # Horizontal layout 4   (Panel Switching Button)
        self.hl4 = QHBoxLayout(self.widget)
        self.hl4.addItem(self.spacerItem4)
        self.hl4.addWidget(self.next)

        # Overall layout
        self.layout.addLayout(self.hl1)
        self.layout.addLayout(self.hl2)
        self.layout.addLayout(self.hl3)
        self.layout.addLayout(self.hl4)

        # Call the Item Event
        self.courseListEvent()


    def courseListEvent(self):
        self.courseList.headerItem = QTreeWidgetItem()
        self.courseList.setHeaderLabel("Course Available")

        self.courseList.item = QTreeWidgetItem()

        for i in range(3):  # numSelectedCourse
            parent = QTreeWidgetItem(self.courseList)
            parent.setText(0, "Parent {}".format(i))  # Course Name
            parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            for x in range(5):  # numCourseSection
                child = QTreeWidgetItem(parent)
                child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                child.setText(0, "Child {}".format(x))  # Instructor Name
                child.setCheckState(0, Qt.Checked)  # By default all checked

    def selectedListEvent(self):
        pass

    def addButtonEvent(self):
        pass

    def removeButtonEvent(self):
        pass
