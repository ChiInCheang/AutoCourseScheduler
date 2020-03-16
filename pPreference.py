from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow


class PanelPreference(QMainWindow):
    def __init__(self):
        super(PanelPreference, self).__init__()
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
        self.setFont(self.fontB)

        # Previous Button
        self.previous = QtWidgets.QPushButton(self)
        self.previous.setGeometry(QtCore.QRect(550, 580, 120, 50))
        self.previous.setText("Previous")
        self.previous.setFont(self.font)

        # Next Button
        self.next = QtWidgets.QPushButton(self)
        self.next.setGeometry(QtCore.QRect(700, 580, 120, 50))
        self.next.setText("Next")
        self.next.setFont(self.font)

        # Label "Length of Class: "
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setGeometry(QtCore.QRect(10, 480, 150, 20))
        self.label2.setText("Length of Class:")

        # Check Box of school days
        self.checkMon = QtWidgets.QCheckBox(self)
        self.checkMon.setGeometry(QtCore.QRect(40, 20, 120, 20))
        self.checkMon.setChecked(True)
        self.checkMon.setText("Monday")

        self.checkTue = QtWidgets.QCheckBox(self)
        self.checkTue.setGeometry(QtCore.QRect(220, 20, 120, 20))
        self.checkTue.setChecked(True)
        self.checkTue.setText("Tuesday")

        self.checkWed = QtWidgets.QCheckBox(self)
        self.checkWed.setGeometry(QtCore.QRect(380, 20, 120, 20))
        self.checkWed.setChecked(True)
        self.checkWed.setText("Wednesday")

        self.checkThu = QtWidgets.QCheckBox(self)
        self.checkThu.setGeometry(QtCore.QRect(550, 20, 120, 20))
        self.checkThu.setChecked(True)
        self.checkThu.setText("Thursday")

        self.checkFri = QtWidgets.QCheckBox(self)
        self.checkFri.setGeometry(QtCore.QRect(740, 20, 120, 20))
        self.checkFri.setChecked(True)
        self.checkFri.setText("Friday")

        # Check Box of length of class
        self.check50 = QtWidgets.QCheckBox(self)
        self.check50.setGeometry(QtCore.QRect(190, 480, 150, 20))
        self.check50.setChecked(True)
        self.check50.setText("50Mins")

        self.check75 = QtWidgets.QCheckBox(self)
        self.check75.setGeometry(QtCore.QRect(360, 480, 150, 20))
        self.check75.setChecked(True)
        self.check75.setText("1Hr 15Mins")

        self.check180 = QtWidgets.QCheckBox(self)
        self.check180.setGeometry(QtCore.QRect(560, 480, 150, 20))
        self.check180.setChecked(True)
        self.check180.setText("2Hr 45Mins")

        # Sliders for Start time of day
        self.MonST = QtWidgets.QSlider(self)
        self.MonST.setGeometry(QtCore.QRect(20, 70, 70, 350))
        self.MonST.setMaximum(48)
        self.MonST.setSingleStep(1)
        self.MonST.setOrientation(QtCore.Qt.Vertical)
        self.MonST.setInvertedAppearance(True)
        self.MonST.setInvertedControls(True)
        self.MonST.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.MonST.setTickInterval(0)

        self.TueST = QtWidgets.QSlider(self)
        self.TueST.setGeometry(QtCore.QRect(190, 70, 70, 350))
        self.TueST.setMaximum(48)
        self.TueST.setSingleStep(1)
        self.TueST.setOrientation(QtCore.Qt.Vertical)
        self.TueST.setInvertedAppearance(True)
        self.TueST.setInvertedControls(True)

        self.WedST = QtWidgets.QSlider(self)
        self.WedST.setGeometry(QtCore.QRect(360, 70, 70, 350))
        self.WedST.setMaximum(48)
        self.WedST.setSingleStep(1)
        self.WedST.setOrientation(QtCore.Qt.Vertical)
        self.WedST.setInvertedAppearance(True)
        self.WedST.setInvertedControls(True)

        self.ThuST = QtWidgets.QSlider(self)
        self.ThuST.setGeometry(QtCore.QRect(530, 70, 70, 350))
        self.ThuST.setMaximum(48)
        self.ThuST.setSingleStep(1)
        self.ThuST.setOrientation(QtCore.Qt.Vertical)
        self.ThuST.setInvertedAppearance(True)
        self.ThuST.setInvertedControls(True)

        self.FriST = QtWidgets.QSlider(self)
        self.FriST.setGeometry(QtCore.QRect(700, 70, 70, 350))
        self.FriST.setMaximum(48)
        self.FriST.setSingleStep(1)
        self.FriST.setOrientation(QtCore.Qt.Vertical)
        self.FriST.setInvertedAppearance(True)
        self.FriST.setInvertedControls(True)

        # Sliders for End time of day
        self.MonEd = QtWidgets.QSlider(self)
        self.MonEd.setGeometry(QtCore.QRect(90, 70, 70, 350))
        self.MonEd.setMaximum(48)
        self.MonEd.setOrientation(QtCore.Qt.Vertical)

        self.TueEd = QtWidgets.QSlider(self)
        self.TueEd.setGeometry(QtCore.QRect(260, 70, 70, 350))
        self.TueEd.setMaximum(48)
        self.TueEd.setOrientation(QtCore.Qt.Vertical)

        self.WedEd = QtWidgets.QSlider(self)
        self.WedEd.setGeometry(QtCore.QRect(430, 70, 70, 350))
        self.WedEd.setMaximum(48)
        self.WedEd.setOrientation(QtCore.Qt.Vertical)

        self.ThuEd = QtWidgets.QSlider(self)
        self.ThuEd.setGeometry(QtCore.QRect(600, 70, 70, 350))
        self.ThuEd.setMaximum(48)
        self.ThuEd.setOrientation(QtCore.Qt.Vertical)

        self.FriEd = QtWidgets.QSlider(self)
        self.FriEd.setGeometry(QtCore.QRect(770, 70, 70, 350))
        self.FriEd.setMaximum(48)
        self.FriEd.setOrientation(QtCore.Qt.Vertical)

        # Horizontal lines (1 - 3)
        self.line1 = QtWidgets.QFrame(self)
        self.line1.setGeometry(QtCore.QRect(0, 40, 850, 20))
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line2 = QtWidgets.QFrame(self)
        self.line2.setGeometry(QtCore.QRect(0, 430, 850, 20))
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line3 = QtWidgets.QFrame(self)
        self.line3.setGeometry(QtCore.QRect(0, 520, 850, 20))
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)

        # Vertical lines (4 - 7)
        self.line4 = QtWidgets.QFrame(self)
        self.line4.setGeometry(QtCore.QRect(170, 0, 20, 440))
        self.line4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line4.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line5 = QtWidgets.QFrame(self)
        self.line5.setGeometry(QtCore.QRect(340, 0, 20, 440))
        self.line5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line5.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line6 = QtWidgets.QFrame(self)
        self.line6.setGeometry(QtCore.QRect(510, 0, 20, 440))
        self.line6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line6.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line7 = QtWidgets.QFrame(self)
        self.line7.setGeometry(QtCore.QRect(680, 0, 20, 440))
        self.line7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line7.setFrameShadow(QtWidgets.QFrame.Sunken)
