import os

from mysql.connector.errors import IntegrityError

from console_reader import ConsoleReader
from db_manager import DBManager
from file_parser import JSONParser
from output import FileSaver
from queries import *
from serializers import JSONSerializer, XMLSerializer


def main():
    db_option_file_path = "./main.cnf"
    serializers = {"json": JSONSerializer, "xml": XMLSerializer}
    command_reader = ConsoleReader()
    parameters = command_reader.read_from_command_line()

    output_path = os.getcwd()
    parser = JSONParser()

    students_path = parser.create_data_path(parameters.get("students"), "students.json")
    dict_students = parser.extract_text(students_path)
    if not isinstance(dict_students, list):
        dict_students = list(dict_students)

    rooms_path = parser.create_data_path(parameters.get("students"), "rooms.json")
    dict_rooms = parser.extract_text(rooms_path)
    if not isinstance(dict_rooms, list):
        dict_rooms = list(dict_rooms)

    db_manager = DBManager(option_files=db_option_file_path)
    try:
        db_manager.create("rooms", columns_values=dict_rooms)
        db_manager.create("students", columns_values=dict_students)
    except IntegrityError as err:
        pass

    serializer = serializers.get(parameters.get("format"))
    list_of_dict_students = db_manager.get_data_by_custom_query(
        ["id", "name", "students_in_room"], num_of_students_in_rooms
    )
    serialized = serializer().serialize(list_of_dict_students)
    saver = FileSaver(output_path, "num_of_students_in_rooms", parameters.get("format"), "w")
    saver.save(serialized)

    list_of_dict_students = db_manager.get_data_by_custom_query(["id", "name"], top5_rooms_lowest_avg_age)
    serialized = serializer().serialize(list_of_dict_students)
    saver = FileSaver(output_path, "top5_rooms_lowest_avg_age", parameters.get("format"), "w")
    saver.save(serialized)

    list_of_dict_students = db_manager.get_data_by_custom_query(["id", "name"], top5_rooms_biggest_age_diff)
    serialized = serializer().serialize(list_of_dict_students)
    saver = FileSaver(output_path, "top5_rooms_biggest_age_diff", parameters.get("format"), "w")
    saver.save(serialized)

    list_of_dict_students = db_manager.get_data_by_custom_query(["id", "name"], rooms_with_diff_sex)
    serialized = serializer().serialize(list_of_dict_students)
    saver = FileSaver(output_path, "rooms_with_diff_sex", parameters.get("format"), "w")
    saver.save(serialized)


if __name__ == "__main__":
    main()
