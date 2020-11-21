from dataclasses import dataclass
from typing import List


@dataclass
class Student:
    id: int
    name: str
    room: int

    @classmethod
    def student_mapper(cls, data: dict):
        return cls(id=data.get('id'), name=data.get('name'), room=data.get('room'))

    def to_dict(self) -> dict:
        student_dict = dict()
        student_dict['id'] = self.id
        student_dict['name'] = self.name
        student_dict['room'] = self.room
        return student_dict


@dataclass
class Room:
    id: int
    name: str
    students: List[Student] = None

    @classmethod
    def room_mapper(cls, data: dict):
        return cls(id=data.get('id'), name=data.get('name'))

    def add_student(self, student: Student):
        if self.students:
            self.students.append(student)
        else:
            self.students = [student]

    def to_dict(self) -> dict:
        room_dict = dict()
        room_dict['id'] = self.id
        room_dict['name'] = self.name
        room_dict['students'] = [student.to_dict() for student in self.students]
        return room_dict
