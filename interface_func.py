from user_id import User
from interface_gui import *
from xml.etree import ElementTree

from xml_pars import parsXMLGroupAddress
from xml_pars import parsXMLDatapointSubtype
from xml_pars import parsXMLButtons
from create_new_buttons import tableNewButtonXML

from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2 import QtCore, QtGui, QtWidgets
import sys


class SetupMainWindow:
    def __init__(self):
        self.appWin = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.uiMwin = Ui_MainWindow()
        self.uiMwin.setupUi(self.MainWindow)
        self.MenuPositionClick = "Close"
        self.baseDict00 = {}
        self.ButtonsDate = dict()   # База выключателей полученых из проекта

        self.XMLGroupAddress = list()
        self.XMLDatapointSubtype = dict()

        # Обьявляем постройки\этажи\комнаты ------------------------------------
        self.Home_info = {'Home1', 'Home2', 'Home3'}
        self.Floor_info = dict()
        self.Floor_info = {'Home1': {'Floore1', 'Floor2'}, 'Home2': {'Floore1', 'Floor2', 'Floor3'}, 'Home3': {'Floore1'}}
        # ----------------------------------------------------------------------

        # Зона новых кнопок в таблице (XML) ------------------------------------
        self.listNewButtonTableNumber = list()    # База новых кнопок из таблицы Numbers
        self.listNewButtonTableAddress = list()  # База новых кнопок из таблицы раздел Address
        self.feedbackLogButton = dict()  # запись адресов новых кнопок
        # ----------------------------------------------------------------------

        # Зона новых кнопок и создание доп. кнопок в таблице (Buttons / Setting Page) --
        self.listNewButtonTableButtonsSet = list()   # База новых кнопок из таблицы ButtonsSet
        self.feedbackButtonsSet = dict()  # запись адресов новых кнопок ButtonsSet
        # ------------------------------------------------------------------------------

        # Зона новых кнопок в таблице (меню настройки) -------------------------
        self.listNewButtonHome = list()
        self.listNewButtonFloor = list()
        self.listNewButtonRoom = list()
        # ----------------------------------------------------------------------

        self.uiMwin.stackedWidget.setCurrentWidget(self.uiMwin.Page_Index_Home)
        self.uiMwin.stackedWidget_MenuBar_1.setCurrentWidget(self.uiMwin.page_2)

        self.uiMwin.Btn_HomePage.clicked.connect(self.changePageHome)
        self.uiMwin.Btn_XMLPage.clicked.connect(self.changePageXML)
        self.uiMwin.Btn_LogPage_inf.clicked.connect(self.changePageLogs)
        self.uiMwin.Btn_SettingPage.clicked.connect(self.changePageSetting)
        self.uiMwin.Btn_Menu.clicked.connect(self.MenuOpenClose)

        # Кнопка открытия списка домов -------
        self.uiMwin.Btn_Home.clicked.connect(self.btnHomeClick)
        self.btnHomeStatusHide = False
        self.btnHomeClick()
        # ------------------------------------

        self.uiMwin.Read_XML.clicked.connect(self.setXMLTable)
        self.uiMwin.Btn_CloseWindow.clicked.connect(self.appWin.closeAllWindows)
        self.uiMwin.pushButton_3.clicked.connect(self.CreateButtonsInfo)

    def MenuOpenClose(self):

        if self.MenuPositionClick == "Open":
            self.uiMwin.stackedWidget_MenuBar_1.setCurrentWidget(self.uiMwin.page_2)
            self.MenuPositionClick = "Close"
        elif self.MenuPositionClick == "Close":
            self.uiMwin.stackedWidget_MenuBar_1.setCurrentWidget(self.uiMwin.page)
            self.MenuPositionClick = "Open"

    def show(self):
        self.MainWindow.show()

    def exit(self):
        sys.exit(self.appWin.exec_())

    def changeSizeF3(uiMwin):
        uiMwin.changeSizeFrame3()

    def changePageHome(self):
        self.uiMwin.stackedWidget.setCurrentWidget(self.uiMwin.Page_Index_Home)

    def changePageSetting(self):
        self.uiMwin.stackedWidget.setCurrentWidget(self.uiMwin.Page_settings)

    def changePageXML(self):
        self.uiMwin.stackedWidget.setCurrentWidget(self.uiMwin.Page_XML)

    def changePageLogs(self):
        self.uiMwin.stackedWidget.setCurrentWidget(self.uiMwin.Page_Log)

    def tableButtonClick(self, number_row_item):
        self.uiMwin.stackedWidget.setCurrentWidget(self.uiMwin.Page_settings)

    def setXMLTable(self):

        # Пересоздаем таблицу --------------------------------------------------------------------------------------

        self.listNewButtonTableNumber.clear()  # очищаем базу созднных кнопок
        self.listNewButtonTableAddress.clear()  # очищаем базу созднных кнопок
        self.feedbackLogButton.clear()

        if not self.XMLGroupAddress:
            self.takeXMLfile()
            self.takeXMLDatapointSubtype()

        "' Очищаем заглавия '"

        self.uiMwin.table_forLog.clear()
        self.uiMwin.table_forLog.setRowCount(0)

        labels = ['№', 'Name', 'Address', 'GateWay', 'Long/Short', 'Data Type', 'Day/Night', 'Toggle', 'Comments']

        self.uiMwin.table_forLog.setColumnCount(len(labels))  # устанавливаем длинну таблицы
        self.uiMwin.table_forLog.setHorizontalHeaderLabels(labels)  # заполняем название столбцов

        # ----------------------------------------------------------------------------------------------------------

        index_row = 0
        number_row_item = 1
        its_group_name = False

        for items in self.XMLGroupAddress:
            row = self.uiMwin.table_forLog.rowCount()  # получаем кол-во строк
            self.uiMwin.table_forLog.setRowCount(row + 1)  # создаем новою строку
            if 'RangeStart' in items:
                its_group_name = True
                for it in range(len(labels)):
                    color_item = QTableWidgetItem()
                    color_item.setBackgroundColor(QColor(90, 90, 90))
                    self.uiMwin.table_forLog.setItem(index_row, it, color_item)
            else:

                # Создаем новую кнопку в таблице для перехода в меню настройки

                tableNewButtonXML(self, number_row_item,  self.listNewButtonTableNumber, number_row_item)
                self.uiMwin.table_forLog.setCellWidget(index_row, 0, self.listNewButtonTableNumber[number_row_item - 1])
                tableNewButtonXML(self, number_row_item, self.listNewButtonTableAddress, items['Address'])
                self.uiMwin.table_forLog.setCellWidget(index_row, 2, self.listNewButtonTableAddress[number_row_item - 1])

                # запоминаем адрес кнопки

                self.feedbackLogButton[str(number_row_item)] = items['Address']
                number_row_item += 1

            if 'Name' in items:
                if its_group_name:
                    color_item = QTableWidgetItem()
                    color_item.setBackgroundColor(QColor(90, 90, 90))
                    color_item.setText(items['Name'])
                    self.uiMwin.table_forLog.setItem(index_row, 1, color_item)
                else:
                    self.uiMwin.table_forLog.setItem(index_row, 1, QTableWidgetItem(items['Name']))

            if 'DPTs' in items:
                self.uiMwin.table_forLog.setItem(index_row, 5, QTableWidgetItem(self.XMLDatapointSubtype[items['DPTs']]))

                "self.uiMwin.table_forLog.setItem(index_row, 5, QTableWidgetItem(items['DPTs']))"

            index_row += 1
            its_group_name = False

    def takeXMLfile(self):
        self.XMLGroupAddress = parsXMLGroupAddress()

    def takeXMLDatapointSubtype(self):
        for item in parsXMLDatapointSubtype():
            self.XMLDatapointSubtype[item["Id"]] = item['Text']

    def btnHomeClick(self):
        if self.btnHomeStatusHide:
            self.showMenuFloorRoom()
        else:
            self.hideMenuFloorRoom()

    def showMenuFloorRoom(self):
        self.uiMwin.Menu_Settings.setMaximumSize(QtCore.QSize(296, 16777215))
        self.uiMwin.Menu_Settings.setMinimumSize(QtCore.QSize(296, 16777215))
        self.uiMwin.tableWidgetforHome.show()
        self.uiMwin.tableMenu1.show()
        self.uiMwin.tableMenu2.show()
        self.btnHomeStatusHide = False

    def hideMenuFloorRoom(self):
        self.uiMwin.Menu_Settings.setMaximumSize(QtCore.QSize(92, 16777215))
        self.uiMwin.Menu_Settings.setMinimumSize(QtCore.QSize(92, 16777215))
        self.uiMwin.tableWidgetforHome.hide()
        self.uiMwin.tableMenu1.hide()
        self.uiMwin.tableMenu2.hide()
        self.btnHomeStatusHide = True

    def CreateButtonsInfo(self):
        date_it = parsXMLButtons()

        for it in date_it:
            self.ButtonsDate[it['Address']] = {"Address": it['Address'], "Name": it['Name'],
                                               "Scenes": "No1", "Home": "unknowed", "Floor": "unknowed", "Room": "unknowed",
                                               "Comments": "some words"}  # "Long/Short": 0, "Toggle": 0, "Day/Night": 0 }
            print(self.ButtonsDate[it['Address']])