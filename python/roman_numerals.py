class RomanNumeral:
    def __init__(self, number):
        roman_symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # algo for roman-decimal conversion
        # reversing the string
        roman = number[::-1]
        result = 0
        temp = [roman_symbols[roman[0]], ]
        for i in range(len(roman) - 1):
            if roman_symbols[roman[i + 1]] >= roman_symbols[roman[i]]:
                temp.append(roman_symbols[roman[i + 1]])
            else:
                temp.append(-roman_symbols[roman[i + 1]])
                result = result + sum(temp)
                temp = []
        result = result + sum(temp)

        # every 1xxx number can't repeat 4 times and every 5xxx number can't repeat twice,
        # every "roman number"*2=="another roman number" scenario
        # number longer than 9 can't be valid, because max num length is MMMCMXCVIII
        forbidden_combinations = ['LC', 'DM', 'IIII', 'VV', 'XX', 'LL', 'CCCC', 'MMMM', 'VX']
        for case in forbidden_combinations:
            if result > 3999 or len(number) > 10 or case in number:
                raise Exception("This roman numeral doesn't exist")

        self.number = number
        self.roman_symbols = roman_symbols
        self.result = result

    def roman_to_decimal(self):
        print(self.result)
        return self.result


if __name__ == '__main__':
    roman_number = RomanNumeral('MMMCMXCIX')
    roman_number.roman_to_decimal()