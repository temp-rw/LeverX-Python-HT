from json import dumps
from typing import Any, List
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, tostring

from data import Student, Room


class ISerializer:
    def _serialize_to_xml(self, obj: List[Any]) -> str:
        raise NotImplementedError

    def _serialize_to_json(self, obj: List[Any]) -> str:
        raise NotImplementedError


class StudentSerializer(ISerializer):
    def __init__(self):
        self.serialized_students = None

    def serialize(self, students: List[Student], serialize_format: str = None) -> str:
        if serialize_format is None:
            raise ValueError("format must be string")

        if serialize_format == 'xml':
            return self._serialize_to_xml(students)
        elif serialize_format == 'json':
            return self._serialize_to_json(students)
        else:
            raise ValueError("format may be only xml or json")

    def _serialize_to_json(self, students: List[Student]) -> str:
        list_of_dicts = []
        for student in students:
            list_of_dicts.append(student.to_dict())

        self.serialized_students = dumps(list_of_dicts, ensure_ascii=False, indent=2)
        return self.serialized_students

    def _serialize_to_xml(self, students: List[Student]) -> str:
        self.serialized_students = tostring(self._build_xml_tree(students), encoding="unicode")
        self.serialized_students = minidom.parseString(self.serialized_students).toprettyxml(indent="  ")
        return self.serialized_students

    @staticmethod
    def _build_xml_tree(students: List[Student]) -> Element:
        students_tree = Element("students")

        for student in students:
            element_student = SubElement(students_tree, "student")
            element_student_id = SubElement(element_student, "id")
            element_student_id.text = str(student.id)

            element_student_name = SubElement(element_student, "name")
            element_student_name.text = str(student.name)

            element_student_room = SubElement(element_student, "room")
            element_student_room.text = str(student.room)
        return students_tree


class RoomSerializer(ISerializer):
    def __init__(self):
        self.serialized_rooms = None

    def serialize(self, rooms: List[Room], serialize_format: str = None) -> str:
        if serialize_format is None:
            raise ValueError("format must be string")

        if serialize_format == 'xml':
            return self._serialize_to_xml(rooms)
        elif serialize_format == 'json':
            return self._serialize_to_json(rooms)
        else:
            raise ValueError("format may be only xml or json")

    def _serialize_to_json(self, rooms: List[Room]) -> str:
        list_of_dicts = []
        for room in rooms:
            list_of_dicts.append(room.to_dict())

        self.serialized_rooms = dumps(list_of_dicts, ensure_ascii=False, indent=2)
        return self.serialized_rooms

    def _serialize_to_xml(self, rooms: List[Room]) -> str:
        self.serialized_rooms = tostring(self._build_xml_tree(rooms), encoding="unicode")
        self.serialized_rooms = minidom.parseString(self.serialized_rooms).toprettyxml(indent="  ")
        return self.serialized_rooms

    @staticmethod
    def _build_xml_tree(rooms: List[Room]) -> Element:
        rooms_tree = Element("rooms")

        for room in rooms:
            element_room = SubElement(rooms_tree, "room")
            element_room_id = SubElement(element_room, "id")
            element_room_id.text = str(room.id)

            element_room_name = SubElement(element_room, "name")
            element_room_name.text = str(room.name)

            element_students = StudentSerializer()._build_xml_tree(room.students)
            element_room.append(element_students)

            element_room_id.text = str(room.id)
            element_room_name.text = str(room.name)

        return rooms_tree


# prettify = minidom.parseString(string).toprettyxml(indent="  ")
