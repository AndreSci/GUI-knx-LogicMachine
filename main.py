#######################################################
# Designed to facilitate work with smart home control #
# systems based on KNX and Logic Machine 5            #
# the program uses libraries - PyQt, PySide, KNX, xml #
#######################################################

from interface_func import SetupMainWindow


def open_main_window():

    """ creating the graphic window class """

    main_win = SetupMainWindow()
    main_win.show()

    main_win.exit()


if __name__ == "__main__":
    open_main_window()

