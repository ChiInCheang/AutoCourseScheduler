from database.DB import *


if __name__ == '__main__':
    csFile = 'cs.csv'
    langFile = 'lang.csv'
    rootsFile = 'roots.csv'

    testdb = DB()
    flag = testdb.createDatabase()  # return 1 if database is newly created, 0 if database already created
    testdb.importData(csFile, flag)
    testdb.importData(langFile, flag)
    testdb.importData(rootsFile, flag)

    l1 = testdb.getSubject()
    l2 = testdb.getLevel("CMPT")
    l3 = testdb.getCourse("CMPT", "100")
    l4 = testdb.getTitle("CMPT", "101")
    l5 = testdb.getInst("CMPT", "101")

    print(l1)
    # print(l1[1][0])
    # print(l1[1])
    print(l2)
    # print(l2[1][0])
    # print(l2[1])
    print(l3)
    # print(l3[1][0])
    # print(l3[1])
    print(l4)
    print(l5)
    testdb.close()