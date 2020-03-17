from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from pCourse import PanelCourse
from pInstructor import PanelInstructor
from pPreference import PanelPreference
from pPriority import PanelPriority
from pResult import PanelResult
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 1000, 650)
        self.setWindowTitle("Auto Course Scheduler")
        self.setWindowIcon(QtGui.QIcon('pic/mainIcon.png'))
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout(self.centralWidget)

        # Left column
        self.widget1 = QWidget(self.centralWidget)
        self.widget1.setMaximumSize(QtCore.QSize(150, 650))
        self.layout1 = QVBoxLayout(self.widget1)     # left column using vertical layout
        self.layout1.setContentsMargins(0, 0, 0, 0)
        self.layout1.setSpacing(0)
        # Font in left column
        self.font = QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(10)
        self.widget1.setFont(self.font)

        # Size policy in left column
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Label for Logo
        self.logo = QLabel(self.widget1)
        self.logo.setPixmap(QtGui.QPixmap("pic/mainIcon.png"))
        self.logo.setScaledContents(True)
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMaximumSize(150, 150)
        self.layout1.addWidget(self.logo)

        # Button Course
        self.course = QtWidgets.QPushButton(self.widget1)
        self.course.setText("Course")
        self.course.setSizePolicy(sizePolicy)
        self.course.setMinimumSize(150, 50)
        self.layout1.addWidget(self.course)

        # Button Instructor
        self.instructor = QtWidgets.QPushButton(self.widget1)
        self.instructor.setText("Instructor")
        self.instructor.setSizePolicy(sizePolicy)
        self.instructor.setMinimumSize(150, 50)
        self.layout1.addWidget(self.instructor)

        # Button Preference
        self.preference = QtWidgets.QPushButton(self.widget1)
        self.preference.setText("Preference")
        self.preference.setSizePolicy(sizePolicy)
        self.preference.setMinimumSize(150, 50)
        self.layout1.addWidget(self.preference)

        # Button Priority
        self.priority = QtWidgets.QPushButton(self.widget1)
        self.priority.setText("Priority")
        self.priority.setSizePolicy(sizePolicy)
        self.priority.setMinimumSize(150, 50)
        self.layout1.addWidget(self.priority)

        # Button Result
        self.result = QtWidgets.QPushButton(self.widget1)
        self.result.setText("Result")
        self.result.setSizePolicy(sizePolicy)
        self.result.setMinimumSize(150, 50)
        self.layout1.addWidget(self.result)

        # Spacer
        vSpacer = QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout1.addSpacerItem(vSpacer)

        # Add left column to main layout
        self.layout.addWidget(self.widget1)

        #########

        # Right Panel
        self.widget2 = QWidget(self.centralWidget)
        self.layout2 = QStackedLayout(self.widget2)      # Panel using stacked layout

        # create panels
        self.p0 = PanelCourse()
        self.p1 = PanelInstructor()
        self.p2 = PanelPreference()
        self.p3 = PanelPriority()
        self.p4 = PanelResult()

        # Add panels to the stacked layout
        self.layout2.addWidget(self.p0)
        self.layout2.addWidget(self.p1)
        self.layout2.addWidget(self.p2)
        self.layout2.addWidget(self.p3)
        self.layout2.addWidget(self.p4)

        # Add right panel to main layout
        self.layout.addWidget(self.widget2)
        ##############################

        # Event of Buttons in Left frame
        self.course.clicked.connect(lambda: self.layout2.setCurrentIndex(0))
        self.instructor.clicked.connect(lambda: self.layout2.setCurrentIndex(1))
        self.preference.clicked.connect(lambda: self.layout2.setCurrentIndex(2))
        self.priority.clicked.connect(lambda: self.layout2.setCurrentIndex(3))
        self.result.clicked.connect(lambda: self.layout2.setCurrentIndex(4))

        # Event of Next/Previous Buttons on each panels
        # Panel Course
        self.p0.next.clicked.connect(lambda: self.layout2.setCurrentIndex(self.layout2.currentIndex() + 1))
        # Panel Instructor
        self.p1.next.clicked.connect(lambda: self.layout2.setCurrentIndex(self.layout2.currentIndex() + 1))
        self.p1.previous.clicked.connect(lambda: self.layout2.setCurrentIndex(self.layout2.currentIndex() - 1))
        # Panel Preference
        self.p2.next.clicked.connect(lambda: self.layout2.setCurrentIndex(self.layout2.currentIndex() + 1))
        self.p2.previous.clicked.connect(lambda: self.layout2.setCurrentIndex(self.layout2.currentIndex() - 1))
        # Panel Priority
        self.p3.previous.clicked.connect(lambda: self.layout2.setCurrentIndex(self.layout2.currentIndex() - 1))
        ###############################


#############
def execute():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())



execute()
