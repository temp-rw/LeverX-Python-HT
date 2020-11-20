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
