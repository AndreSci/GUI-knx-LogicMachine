from interface_func import SetupMainWindow


def open_main_window():

    main_win = SetupMainWindow()
    main_win.show()

    main_win.exit()


if __name__ == "__main__":
    open_main_window()

