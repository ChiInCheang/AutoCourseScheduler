from PyQt5.QtCore import Qt

# a class getting data from the gui
class UIdata():
    def __init__(self, gui):
        self.__gui = gui

        # list of string: priority
        self.__priority = self.__gui.pPriority.priorityList.nodes

        # list of boolean: value for school days
        # index 0 - 4: Monday - Friday
        self.__schoolDay = [self.__gui.pPreference.check1.checkState(),
                            self.__gui.pPreference.check2.checkState(),
                            self.__gui.pPreference.check3.checkState(),
                            self.__gui.pPreference.check4.checkState(),
                            self.__gui.pPreference.check5.checkState()]
        for i in range(len(self.__schoolDay)):
            self.__schoolDay[i] = self.__biCheckState(self.__schoolDay[i])

        # list of boolean: value for length of class
        # index 0 - 2: 50Min, 1Hr15Min, 2Hr45Min
        self.__classLen = [self.__gui.pPreference.check50.checkState(),
                           self.__gui.pPreference.check75.checkState(),
                           self.__gui.pPreference.check180.checkState()]
        for i in range(len(self.__classLen)):
            self.__classLen[i] = self.__biCheckState(self.__classLen[i])

        # list of string: Start Time
        # possible value: from "08:00" to "21:30", every 30 minutes
        # index 0 - 4: Monday - Friday
        self.__st = [self.__gui.pPreference.st1.currentText(),
                     self.__gui.pPreference.st2.currentText(),
                     self.__gui.pPreference.st3.currentText(),
                     self.__gui.pPreference.st4.currentText(),
                     self.__gui.pPreference.st5.currentText()]

        # list of string: End Time for everyday
        # possible value: from "08:00" to "21:30", every 30 minutes
        # index 0 - 4: Monday - Friday
        self.__et = [self.__gui.pPreference.et1.currentText(),
                     self.__gui.pPreference.et2.currentText(),
                     self.__gui.pPreference.et3.currentText(),
                     self.__gui.pPreference.et4.currentText(),
                     self.__gui.pPreference.et5.currentText()]

        """
        Data from Selected List (sl)
        list of slTuples:
             [(str subj, str lv, str #crse, list crse)]
        eg. ("CMPT", "100", "Ignore", crse)
              possible value of #crse: "1"-"9" and "Ignore"
              crse is the list of selected-CMPT-100lv courses
              
              tuple in crse: (str crseNo, bool isMandatory, list inst)
              eg. ("101", True, inst)
                    inst is a list of tuple (str instName, bool chk)
                    chk is the whether the instructor is checked in the filter 
        """
        self.__sl = self.__selectedData()


    def __selectedData(self):
        data = []

        # Access the selected list in gui
        sl = self.__gui.pCourse.selectedList
        slRoot = sl.invisibleRootItem()

        slCount = slRoot.childCount()
        for i in range(slCount):  # loop through each subject-level
            slItem = slRoot.child(i)

            # get subject name and level
            slText = slItem.text(0).split()
            subj = slText[0]
            lv = slText[1]
            # get combo box value
            cb = sl.itemWidget(slItem, 2).currentText()
            # data of courses in current subj-level
            crseList = self.__courseData(subj, slItem)

            tup = slTuple(subj, lv, cb, crseList)
            data.append(tup)

        return data

    def __courseData(self, subj, slItem):
        data = []
        # Access the selected list in gui
        sl = self.__gui.pCourse.selectedList

        crseCount = slItem.childCount()
        for i in range(crseCount):
            crseItem = slItem.child(i)
            crseItemText = crseItem.text(0)
            # course number
            crseNum = crseItemText.split()
            crseNum = crseNum[0]
            # value of check box for mandatory
            checkBox = sl.itemWidget(crseItem, 1)
            mandatory = checkBox.checkState()
            mandatory = self.__biCheckState(mandatory)
            # instructor data of the course
            instructors = self.__instData(subj, crseItemText)
            tup = clTuple(crseNum, mandatory, instructors)
            data.append(tup)
        return data

    def __instData(self, subj, crseItemText):
        data = []
        filter = self.__gui.pInstructor.filter
        searchTerm = "{} {}".format(subj, crseItemText)
        crse = filter.findItems(searchTerm, Qt.MatchExactly)
        crse = crse[0]
        crseCount = crse.childCount()
        for i in range(crseCount):
            instName = crse.child(i).text(0)
            instCheck = crse.child(i).checkState(0)
            instCheck = self.__biCheckState(instCheck)
            tup = (instName, instCheck)
            data.append(tup)
        return data

    def __biCheckState(self, val):
        if val == 2:
            return 1
        return val

    def getPriority(self):
        return self.__priority

    def getSchoolDay(self):
        return self.__schoolDay

    def getClassLen(self):
        return self.__classLen

    def getStartTime(self):
        return self.__st

    def getEndTime(self):
        return self.__et

    def getCourses(self):
        return self.__sl

# container for data of selected list
class slTuple():
    def __init__(self, subj, lv, cb, crseList):
        self.subj = subj            # Name of the subject
        self.lv = lv                # level
        self.cb = cb                # value of the combo box
        self.crseList = crseList    # list of selected course

# data container of selected course
class clTuple():
    def __init__(self, crseNum, mandatory, instructors):
        self.crseNum = crseNum
        self.mandatory = mandatory
        self.instructors = instructors