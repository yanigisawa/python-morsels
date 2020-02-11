from functools import total_ordering
from operator import itemgetter


@total_ordering
class RomanNumeral:
    DIGITS = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }

    def __init__(self, numeral):
        self.numeral = numeral
        self.numbers = [self.DIGITS[n] for n in numeral]

    def __int__(self):
        tmp_numbers = self.numbers + [0]
        total, i = 0, 0
        while i < len(self.numbers):
            if tmp_numbers[i + 1] <= tmp_numbers[i]:
                total += tmp_numbers[i]
                i += 1
                continue
            total = total + (tmp_numbers[i + 1] - tmp_numbers[i])
            i += 2
        return total

    def __add__(self, other):
        return RomanNumeral.from_int(int(self) + int(other))

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        return int(self) == int(other)

    def __lt__(self, other):
        if isinstance(other, str):
            raise TypeError
        return int(self) < int(other)

    def from_int(number):
        def find_largest_numeral(digit):
            digits = sorted(RomanNumeral.DIGITS.items(), key=itemgetter(1))
            for k, v in digits:
                if v > digit:
                    return highest
                highest = k
            return highest

        tmp_number = number
        numeral = ""
        while tmp_number > 0:
            tmp = find_largest_numeral(tmp_number)
            numeral += tmp
            tmp_number -= RomanNumeral.DIGITS[tmp]
        return RomanNumeral(numeral)

    def __repr__(self):
        return f"RomanNumeral('{self.numeral}')"

    def __str__(self):
        return self.numeral

