from json import dumps
from typing import Any, Dict, List, Union
from xml.dom.minidom import parseString

from dicttoxml import dicttoxml


class ISerializer:
    def serialize(self, data: Union[Dict, List[Dict]]) -> str:
        raise NotImplementedError


class JSONSerializer(ISerializer):
    def __init__(self):
        self.serialized = None

    def serialize(self, data: Union[Dict, List]) -> str:
        list_of_dicts = []
        if isinstance(data, List):
            for student in data:
                list_of_dicts.append(student)
        else:
            list_of_dicts.append(data)

        self.serialized = dumps(list_of_dicts, ensure_ascii=False, indent=2)
        return self.serialized


class XMLSerializer(ISerializer):
    def __init__(self, root_element_name: str = "root"):
        self.serialized = None
        self.root_element_name = root_element_name

    def serialize(self, data: Union[Dict, List[Dict]]) -> str:
        list_of_dicts = []
        if isinstance(data, List):
            for element in data:
                list_of_dicts.append(element)
        else:
            list_of_dicts.append(data)

        xml_string = dicttoxml(list_of_dicts, custom_root=self.root_element_name)
        self.serialized = parseString(xml_string).toprettyxml(indent="  ")
        return self.serialized
