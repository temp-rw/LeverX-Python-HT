from dataclasses import asdict
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Student:
    id: int
    name: str
    birthday: datetime
    room_id: int
    sex: str

    @classmethod
    def student_mapper(cls, data: dict):
        return cls(id=data.get('id'), name=data.get('name'), birthday=data.get('birthday'),
                   room_id=data.get('room'), sex=data.get('sex'))

    def to_dict(self) -> dict:
        return asdict(self, dict_factory=dict)


@dataclass
class Room:
    id: int
    name: str

    @classmethod
    def room_mapper(cls, data: dict):
        return cls(id=data.get('id'), name=data.get('name'))

    def to_dict(self) -> dict:
        return asdict(self, dict_factory=dict)
