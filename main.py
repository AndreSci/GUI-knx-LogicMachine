from interface_func import SetupMainWindow

def OpenMainWindow():
    main_win = SetupMainWindow()
    main_win.show()

    main_win.exit()
#test
OpenMainWindow()