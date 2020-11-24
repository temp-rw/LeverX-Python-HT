from console_reader import ConsoleReader
from data import Student, Room
from file_parser import JSONParser
from output import SaveToFile
from serializers import RoomSerializer


def main():
    # command_reader = ConsoleReader()
    # parameters = command_reader.read_from_command_line()
    parameters = {
        'students': r"D:\Python\LeverX HT\LeverX-Python-HT\Task1",
        'rooms': r"D:\Python\LeverX HT\LeverX-Python-HT\Task1",
        'format': "json"
    }

    output_file_name = "rooms_with_students"
    parser = JSONParser()

    students_path = parser.create_data_path(parameters.get('students'), 'students.json')
    dict_students = parser.extract_text(students_path)
    students = {}
    for student in dict_students:
        students.setdefault(student.get('room'), [])
        students[student.get("room")].append(Student.student_mapper(student))

    rooms_path = parser.create_data_path(parameters.get('students'), 'rooms.json')
    dict_rooms = parser.extract_text(rooms_path)
    rooms = []
    for room in dict_rooms:
        rooms.append(Room.room_mapper(room))

    for room in rooms:
        room.add_students(students[room.id])

    serialized_rooms = RoomSerializer().serialize(rooms, parameters.get('format'))
    SaveToFile(parameters.get('rooms'), output_file_name, parameters.get('format'), 'w').save(serialized_rooms)


if __name__ == '__main__':
    main()
