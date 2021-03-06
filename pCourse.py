from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from database.DB import *
import string

class PanelCourse(QMainWindow):
    """
    Draw "Course" panel
    """
    def __init__(self):
        super(PanelCourse, self).__init__()
        self.widget = QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 850, 650))
        self.setCentralWidget(self.widget)
        self.layout = QVBoxLayout(self.widget)  # Overall vertical layout

        # Font
        self.font = QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(9)
        self.setFont(self.font)

        """
        Widgets
        """
        # Label
        self.label = QLabel("Total number of course going to take: ", self.widget)
        # Combo Box
        self.limit = QComboBox(self.widget)
        self.limit.addItems([str(n + 1) for n in range(10)])
        self.limit.setCurrentIndex(4)
        # Search Bar
        self.searchBar = QLineEdit(self.widget)
        self.searchBar.setClearButtonEnabled(True)
        # Search Button
        self.search = QPushButton("Search", self.widget)
        # Spacer
        self.spacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.spacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.spacer3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.spacer4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # Course List
        self.courseList = QTreeWidget(self.widget)
        self.initCourseList()
        # Selected Course List
        self.selectedList = QTreeWidget(self.widget)
        self.initSelectedList()
        # Add Button
        self.add = QPushButton("Add", self.widget)
        # Remove Button
        self.remove = QPushButton("Remove", self.widget)
        # Next Button
        self.next = QPushButton("Next", self.widget)

        """
        Layout
        """
        # Horizontal layout 1
        self.hl1 = QHBoxLayout(self.widget)
        self.hl1.addWidget(self.searchBar)
        self.hl1.addWidget(self.search)
        self.hl1.addItem(self.spacer1)
        self.hl1.addWidget(self.label)
        self.hl1.addWidget(self.limit)
        # Horizontal layout 2
        self.hl2 = QHBoxLayout(self.widget)
        self.hl2.addWidget(self.courseList)
        self.hl2.addWidget(self.selectedList)
        # Horizontal layout 3
        self.hl3 = QHBoxLayout(self.widget)
        self.hl3.addItem(self.spacer2)
        self.hl3.addWidget(self.add)
        self.hl3.addWidget(self.remove)
        self.hl3.addItem(self.spacer3)
        # Horizontal layout 4
        self.hl4 = QHBoxLayout(self.widget)
        self.hl4.addItem(self.spacer4)
        self.hl4.addWidget(self.next)
        # Overall vertical layout
        self.layout.addLayout(self.hl1)
        self.layout.addLayout(self.hl2)
        self.layout.addLayout(self.hl3)
        self.layout.addLayout(self.hl4)

        """
        Events
        """
        self.add.clicked.connect(lambda: self.__addButtonEvent())
        self.remove.clicked.connect(lambda: self.__removeButtonEvent())


    """
    Member functions
    """
    def initCourseList(self):
        self.courseList.setHeaderLabel("Course Available")
        # show the horizontal scrollbar when needed
        self.courseList.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.courseList.header().setStretchLastSection(False)

        # connect to database
        db = DB()
        db.useDatabase()
        # fetch and display data
        subjects = db.getSubject()     # list of subject
        for x in subjects:  # x: subject name
            subjItem = QTreeWidgetItem(self.courseList)
            subjItem.setText(0, x)
            levels = db.getLevel(x)
            for y in levels:    # y: level in subject x
                lvItem = QTreeWidgetItem(subjItem)
                lvItem.setFlags(lvItem.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
                lvItem.setText(0, "{} Level".format(y))
                lvItem.setCheckState(0, Qt.Unchecked)
                courses = db.getCourse(x, y)
                for z in courses:   # z: course name in "subject x - level y"
                    crseItem = QTreeWidgetItem(lvItem)
                    title = db.getTitle(x, z)
                    crseItem.setFlags(crseItem.flags() | Qt.ItemIsUserCheckable)
                    crseItem.setText(0, "{} - {}".format(z, title[0]))
                    crseItem.setCheckState(0, Qt.Unchecked)

        self.courseList.sortItems(0, Qt.AscendingOrder)
        db.close()

    def initSelectedList(self):
        self.selectedList.setColumnCount(3)
        self.selectedList.setHeaderLabels(["Intended Course", "Mandatory", "# of Course"])
        self.selectedList.setColumnWidth(0, 210)
        self.selectedList.setColumnWidth(1, 90)
        self.selectedList.setColumnWidth(2, 80)

    def __addButtonEvent(self):
        """
        access the root of courseList
        loop through each subject:
            loop each level in the subject:
                if the level is not Unchecked (that means, Checked or Partially Checked):
                    take the checked courses in the level from the courseList,
                    add them to the selectedList
        sort the item in selectedList
        """
        root = self.courseList.invisibleRootItem()
        subjCount = root.childCount()
        for i in range(subjCount):     # loop through each subject
            subjItem = root.child(i)
            lvCount = subjItem.childCount()
            for j in range(lvCount - 1, -1, -1):    # loop through each level in current subject
                lvItem = subjItem.child(j)
                lvState = lvItem.checkState(0)
                if lvState != Qt.Unchecked:
                    self.__addToSelected(subjItem, lvItem)
        self.selectedList.sortItems(0, Qt.AscendingOrder)

    def __addToSelected(self, subjItem, lvItem):
        # find corresponding subject-level
        searchTerm = "{} {}".format(subjItem.text(0), lvItem.text(0))
        find = self.selectedList.findItems(searchTerm, Qt.MatchExactly)
        # check if the level exists in selected list
        if len(find):
            tarLv = find[0]
        else:
            # create level item in selectedList
            # this is the target level item will be added course
            tarLv = QTreeWidgetItem()
            tarLv.setText(0, searchTerm)
            # combo box for each level item
            comboBox = QComboBox()
            num = [str(n+1) for n in range(9)]
            num.append("Ignore")
            comboBox.addItems(num)
            comboBox.setCurrentIndex(len(num) - 1)
            self.selectedList.addTopLevelItem(tarLv)
            self.selectedList.setItemWidget(tarLv, 2, comboBox)
            self.selectedList.expandItem(tarLv)

        # move checked crse
        crseCount = lvItem.childCount()  # loop through each course in current level
        for k in range(crseCount - 1, -1, -1):
            crseItem = lvItem.child(k)
            crseState = crseItem.checkState(0)
            if crseState == Qt.Checked:
                checkedItem = lvItem.takeChild(k)
                checkedItem.setText(0, "{}".format(crseItem.text(0)))
                checkedItem.setCheckState(0, Qt.Unchecked)
                tarLv.addChild(checkedItem)
                checkBox = QCheckBox()      # check box for mandatory in the second column
                checkBox.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                self.selectedList.setItemWidget(checkedItem, 1, checkBox)

        # remove empty level in courseList
        if lvItem.childCount() == 0:
            subjItem.removeChild(lvItem)

    def __removeButtonEvent(self):
        """
        access the root of selectedList
        loop through each subject-level:
            loop each course in the subject-level:
                if the level is checked:
                    remove the course in the level and add it back to courseList
        sort the item in CourseList
        """
        root = self.selectedList.invisibleRootItem()
        slCount = root.childCount()
        for i in range(slCount - 1, -1, -1):  # loop through each subject-level
            slItem = root.child(i)
            crseCount = slItem.childCount()
            for j in range(crseCount - 1, -1, -1):  # loop through each course in current subject-level
                crseItem = slItem.child(j)
                crseState = crseItem.checkState(0)
                if crseState == Qt.Checked:  # if crse is checked
                    self.__removeFromSelcted(i, j, slItem)
        self.courseList.sortItems(0, Qt.AscendingOrder)

    def __removeFromSelcted(self, i, j, slItem):
        # find corresponding subject
        searchTerm = slItem.text(0).split()
        subjName = searchTerm[0]
        lvName = " ".join(searchTerm[1:len(searchTerm)])
        tarSubj = self.courseList.findItems(subjName, Qt.MatchExactly)[0]
        isFind = False
        # check if the level exists in corresponding subject (in courseList)
        for k in range(tarSubj.childCount()):
            lvItem = tarSubj.child(k)
            if lvItem.text(0) == lvName:
                # access the target level item
                tarLv = lvItem
                isFind = True
                break
        # if not
        if isFind is False:     # create level in courseList
            tarLv = QTreeWidgetItem()
            tarLv.setText(0, lvName)
            tarLv.setFlags(tarLv.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            tarLv.setCheckState(0, Qt.Unchecked)
            tarSubj.addChild(tarLv)

        # move checked crse to courseList
        crseItem = slItem.takeChild(j)
        crseItem.setCheckState(0, Qt.Unchecked)
        tarLv.addChild(crseItem)

        # remove empty subject-item
        if slItem.childCount() == 0:
            self.selectedList.removeItemWidget(slItem, 2)
            self.selectedList.removeItemWidget(slItem, 0)
            self.selectedList.takeTopLevelItem(i)



