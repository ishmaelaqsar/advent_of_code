INPUT = "input.txt"

MAPP = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def check_string(string, digits):
    string = MAPP[string] if string in MAPP else string
    if string.isdigit():
        digits[1] = string
        if not digits[0]:
            digits[0] = string


def get_calibration_value(text):
    digits = [None, None]

    for i in range(len(text)):
        for j in range(len(text) + 1):
            sub = text[i:j]
            check_string(sub, digits)

    if not digits[0]: return 0
    return int(digits[0] + digits[1])


def main():
    sum = 0
    with open(INPUT, 'r') as file:    
        for line in file:
            sum += get_calibration_value(line)
    print('Result:', sum)


if __name__ == "__main__":
    main()
