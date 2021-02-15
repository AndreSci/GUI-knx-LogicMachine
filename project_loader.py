import sys


class AllBase:
    def __init__(self):
        # База данных проекта в меню настроик ----------------------------------
        "Размеры проектов слишком малы для переопределение по имени, "
        "не будет нагрузкой каждый раз выполнять поиск элемента"
        self.baseAllDate = list()
        self.HomeInfo = list() #list(dict()) # Home: list(Floor) == Floor: list(name_floor = dict())
        # ----------------------------------------------------------------------

    def setNewDate(self, newDate):  #take list(dict())

        for item in newDate:
            self.baseAllDate.append(item)

    def getDateAttrib(self, attribItem): #take string
        returnDate = list()
        for it in self.baseAllDate:
            if attribItem == it['Class']:
                returnDate.append(it)
        return returnDate

    def saveChangeDate(self, newDate): #take list(dict())
        RANGE_IT = len(self.baseAllDate) #константа размер для прохождения цикла
        changeD = False
        for it in newDate:

            for item in range(RANGE_IT):
                if self.baseAllDate[item]['Address'] == it['Address']:
                    self.baseAllDate[item] = it
                    changeD = True
                    break

                if changeD == False:
                    self.baseAllDate.append(it)

                changeD = False

    def PrintBase(self):
        for item in self.baseAllDate:
            print(item)


def takeProject():
    Project = dict()
    Project = {}
    return Project

#test -------------------------------------------------------------
def Test_01():
    mainD = AllBase()
    item = list()
    "'Data Type', 'Long/Short', 'GateWay', 'Day/Night', 'Toggle', 'Comments'"
    item.append({'Address': '0/1/1', 'Name': 'name_1', 'Class': 'button',
                 'Data Type': 'Type', 'Toggle': 'yes', 'Long/Short': 'long',
                 'Home': 'unknown', 'Floor': 'unknown', 'Room': 'unknown',
                 'Comments': 'some words'})
    item.append({'Address': '0/1/2', 'Name': 'name_2', 'Class': 'button',
                 'Data Type': 'Type', 'Toggle': 'yes', 'Long/Short': 'long',
                 'Home': 'unknown', 'Floor': 'unknown', 'Room': 'unknown',
                 'Comments': 'some words'})
    mainD.setNewDate(item)

    item2 = list()
    item2.append({'Address': '0/1/3', 'Name': 'name_3', 'Class': 'button',
                 'Data Type': 'Type', 'Toggle': 'yes', 'Long/Short': 'long',
                 'Home': 'unknown', 'Floor': 'unknown', 'Room': 'unknown',
                 'Comments': 'some words'})
    item2.append({'Address': '0/1/4', 'Name': 'name_4', 'Class': 'button',
                 'Data Type': 'Type', 'Toggle': 'yes', 'Long/Short': 'long',
                 'Home': 'unknown', 'Floor': 'unknown', 'Room': 'unknown',
                 'Comments': 'some words'})
    item2.append({'Address': '0/1/1', 'Name': 'name_1', 'Class': 'button',
                 'Data Type': 'Type', 'Toggle': 'yes', 'Long/Short': 'long',
                 'Home': 'unknown', 'Floor': 'unknown', 'Room': 'unknown',
                 'Comments': 'some words'})
    mainD.saveChangeDate(item2)

    mainD.PrintBase()
#-----------------------------------------------------------------------

Test_01()