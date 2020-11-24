from dataclasses import dataclass
from dataclasses import asdict
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
        return asdict(self, dict_factory=dict)


@dataclass
class Room:
    id: int
    name: str
    students: List[Student] = None

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
