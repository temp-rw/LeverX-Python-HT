from dataclasses import asdict
from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class Student:
    id: int
    name: str
    birthday: date
    room: int
    sex: str

    @classmethod
    def student_mapper(cls, data: dict):
        return cls(id=data.get('id'), name=data.get('name'), birthday=data.get('birthday'),
                   room=data.get('room'), sex=data.get('name'))

    def to_dict(self) -> dict:
        return asdict(self, dict_factory=dict)


@dataclass
class Room:
    id: int
    name: str
    students: List[Student]

    @classmethod
    def room_mapper(cls, data: dict):
        return cls(id=data.get('id'), name=data.get('name'))

    def add_student(self, student: Student):
        if self.students is None:
            self.students = []

        self.students.append(student)

    def add_students(self, students: List[Student]):
        if self.students is None:
            self.students = []

        self.students.extend(students)

    def to_dict(self) -> dict:
        return asdict(self, dict_factory=dict)
