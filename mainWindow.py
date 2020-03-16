from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QStackedLayout, QHBoxLayout, QVBoxLayout
from pCourse import PanelCourse
from pInstructor import PanelInstructor
from pPreference import PanelPreference
from pPriority import PanelPriority
from pResult import PanelResult
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 1010, 660)
        self.setWindowTitle("Auto Course Scheduler")
        self.setWindowIcon(QtGui.QIcon('mainIcon.png'))

        ##########
        # Left frame
        self.frame1 = QFrame(self)
        self.frame1.setGeometry(QtCore.QRect(0, 0, 150, 660))

        # Font in left frame
        self.font = QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(10)
        self.frame1.setFont(self.font)

        # Button Course
        self.course = QtWidgets.QPushButton(self.frame1)
        self.course.setGeometry(QtCore.QRect(0, 150, 150, 50))
        self.course.setText("Course")

        # Button Instructor
        self.instructor = QtWidgets.QPushButton(self.frame1)
        self.instructor.setGeometry(QtCore.QRect(0, 200, 150, 50))
        self.instructor.setText("Instructor")

        # Button Preference
        self.preference = QtWidgets.QPushButton(self.frame1)
        self.preference.setGeometry(QtCore.QRect(0, 250, 150, 50))
        self.preference.setText("Preference")

        # Button Priority
        self.priority = QtWidgets.QPushButton(self.frame1)
        self.priority.setGeometry(QtCore.QRect(0, 300, 150, 50))
        self.priority.setText("Priority")

        # Button Result
        self.result = QtWidgets.QPushButton(self.frame1)
        self.result.setGeometry(QtCore.QRect(0, 350, 150, 50))
        self.result.setText("Result")

        # Label for Logo
        self.logo = QtWidgets.QLabel(self.frame1)
        self.logo.setGeometry(QtCore.QRect(0, 0, 150, 150))
        self.logo.setPixmap(QtGui.QPixmap("mainIcon.png"))
        self.logo.setScaledContents(True)
        ##########
        # Right frame
        self.frame2 = QFrame(self)
        self.frame2.setGeometry(QtCore.QRect(150, 0, 860, 660))
        self.frame2.setFrameShape(QFrame.StyledPanel)

        # Assigned stacked layout to the right frame
        self.qsl = QStackedLayout(self.frame2)

        # create panels
        self.p0 = PanelCourse()
        self.p1 = PanelInstructor()
        self.p2 = PanelPreference()
        self.p3 = PanelPriority()
        self.p4 = PanelResult()

        # Add panels to the stacked layout
        self.qsl.addWidget(self.p0)
        self.qsl.addWidget(self.p1)
        self.qsl.addWidget(self.p2)
        self.qsl.addWidget(self.p3)
        self.qsl.addWidget(self.p4)
        ##########


        # Event of Buttons in Left frame
        self.course.clicked.connect(lambda: self.qsl.setCurrentIndex(0))
        self.instructor.clicked.connect(lambda: self.qsl.setCurrentIndex(1))
        self.preference.clicked.connect(lambda: self.qsl.setCurrentIndex(2))
        self.priority.clicked.connect(lambda: self.qsl.setCurrentIndex(3))
        self.result.clicked.connect(lambda: self.qsl.setCurrentIndex(4))

        # Event of Next/Previous Buttons on each panels
        # Panel Course
        self.p0.next.clicked.connect(lambda: self.qsl.setCurrentIndex(self.qsl.currentIndex() + 1))
        # Panel Instructor
        self.p1.next.clicked.connect(lambda: self.qsl.setCurrentIndex(self.qsl.currentIndex() + 1))
        self.p1.previous.clicked.connect(lambda: self.qsl.setCurrentIndex(self.qsl.currentIndex() - 1))
        # Panel Preference
        self.p2.next.clicked.connect(lambda: self.qsl.setCurrentIndex(self.qsl.currentIndex() + 1))
        self.p2.previous.clicked.connect(lambda: self.qsl.setCurrentIndex(self.qsl.currentIndex() - 1))
        # Panel Priority
        self.p3.previous.clicked.connect(lambda: self.qsl.setCurrentIndex(self.qsl.currentIndex() - 1))
        ###########


#############
def execute():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())



execute()
