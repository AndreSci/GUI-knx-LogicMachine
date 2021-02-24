
class AllBase:
    def __init__(self):

        # База данных проекта в меню настроик ----------------------------------
        " Размеры проектов слишком малы для переопределение по имени, "
        "не будет нагрузкой каждый раз выполнять поиск элемента"
        self.baseAllDate = list()
        self.HomeInfo = list()  # list(dict()) # Home: list(Floor) == Floor: list(name_floor = dict())
        # ----------------------------------------------------------------------

    def set_new_date(self, new_date):  # take list(dict())

        for item in new_date:
            self.baseAllDate.append(item)

    def get_date_attrib(self, attrib_item):  # take string
        return_date = list()
        for it in self.baseAllDate:
            if attrib_item == it['Class']:
                return_date.append(it)
        return return_date

    def save_change_date(self, new_date):  # take list(dict())

        not_change_d = True

        for it in new_date:

            for item in range(len(self.baseAllDate)):
                if self.baseAllDate[item]['Address'] == it['Address']:
                    self.baseAllDate[item] = it
                    not_change_d = False
                    break

            if not_change_d:
                self.baseAllDate.append(it)
            not_change_d = True

    def print_base(self):
        for item in self.baseAllDate:
            print(item)


def take_project():
    pass  # TODO


"#test -------------------------------------------------------------"


def test_01():

    main_date = AllBase()
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
    main_date.set_new_date(item)

    item2 = list()

    item2.append({'Address': '0/1/3', 'Name': 'name_3', 'Class': 'button',
                 'Data Type': 'Type', 'Toggle': 'no', 'Long/Short': 'long',
                  'Home': 'unknown', 'Floor': 'unknown', 'Room': 'unknown',
                  'Comments': 'some words'})

    item2.append({'Address': '0/1/4', 'Name': 'name_4', 'Class': 'button',
                 'Data Type': 'Type', 'Toggle': 'no', 'Long/Short': 'long',
                  'Home': 'unknown', 'Floor': 'unknown', 'Room': 'unknown',
                  'Comments': 'some words'})

    item2.append({'Address': '0/1/1', 'Name': 'name_1', 'Class': 'button',
                 'Data Type': 'Type', 'Toggle': 'no', 'Long/Short': 'long',
                  'Home': 'unknown', 'Floor': 'unknown', 'Room': 'unknown',
                  'Comments': 'some words'})

    main_date.save_change_date(item2)
    main_date.print_base()


"#------------------------------------------------------------------"


if __name__ == "__main__":
    test_01()

