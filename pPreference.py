from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, \
    QSpacerItem, QSizePolicy, QLabel, QComboBox, QCheckBox

class PanelPreference(QMainWindow):
    def __init__(self):
        super(PanelPreference, self).__init__()
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 850, 650))
        self.setCentralWidget(self.widget)
        self.layout = QVBoxLayout(self.widget)  # Overall vertical layout
        self.layout.setSpacing(15)

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
        self.setFont(self.fontB)

        # Separation lines
        self.hLine1 = self.line('h')
        self.hLine2 = self.line('h')
        # Labels
        lbSizePolicy = QtWidgets.QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.label1 = self.label("School Day")
        self.label2 = self.label("Start Time")
        self.label3 = self.label("End Time")
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setSizePolicy(lbSizePolicy)
        # self.label1.setMaximumHeight(20)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setSizePolicy(lbSizePolicy)
        # self.label2.setMaximumHeight(20)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setSizePolicy(lbSizePolicy)
        # self.label3.setMaximumHeight(20)
        self.label4 = self.label("Length of Class:")
        self.label4.setSizePolicy(lbSizePolicy)
        # Check Box of school days
        self.check1 = self.checkBox("   Monday", True)
        self.check2 = self.checkBox("   Tuesday", True)
        self.check3 = self.checkBox("   Wednesday", True)
        self.check4 = self.checkBox("   Thursday", True)
        self.check5 = self.checkBox("   Friday", True)
        # Combo Box for Start Time
        self.st1 = self.comboBox()
        self.st2 = self.comboBox()
        self.st3 = self.comboBox()
        self.st4 = self.comboBox()
        self.st5 = self.comboBox()
        # Combo Box for End Time
        self.et1 = self.comboBox()
        self.et2 = self.comboBox()
        self.et3 = self.comboBox()
        self.et4 = self.comboBox()
        self.et5 = self.comboBox()
        # Check Box of length of class
        self.check50 = self.checkBox("50Mins", True)
        self.check75 = self.checkBox("1Hr 15Mins", True)
        self.check180 = self.checkBox("2Hr 45Mins", True)
        # Spacer
        self.spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # Previous Button
        self.previous = QtWidgets.QPushButton(self.widget)
        self.previous.setText("Previous")
        self.previous.setFont(self.font)
        # Next Button
        self.next = QtWidgets.QPushButton(self.widget)
        self.next.setText("Next")
        self.next.setFont(self.font)

        # Adding widget to  Layout
        # Grid Layout
        self.gl = QGridLayout(self.widget)
        self.gl.addWidget(self.label1, 0, 0, 1, 1)
        self.gl.addWidget(self.check1, 1, 0, 1, 1)
        self.gl.addWidget(self.check2, 2, 0, 1, 1)
        self.gl.addWidget(self.check3, 3, 0, 1, 1)
        self.gl.addWidget(self.check4, 4, 0, 1, 1)
        self.gl.addWidget(self.check5, 5, 0, 1, 1)
        self.gl.addWidget(self.label2, 0, 1, 1, 1)
        self.gl.addWidget(self.st1, 1, 1, 1, 1)
        self.gl.addWidget(self.st2, 2, 1, 1, 1)
        self.gl.addWidget(self.st3, 3, 1, 1, 1)
        self.gl.addWidget(self.st4, 4, 1, 1, 1)
        self.gl.addWidget(self.st5, 5, 1, 1, 1)
        self.gl.addWidget(self.label3, 0, 2, 1, 1)
        self.gl.addWidget(self.et1, 1, 2, 1, 1)
        self.gl.addWidget(self.et2, 2, 2, 1, 1)
        self.gl.addWidget(self.et3, 3, 2, 1, 1)
        self.gl.addWidget(self.et4, 4, 2, 1, 1)
        self.gl.addWidget(self.et5, 5, 2, 1, 1)
        # Horizontal layout 2
        self.hl1 = QHBoxLayout(self.widget)
        self.hl1.addWidget(self.label4)
        self.hl1.addWidget(self.check50)
        self.hl1.addWidget(self.check75)
        self.hl1.addWidget(self.check180)
        # Horizontal layout 3
        self.hl2 = QHBoxLayout(self.widget)
        self.hl2.addItem(self.spacer)
        self.hl2.addWidget(self.previous)
        self.hl2.addWidget(self.next)
        # Overall vertical layout
        # self.layout.addLayout(self.hl1)
        self.layout.addLayout(self.gl)
        self.layout.addWidget(self.hLine1)
        self.layout.addLayout(self.hl1)
        self.layout.addWidget(self.hLine2)
        self.layout.addLayout(self.hl2)

    # return a line with d as orientation
    def line(self, d):
        line = QtWidgets.QFrame(self.widget)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        if d == 'h':
            line.setFrameShape(QtWidgets.QFrame.HLine)
        elif d == 'v':
            line.setFrameShape(QtWidgets.QFrame.VLine)
        return line

    # return a checkBox
    def checkBox(self, text, default):
        checkBox = QCheckBox(self.widget)
        checkBox.setText(text)
        checkBox.setChecked(default)
        return checkBox

    def comboBox(self):
        comboBox = QComboBox(self.widget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        comboBox.setSizePolicy(sizePolicy)
        comboBox.setMaximumHeight(50)
        return comboBox

    def label(self, text):
        label = QLabel(self.widget)
        label.setText(text)
        return label