###################################################################
# The file is intended for getting data from the ETS project file #
###################################################################

from xml.etree import ElementTree
import re


def ParsXMLFile():
    tree = ElementTree.parse("xml_files/xml_file.xml")
    root = tree.getroot()

    xml_file = list()

    for it_1 in root:

        for it_2 in it_1:
            xml_file.append(it_2.attrib)

            for it_3 in it_2:
                xml_file.append(it_3.attrib)
    return xml_file


def CyclonFunc(items, Address, xmlReturn, attribName=list(), tag=list()):

    text_name = attribName[1]
    address_id = attribName[0]

    for item in items:
        if item.tag in tag and address_id in item.attrib:
            it_ready = dict()
            it_ready[text_name] = item.attrib.get(text_name)
            it_ready[address_id] = item.attrib.get(address_id)
            xmlReturn.append(it_ready)
        CyclonFunc(item, Address,  xmlReturn, attribName, tag)    # функция вызывает саму себя


def CyclonFuncForButtons(items, address_area, address_line, xml_return, attrib_name=list(), tag=list()):

    # ' Area', 'Line', 'DeviceInstance'

    for item in items:

        if item.tag == tag[0]:
            address_area = "{}".format(item.attrib.get('Address'))
        elif item.tag == tag[1]:
            address_area = "{}".format(item.attrib.get('Address'))
        elif item.tag == tag[2]:
            if len(item.attrib.get('Name')):
                it_ready = dict()
                it_ready['Name'] = item.attrib.get('Name')
                it_ready['Address'] = "{}.{}.{}".format(address_area, address_line, item.attrib.get('Address'))

                xml_return.append(it_ready)

        CyclonFuncForButtons(item, address_area, address_line, xml_return, attrib_name, tag)   # функция вызывает саму себя


def getXMLmaster(fileName, NameList, tagNames, itemFind):

    xml_master_return = list()

    tree = ElementTree.parse(fileName)
    root = tree.getroot()

    xmlns = re.search('{.*}', root.tag)
    xmlns = xmlns.group(0)
    index = ""

    tag_names_in = list()

    for it in tagNames:
        tag_names_in.append(f'{xmlns}{it}')

    if itemFind == 'Buttons':
        address_area = "0"
        address_line = "0"
        CyclonFuncForButtons(root, address_area, address_line, xml_master_return, NameList, tag_names_in)
    else:
        CyclonFunc(root, index, xml_master_return, NameList, tag_names_in)

    return xml_master_return


def parsXMLGroupAddress(file_name="xml_files/xml_file.xml"):

    name_list = ["Address", "Name"]  # Имена что ищем в файле (принимает 2 аргумента) поиск осуществляется \
                                     # по первому аргументу (встречается случай когда адрес есть а имени нет)
    tag_names = ['GroupRange', 'GroupAddress']  # Тэги в которых искать нужные адреса (охват по желанию)

    xml_master_return = getXMLmaster(file_name, name_list, tag_names, "")
    print_xml_info(xml_master_return, name_list)

    return xml_master_return


def parsXMLDatapointSubtype(fileName = "xml_files/knx_master.xml"):

    name_list = ["Id", "Text"]
    tag_names = ['DatapointType', 'DatapointSubtype']

    xml_master_return = getXMLmaster(fileName, name_list, tag_names, "")
    print_xml_info(xml_master_return, name_list)

    return xml_master_return


def parsXMLButtons(fileName = "xml_files/xml_buttons.xml"):

    name_list = ["Address", "Name"]
    tag_names = ['Area', 'Line', 'DeviceInstance']

    xml_master_return = getXMLmaster(fileName, name_list, tag_names, "Buttons")
    print_xml_info(xml_master_return, name_list)

    return xml_master_return


def print_xml_info(xml_master_return, name_list):
    for it in xml_master_return:
        print("{} === {}".format(it[name_list[0]], it[name_list[1]]))


if __name__ == "__main__":

    # parsXMLDatapointSubtype()
    # parsXMLGroupAddress()
    parsXMLButtons()