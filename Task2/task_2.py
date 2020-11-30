from typing import List
from functools import total_ordering


@total_ordering
class Version:

    # Weights for alphabetic version identifiers
    # May be expanded.
    ALPHA_VERSION_WEIGHTS = {"alpha": 1, "beta": 2, "rc": 3}

    def __init__(self, version: str):
        self.string_version = version
        if len(self.string_version.split("-")) > 1:
            self.head, self.tail = self.string_version.split("-")
        else:
            self.head, self.tail = self.string_version.split("-")[0], ""

        self.head = self.head.split(".")
        self.tail = self.tail.split(".")

    def __eq__(self, other):
        if len(self.string_version) != len(other.string_version):
            return False
        else:
            return self.string_version == other.string_version

    def __lt__(self, other):
        """
        Compare left-side value with right-side value.
        Every version identifier gets it's own weight in strings_to_coefficients function
        then compare them using this function.
        Comparing algorithm:
        Every next version identifier gets it's weight divided by 10 and normalized by using biggest
        coefficient in comparing pair.
        :param other:
        :return:
        """
        right_sum, left_sum = 0, 0
        coef = 1

        left_side = self.strings_to_coefficients(self.head)
        right_side = self.strings_to_coefficients(other.head)

        for left_element, right_element in zip(left_side, right_side):
            if max(left_element, right_element) > 0:
                norm = max(left_element, right_element)
            else:
                norm = 1.0

            left_sum += (left_element / norm) * coef
            right_sum += (right_element / norm) * coef
            coef /= 10.0
            if right_sum != left_sum:
                return left_sum < right_sum

        if len(left_side) != len(right_side):
            return len(left_side) < len(right_side)

        right_sum, left_sum = 0, 0
        coef = 1

        left_side = self.strings_to_coefficients(self.tail)
        right_side = self.strings_to_coefficients(other.tail)

        if len(left_side) == 0 or len(right_side) == 0:
            return len(left_side) > len(right_side)

        for left_element, right_element in zip(left_side, right_side):
            norm = max(left_element, right_element)
            left_sum += (left_element / norm) * coef
            right_sum += (right_element / norm) * coef
            coef /= 10.0
            if right_sum != left_sum:
                return left_sum < right_sum

        return len(left_side) < len(right_side)

    @staticmethod
    def strings_to_coefficients(strings: List[str]) -> List[int]:
        """
        Takes list of splitted version string, then gives weight to each element according to the rule:
        1) integers are casted from string using int(),
        2) alpha, beta and etc are converted using ALPHA_VERSION_WEIGHTS dictionary,
        3) every single letter gets it's code according to ASCII table.
        :param strings: splitted version string
        :return list: List of corresponding coefficients
        """
        coefficient_list = []
        for string in strings:
            if string.isalpha():
                coefficient_list.append(Version.ALPHA_VERSION_WEIGHTS.get(string) * 1000)
            elif string.isnumeric():
                coefficient_list.append(int(string))
            elif string.isalnum():
                num = []
                alpha = []
                for symbol in string:
                    if symbol.isnumeric():
                        num.append(symbol)
                    else:
                        alpha.append(ord(symbol))

                num = "".join(num)
                num = int(num)
                coefficient_list.extend([num, alpha])
        return coefficient_list

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
        ("1.0.0-alpha.alpha.alpha", "1.0.0-alpha.alpha.beta"),
        ("1.0.0-alpha.10", "1.0.0-alpha.alpha"),
    ]
    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), "le failed"
        assert Version(version_2) > Version(version_1), "ge failed"
        assert Version(version_2) != Version(version_1), "neq failed"


if __name__ == "__main__":
    main()
