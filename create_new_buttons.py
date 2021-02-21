from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2 import QtCore, QtGui, QtWidgets


def tableNewButtonXML(SetupMainWindow, NumberRowItem, listNewButtonTab, Name):
    listNewButtonTab.append(QtWidgets.QPushButton(str(Name)))
    listNewButtonTab[NumberRowItem - 1].setStyleSheet("QPushButton {\n"
                                                      "    border: 0px solid;\n"
                                                      "    background-color: rgb(109, 109, 109);\n"
                                                      "}\n"
                                                      "QPushButton:hover {\n"
                                                      "    background-color: rgb(136, 136, 136);\n"
                                                      "\n"
                                                      "}\n"
                                                      "QPushButton:pressed {    \n"
                                                      "    background-color: rgb(85, 170, 255);\n"
                                                      "}")
    listNewButtonTab[NumberRowItem - 1].clicked.connect(lambda: SetupMainWindow.tableButtonClick(NumberRowItem))


def tableButtonProjectClick(SetupMainWindow, NumberRowItem):
    pass  # TODO


def tableNewButtonProject(SetupMainWindow, NumberRowItem, listNewButtonTab, Name):
    listNewButtonTab.append(QtWidgets.QPushButton(str(Name)))
    listNewButtonTab[NumberRowItem - 1].setStyleSheet("QPushButton {\n"
                                                      "    border: 0px solid;\n"
                                                      "    background-color: rgb(109, 109, 109);\n"
                                                      "}\n"
                                                      "QPushButton:hover {\n"
                                                      "    background-color: rgb(136, 136, 136);\n"
                                                      "\n"
                                                      "}\n"
                                                      "QPushButton:pressed {    \n"
                                                      "    background-color: rgb(85, 170, 255);\n"
                                                      "}")
    listNewButtonTab[NumberRowItem - 1].clicked.connect(lambda: SetupMainWindow.tableButtonProjectClick(NumberRowItem))