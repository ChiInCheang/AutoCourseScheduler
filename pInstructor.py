from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, \
    QSpacerItem, QSizePolicy, QTreeWidgetItem, QTreeWidget
from PyQt5.QtCore import Qt


class PanelInstructor(QMainWindow):
    def __init__(self):
        super(PanelInstructor, self).__init__()
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 850, 650))
        self.setCentralWidget(self.widget)
        self.layout = QVBoxLayout(self.widget)  # Overall vertical layout
        self.layout.setSpacing(15)

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

        # Label "Instructor Filter"
        self.title = QtWidgets.QLabel(self.widget)
        self.title.setText("Instructor Filter")
        self.title.setFont(self.fontL)
        # Instructor filter
        self.filter = QTreeWidget(self.widget)
        self.filterEvent()
        # Spacer
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # Previous Button
        self.previous = QtWidgets.QPushButton(self.widget)
        self.previous.setText("Previous")
        # Next Button
        self.next = QtWidgets.QPushButton(self.widget)
        self.next.setText("Next")

        # Horizontal layout
        self.hl = QHBoxLayout(self.widget)
        self.hl.setContentsMargins(0, 0, 0, 0)
        self.hl.addItem(spacerItem)
        self.hl.addWidget(self.previous)
        self.hl.addWidget(self.next)
        # Overall layout
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.filter)
        self.layout.addLayout(self.hl)
        #####

    def filterEvent(self):
        self.filter.headerItem = QTreeWidgetItem()
        self.filter.setHeaderLabel("Instructors by Course")

        self.filter.item = QTreeWidgetItem()

        for i in range(3):  # numSelectedCourse
            parent = QTreeWidgetItem(self.filter)
            parent.setText(0, "Parent {}".format(i))       # Course Name
            parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            for x in range(5):   # numCourseSection
                child = QTreeWidgetItem(parent)
                child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                child.setText(0, "Child {}".format(x))      # Instructor Name
                child.setCheckState(0, Qt.Checked)  # By default all checked
