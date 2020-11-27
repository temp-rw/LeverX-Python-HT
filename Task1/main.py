from console_reader import ConsoleReader
from data import Student, Room
from file_parser import JSONParser
from output import FileSaver
from serializers import JSONSerializer, XMLSerializer


def main():
    serializers = {"json": JSONSerializer, "xml": XMLSerializer}
    command_reader = ConsoleReader()
    parameters = command_reader.read_from_command_line()

    output_file_name = "rooms_with_students"
    parser = JSONParser()

    students_path = parser.create_data_path(parameters.get("students"), "students.json")
    dict_students = parser.extract_text(students_path)
    students = {}
    for student in dict_students:
        students.setdefault(student.get("room"), [])
        students[student.get("room")].append(Student.student_mapper(student))

    rooms_path = parser.create_data_path(parameters.get("students"), "rooms.json")
    dict_rooms = parser.extract_text(rooms_path)
    rooms = []
    for room in dict_rooms:
        rooms.append(Room.room_mapper(room))

    for room in rooms:
        room.add_students(students[room.id])

    rooms = [room.to_dict() for room in rooms]
    serializer = serializers.get(parameters.get("format"))
    if parameters.get("format") == "xml":
        serialized_rooms = serializer("rooms").serialize(rooms)
    else:
        serialized_rooms = serializer().serialize(rooms)

    saver = FileSaver(parameters.get("rooms"), output_file_name, parameters.get("format"), "w")
    saver.save(serialized_rooms)


if __name__ == "__main__":
    main()
