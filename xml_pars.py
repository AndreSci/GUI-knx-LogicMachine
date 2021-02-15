from xml.etree import ElementTree
import sys
import re

def ParsXMLFile():
    tree = ElementTree.parse("xml_files/xml_file.xml")
    root = tree.getroot()

    xmlFile = list()

    for it_1 in root:

        for it_2 in it_1:
            xmlFile.append(it_2.attrib)

            for it_3 in it_2:
                xmlFile.append(it_3.attrib)
    return xmlFile


def CyclonFunc(items, Address, xmlReturn, attribName = list(), tag = list()):

    TextName = attribName[1]
    AddressId = attribName[0]

    for item in items:
        if item.tag in tag and AddressId in item.attrib:
            it_ready = dict()
            it_ready[TextName] = item.attrib.get(TextName)
            it_ready[AddressId] = item.attrib.get(AddressId)
            xmlReturn.append(it_ready)
        CyclonFunc(item, Address,  xmlReturn, attribName, tag)    #функция вызывает саму себя

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
    xmlMasterReturn = list()

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
        CyclonFuncForButtons(root, AddressArea, AddressLine, xmlMasterReturn, NameList, tagNamesIn)
    else:
        CyclonFunc(root, index, xmlMasterReturn, NameList, tagNamesIn)

    #for it in xmlMasterReturn:
      #  print("{} === {}".format(it[NameList[0]], it[NameList[1]]))


    return xmlMasterReturn


def parsXMLGroupAddress(fileName = "xml_files/xml_file.xml" ):
    NameList = ["Address", "Name"]  #Имена что ищем в файле (принимает 2 аргумента) поиск осуществляется по первому аргументу (встречается случай когда адрес есть а имени нет)
    tagNames = ['GroupRange', 'GroupAddress'] #Тэги в которых искать нужные адреса (охват по желанию)
    return getXMLmaster(fileName, NameList, tagNames, "")

def parsXMLDatapointSubtype(fileName = "xml_files/knx_master.xml"):
    NameList = ["Id", "Text"]
    tagNames = ['DatapointType', 'DatapointSubtype']
    return getXMLmaster(fileName, NameList, tagNames, "")

def parsXMLButtons(fileName = "xml_files/xml_buttons.xml"):
    NameList = ["Address", "Name"]
    tagNames = ['Area', 'Line', 'DeviceInstance']
    return getXMLmaster(fileName, NameList, tagNames, "Buttons")

#parsXMLDatapointSubtype()
#parsXMLGroupAddress()
#parsXMLButtons()