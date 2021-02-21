from xml.etree import ElementTree
import sys
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

def CyclonFuncForButtons(items, AddressArea, AddressLine, xmlReturn, attribName = list(), tag = list()):
    "'Area', 'Line', 'DeviceInstance'"
    for item in items:
        if item.tag == tag[0]:
            AddressArea = "{}".format(item.attrib.get('Address'))
        elif item.tag == tag[1]:
            AddressLine = "{}".format(item.attrib.get('Address'))
        elif item.tag == tag[2]:
            if len(item.attrib.get('Name')):
                it_ready = dict()
                it_ready['Name'] = item.attrib.get('Name')
                it_ready['Address'] = "{}.{}.{}".format(AddressArea, AddressLine, item.attrib.get('Address'))

                xmlReturn.append(it_ready)

        CyclonFuncForButtons(item, AddressArea, AddressLine, xmlReturn, attribName, tag)    #функция вызывает саму себя



def getXMLmaster(fileName, NameList, tagNames, itemFind):
    xml_master_return = list()

    tree = ElementTree.parse(fileName)
    root = tree.getroot()

    xmlns = re.search('{.*}', root.tag)
    xmlns = xmlns.group(0)
    index = ""

    tagNamesIn = list()
    for it in tagNames:
        tagNamesIn.append(f'{xmlns}{it}')

    if itemFind == 'Buttons':
        AddressArea = "0"
        AddressLine = "0"
        CyclonFuncForButtons(root, AddressArea, AddressLine, xml_master_return, NameList, tagNamesIn)
    else:
        CyclonFunc(root, index, xml_master_return, NameList, tagNamesIn)

    #for it in xml_master_return:
      #  print("{} === {}".format(it[NameList[0]], it[NameList[1]]))


    return xml_master_return


def parsXMLGroupAddress(fileName = "xml_files/xml_file.xml" ):
    NameList = ["Address", "Name"]  #Имена что ищем в файле (принимает 2 аргумента) поиск осуществляется по первому аргументу (встречается случай когда адрес есть а имени нет)
    tagNames = ['GroupRange', 'GroupAddress'] #Тэги в которых искать нужные адреса (охват по желанию)
    return getXMLmaster(fileName, NameList, tagNames, "")

def parsXMLDatapointSubtype(fileName = "xml_files/knx_master.xml"):
    NameList = ["Id", "Text"]
    tagNames = ['DatapointType', 'DatapointSubtype']
    return getXMLmaster(fileName, NameList, tagNames, "")

def parsXMLButtons(fileName = "xml_files/xml_buttons.xml"):
    name_list = ["Address", "Name"]
    tag_names = ['Area', 'Line', 'DeviceInstance']
    return getXMLmaster(fileName, name_list, tag_names, "Buttons")

#parsXMLDatapointSubtype()
#parsXMLGroupAddress()
#parsXMLButtons()