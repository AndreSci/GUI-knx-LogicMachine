from login_gui import Login_Dialog
from user_id import User
from interface_func import SetupMainWindow
from interface_gui import *

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

#в будущем создать функцию пользователей
def takeLoginPassowrd(login, password):
    pass

def OpenMainWindow():
    main_win = SetupMainWindow()
    main_win.show()

    main_win.exit()

newUser = User()

#Hook logic
def EnterLogPass(app, ui, Dialog):
    wordLogin = ui.lineEdit_Login.text()
    newUser.setProfileName(ui.lineEdit_Login.text())
    wordPassword = ui.lineEdit_Password.text()
    if len(wordLogin) == 0:
        ui.dialog_window.setText("Enter login")
    elif len(wordPassword) == 0:
        ui.dialog_window.setText("Enter password")
    elif wordLogin == newUser.getLogName() and wordPassword == newUser.getPassword():
        Dialog.hide()
        OpenMainWindow()
        print("Enter Successful!")
    else:
        ui.dialog_window.setText("Wrong login or password!")
        ui.lineEdit_Password.clear()
        print("Error - wrong login or password enter!")