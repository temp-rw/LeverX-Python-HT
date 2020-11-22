import re


class Version:
    RE_EXPR = r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)([a-z]*)" \
              r"(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"

    def __init__(self, version: str):
        self.string_version = version
        version = re.split(Version.RE_EXPR, version)
        self.tuple_version = tuple(version[1:-1:1])

    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        if len(self.string_version) != len(other.string_version):
            return False
        else:
            for left, right in zip(self.tuple_version, other.tuple_version):
                if left != right:
                    return False

    def __lt__(self, other):
        # major, minor, patch comparison
        for left, right in zip(self.tuple_version[:4], other.tuple_version[:4]):
            if left < right:
                return True
            elif left > right:
                return False

        # pre-release tail comparison
        for left, right in zip(self.tuple_version[4:], other.tuple_version[4:]):
            if left is None:
                return False
            elif right is None:
                return True
            else:
                inner_left, inner_right = left.split('.'), right.split('.')
                for left_item, right_item in zip(inner_left, inner_right):
                    if left_item.isnumeric() and right_item.isnumeric():
                        if left_item < right_item:
                            return True
                        elif left_item > right_item:
                            return False
                    elif left_item.isnumeric() or right_item.isnumeric():
                        return left_item.isnumeric()
                    elif left_item.isalpha() and right_item.isalpha():
                        if left_item == right_item:
                            continue
                        else:
                            return left_item < right_item

                if len(inner_left) < len(inner_right):
                    return True
                elif len(inner_left) > len(inner_right):
                    return False

    def __le__(self, other):
        if self.__lt__(other):
            return True
        elif self.__eq__(other):
            return True

        return False

    def __gt__(self, other):
        # major, minor, patch comparison
        for left, right in zip(self.tuple_version[:4], other.tuple_version[:4]):
            if left > right:
                return True
            elif left < right:
                return False

        # pre-release tail comparison
        for left, right in zip(self.tuple_version[4:], other.tuple_version[4:]):
            if left is None:
                return True
            elif right is None:
                return False
            else:
                inner_left, inner_right = left.split('.'), right.split('.')
                for left_item, right_item in zip(inner_left, inner_right):
                    if left_item.isnumeric() and right_item.isnumeric():
                        if left_item > right_item:
                            return True
                        elif left_item < right_item:
                            return False
                    elif left_item.isnumeric() or right_item.isnumeric():
                        return left_item.isalpha()
                    elif left_item.isalpha() and right_item.isalpha():
                        if left_item == right_item:
                            continue
                        else:
                            return left_item > right_item

                if len(inner_left) > len(inner_right):
                    return True
                elif len(inner_left) < len(inner_right):
                    return False

    def __ge__(self, other):
        if self.__gt__(other):
            return True
        elif self.__eq__(other):
            return True

        return False

    def __str__(self):
        return self.string_version


def main():
    to_test = [
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0"),
        ("1.0.0-alpha.alpha.alpha", "1.0.0-alpha.alpha.beta")
    ]
    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), "le failed"
        assert Version(version_2) > Version(version_1), "ge failed"
        assert Version(version_2) != Version(version_1), "neq failed"


if __name__ == "__main__":
    main()
