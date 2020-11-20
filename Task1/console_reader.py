from argparse import ArgumentParser


class ConsoleReader(ArgumentParser):
    """
    Read input from command-line
    """
    def __init__(self):
        super().__init__(description="Parse list of students then group them by rooms.")
        self.add_argument("students", type=str, help="Path to students file")
        self.add_argument("rooms", type=str, help="Path to rooms file")
        self.add_argument("format", type=str, help="Choose output format (JSON or XML)", default="json")
        self.arguments = None

    def read_from_command_line(self) -> dict:
        """
        Parse arguments from command-line
        :return dict: dictionary of parsed arguments
        """
        self.arguments = vars(self.parse_args())
        return self.arguments
