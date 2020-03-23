from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from pCourse import PanelCourse
from pInstructor import PanelInstructor
from pPreference import PanelPreference
from pPriority import PanelPriority
from pResult import PanelResult
from UIdata import *


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.guiData = None
        """
        Draw the main window
        """
        self.setGeometry(200, 200, 1000, 650)
        self.setWindowTitle("Auto Course Scheduler")
        self.setWindowIcon(QtGui.QIcon('pic/prgmIcon.png'))
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralLayout = QHBoxLayout(self.centralWidget)   # Central Widget using horizontal layout

        '''
        Left column
        '''
        self.leftWidget = QWidget(self.centralWidget)
        self.leftWidget.setMaximumWidth(150)
        self.leftLayout = QVBoxLayout(self.leftWidget)     # leftWidget using vertical layout
        self.leftLayout.setContentsMargins(0, 0, 0, 0)
        self.leftLayout.setSpacing(0)
        # Font of leftWidget
        self.font = QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(10)
        self.leftWidget.setFont(self.font)
        # Size policy in left column
        self.leftSizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.leftMinHeight = 50
        # Logo
        self.logo = QLabel(self.leftWidget)
        self.logo.setPixmap(QtGui.QPixmap("pic/MClogo.png"))
        self.logo.setScaledContents(True)
        self.logo.setSizePolicy(self.leftSizePolicy)
        self.logo.setMaximumSize(150, 118)
        # Button "Course"
        self.course = QPushButton("Course", self.leftWidget)
        self.course.setSizePolicy(self.leftSizePolicy)
        self.course.setMinimumHeight(self.leftMinHeight)
        # Button "Instructor"
        self.instructor = QPushButton("Instructor", self.leftWidget)
        self.instructor.setSizePolicy(self.leftSizePolicy)
        self.instructor.setMinimumHeight(self.leftMinHeight)
        # Button "Preference"
        self.preference = QPushButton("Preference", self.leftWidget)
        self.preference.setSizePolicy(self.leftSizePolicy)
        self.preference.setMinimumHeight(self.leftMinHeight)
        # Button "Priority"
        self.priority = QPushButton("Priority", self.leftWidget)
        self.priority.setSizePolicy(self.leftSizePolicy)
        self.priority.setMinimumHeight(self.leftMinHeight)
        # Button "Result"
        self.result = QPushButton("Result", self.leftWidget)
        self.result.setSizePolicy(self.leftSizePolicy)
        self.result.setMinimumHeight(self.leftMinHeight)
        # Spacer
        self.vSpacer1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.vSpacer2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # Add widgets to left column
        self.leftLayout.addWidget(self.logo)
        self.leftLayout.addSpacerItem(self.vSpacer1)
        self.leftLayout.addWidget(self.course)
        self.leftLayout.addWidget(self.instructor)
        self.leftLayout.addWidget(self.preference)
        self.leftLayout.addWidget(self.priority)
        self.leftLayout.addWidget(self.result)
        self.leftLayout.addSpacerItem(self.vSpacer2)

        '''
        Right column
        '''
        self.rightWidget = QWidget(self.centralWidget)
        self.rightLayout = QStackedLayout(self.rightWidget)  # Right column using stacked layout

        # Panels
        self.pCourse = PanelCourse()
        self.pInstructor = PanelInstructor()
        self.pPreference = PanelPreference()
        self.pPriority = PanelPriority()
        self.pResult = PanelResult()
        # Add panels to the stacked layout
        self.rightLayout.addWidget(self.pCourse)
        self.rightLayout.addWidget(self.pInstructor)
        self.rightLayout.addWidget(self.pPreference)
        self.rightLayout.addWidget(self.pPriority)
        self.rightLayout.addWidget(self.pResult)

        """
        Layout
        """
        self.centralLayout.addWidget(self.leftWidget)
        self.centralLayout.addWidget(self.rightWidget)

        """
        Events
        """
        # Buttons in left column
        self.course.clicked.connect(lambda: self.showPanel(0))
        self.instructor.clicked.connect(lambda: self.clickInst())
        self.preference.clicked.connect(lambda: self.showPanel(2))
        self.priority.clicked.connect(lambda: self.showPanel(3))
        self.result.clicked.connect(lambda: self.showPanel(4))

        # Next/Previous Buttons
        # Panel Course
        self.pCourse.next.clicked.connect(lambda: self.click_next_pCourse())
        # Panel Instructor
        self.pInstructor.next.clicked.connect(lambda: self.showNextPanel())
        self.pInstructor.previous.clicked.connect(lambda: self.showPreviousPanel())
        # Panel Preference
        self.pPreference.next.clicked.connect(lambda: self.showNextPanel())
        self.pPreference.previous.clicked.connect(lambda: self.showPreviousPanel())
        # Panel Priority
        self.pPriority.previous.clicked.connect(lambda: self.showPreviousPanel())
        self.pPriority.submit.clicked.connect(lambda: self.click_submit())
    """
    Member functions
    """
    def clickInst(self):
        if self.rightLayout.currentIndex() == 0:
            self.pInstructor.filterEvent(self.pCourse)
        self.showPanel(1)

    def click_next_pCourse(self):
        self.pInstructor.filterEvent(self.pCourse)
        self.showNextPanel()

    def showPanel(self, index):
        self.rightLayout.setCurrentIndex(index)

    def showNextPanel(self):
        self.rightLayout.setCurrentIndex(self.rightLayout.currentIndex() + 1)

    def showPreviousPanel(self):
        self.rightLayout.setCurrentIndex(self.rightLayout.currentIndex() - 1)

    def click_submit(self):
        self.guiData = self.submitUIData()
        self.showNextPanel()

    def submitUIData(self):
        guiData = UIdata(self)
        return guiData