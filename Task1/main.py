from console_reader import ConsoleReader
from data import Student, Room
from file_parser import JSONParser
from output import SaveFile
from serializers import RoomSerializer


def main():
    command_reader = ConsoleReader()
    parameters = command_reader.read_from_command_line()

    output_file_name = "rooms_with_students"
    parser = JSONParser()

    students_path = parser.create_data_path(parameters.get('students'), 'students.json')
    dict_students = parser.extract_text(students_path)
    students = []
    for student in dict_students:
        students.append(Student.student_mapper(student))

    rooms_path = parser.create_data_path(parameters.get('students'), 'rooms.json')
    dict_rooms = parser.extract_text(rooms_path)
    rooms = []
    for room in dict_rooms:
        rooms.append(Room.room_mapper(room))

    rooms.sort(key=lambda rm: rm.id)
    students.sort(key=lambda st: st.room)
    for room in rooms:
        for student in students:
            if student.room == room.id:
                room.add_student(student)

    serialized_rooms = RoomSerializer().serialize(rooms, parameters.get('format'))
    SaveFile(parameters.get('rooms'), output_file_name, parameters.get('format'), 'w').save(serialized_rooms)


if __name__ == '__main__':
    main()
