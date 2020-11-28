from console_reader import ConsoleReader
from data import Student, Room
from file_parser import JSONParser
from output import FileSaver
from serializers import JSONSerializer, XMLSerializer
from db_manager import DBManager


def main():
    serializers = {"json": JSONSerializer, "xml": XMLSerializer}
    # command_reader = ConsoleReader()
    # parameters = command_reader.read_from_command_line()
    parameters = {
        "students": r"D:\Python\LeverX HT\LeverX-Python-HT\Task4",
        "rooms": r"D:\Python\LeverX HT\LeverX-Python-HT\Task4",
        "format": "json"
    }
    output_file_name = "rooms_with_students"
    parser = JSONParser()

    students_path = parser.create_data_path(parameters.get("students"), "students.json")
    dict_students = parser.extract_text(students_path)
    if not isinstance(dict_students, list):
        dict_students = list(dict_students)

    for index, student in enumerate(dict_students):
        dict_students[index] = Student.student_mapper(student).to_dict()

    rooms_path = parser.create_data_path(parameters.get("students"), "rooms.json")
    dict_rooms = parser.extract_text(rooms_path)
    if not isinstance(dict_rooms, list):
        dict_rooms = list(dict_rooms)

    for index, room in enumerate(dict_rooms):
        dict_rooms[index] = Room.room_mapper(room).to_dict()

    db_manager = DBManager(host="127.0.0.1", user="root", password="1721185", database="roomsdb")
    db_manager.create("rooms", columns_values=dict_rooms)
    db_manager.create("students", columns_values=dict_students)


if __name__ == "__main__":
    main()
