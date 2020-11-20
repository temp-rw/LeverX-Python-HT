from console_reader import ConsoleReader
from file_parser import JSONParser
from data import Student, Room
import os


def main():
    # command_reader = ConsoleReader()
    # args = command_reader.read_from_command_line()
    args = {
        'students': r"D:\Python\LeverX HT\LeverX-Python-HT\Task1",
        'rooms': r"D:\Python\LeverX HT\LeverX-Python-HT\Task1",
        'format': "json"
    }
    parser = JSONParser()

    students_path = parser.create_data_path(args.get('students'), 'students.json')
    dict_students = parser.extract_text(students_path)
    students = []
    for student in dict_students:
        students.append(Student.student_mapper(student))

    rooms_path = parser.create_data_path(args.get('rooms'), 'rooms.json')
    dict_rooms = parser.extract_text(rooms_path)
    rooms = []
    for room in dict_rooms:
        rooms.append(Room.room_mapper(room))

    students.sort(key=lambda st: st.room)
    for room in rooms:
        for student in students:
            if student.room == room.id:
                room.add_student(student)


if __name__ == '__main__':
    main()
