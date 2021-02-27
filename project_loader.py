#######################################################
# Class for the project database responsible for      #
# the settings window                                 #
#######################################################


class SettingBaseMain:
    def __init__(self):

        # База данных проекта в меню настроик ----------------------------------
        """ Размеры проектов слишком малы для переопределение по имени, """
        """ не будет нагрузкой каждый раз выполнять поиск элемента """
        """ 0 = 'Address', 1 = 'Name', 
            2 = 'Class', 3 = 'DataType', 
            4 = 'Toggle', 5 = 'Long/Short',
            6 = 'Home', 7 = 'Floor',
            8 = 'Room', 9 = 'Comments',
            10 = 'GateWay', 11 = 'Day/Night', """

        self.baseAllDate = dict()
        self.home_info = dict()
        self.floor_info = dict()
        # ----------------------------------------------------------------------

    def set_new_date(self, new_date):  # take dict(dict())
        self.baseAllDate.update(new_date)
        self.update_home_info()
        self.update_floor_info()

    def get_date_by_attrib(self, attrib_item):  # take string address "0/0/0"
        return self.baseAllDate[attrib_item]

    def print_base(self):
        for item in self.baseAllDate:
            print(self.baseAllDate[item])

    def update_home_info(self):
        for address_it in self.baseAllDate:
            home_name = self.baseAllDate[address_it]['Home']
            floor = list()

            if home_name in self.home_info:
                floor = self.home_info[home_name]

            if not self.baseAllDate[address_it]['Floor'] in floor:
                floor.append(self.baseAllDate[address_it]['Floor'])

            self.home_info.update({home_name: floor})
            self.home_info[home_name].sort()

    def update_floor_info(self):
        for address_it in self.baseAllDate:
            floor_name = self.baseAllDate[address_it]['Floor']
            room = list()

            if floor_name in self.floor_info:
                room = self.floor_info[floor_name]

            if not self.baseAllDate[address_it]['Room'] in room:
                room.append(self.baseAllDate[address_it]['Room'])

            self.floor_info.update({floor_name: room})
            self.floor_info[floor_name].sort()


    def print_home_info(self):
        print("Printed Home Info: {}".format(self.home_info))
    def print_floor_info(self):
        print("Printed Room Info: {}".format(self.floor_info))

    def get_home_info(self):
        return self.home_info

    def take_project(self):
        return self.baseAllDate


"#test -------------------------------------------------------------"


def test_01():

    main_date = SettingBaseMain()
    item = dict()

    """ 0 = 'Address', 1 = 'Name', 
        2 = 'Class', 3 = 'DataType', 
        4 = 'Toggle', 5 = 'Long/Short',
        6 = 'Home', 7 = 'Floor',
        8 = 'Room', 9 = 'Comments',
        10 = 'GateWay', 11 = 'Day/Night', """

    item.update({'0/1/1': {'Address': '0/1/1', 'Name': 'name_1', 'Class': 'button',
                 'DataType': 'Type', 'Toggle': 'yes', 'Long/Short': 'long',
                 'Home': 'number_1', 'Floor': 1, 'Room': '01',
                 'Comments': 'some words', 'GateWay': '1', 'Day/Night': 'yes'}})

    item.update({'0/1/2': {'Address': '0/1/2', 'Name': 'name_2', 'Class': 'button',
                  'DataType': 'Type', 'Toggle': 'yes', 'Long/Short': 'long',
                  'Home': 'number_1', 'Floor': 1, 'Room': '02',
                  'Comments': 'some words', 'GateWay': '1', 'Day/Night': 'yes'}})

    item.update({'0/2/2': {'Address': '0/2/2', 'Name': 'name_22', 'Class': 'button',
                  'DataType': 'Type', 'Toggle': 'yes', 'Long/Short': 'long',
                  'Home': 'number_1', 'Floor': 1, 'Room': '01',
                  'Comments': 'some words', 'GateWay': '1', 'Day/Night': 'yes'}})

    main_date.set_new_date(item)

    item2 = dict()

    item2.update({'0/1/3': {'Address': '0/1/3', 'Name': 'name_3', 'Class': 'button',
                   'DataType': 'Type', 'Toggle': 'no', 'Long/Short': 'long',
                   'Home': 'number_2', 'Floor': 2, 'Room': '03',
                   'Comments': 'some words', 'GateWay': '1', 'Day/Night': 'yes'}})

    item2.update({'0/1/4': {'Address': '0/1/4', 'Name': 'name_4', 'Class': 'button',
                   'DataType': 'Type', 'Toggle': 'no', 'Long/Short': 'long',
                   'Home': 'number_2', 'Floor': -1, 'Room': '01',
                   'Comments': 'some words', 'GateWay': '1', 'Day/Night': 'yes'}})

    item2.update({'0/1/1': {'Address': '0/1/1', 'Name': 'name_1', 'Class': 'button',
                   'DataType': 'Type', 'Toggle': 'no', 'Long/Short': 'long',
                   'Home': 'nubmer_3', 'Floor': 3, 'Room': 'unknown',
                   'Comments': 'some words', 'GateWay': '1', 'Day/Night': 'yes'}})

    main_date.set_new_date(item2)
    main_date.print_base()
    main_date.print_home_info()
    main_date.print_floor_info()


"#------------------------------------------------------------------"


if __name__ == "__main__":
    test_01()

