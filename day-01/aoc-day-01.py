import re
from sys import argv


def replace_numbers(line):
    numbers = ['one:1','two:2','three:3','four:4','five:5','six:6','seven:7','eight:8','nine:9']
    replaced_line = list(line)
    for number in numbers:
        number = number.split(':')
        matches = [n.start() for n in re.finditer(number[0], line)]
        for index in matches:
            replaced_line[index] = str(number[1])
    replaced_line = ''.join(replaced_line)
    return replaced_line

def sum_line(line):
    line_digits = re.findall(r'\d+', line)
    if len(line_digits) == 1:
        line_digits.append(line_digits[0])
    line_values = line_digits[0][0] + line_digits[-1][-1]
    return line_values

with open(argv[1],'r') as input_file:
    calibration_pt1 = 0
    calibration_pt2 = 0
    for line in input_file:
        calibration_pt1 = calibration_pt1 + int(sum_line(line))
        translated_line = replace_numbers(line)
        translated_line = translated_line.replace("\n","")
        calibration_pt2 = calibration_pt2 + int(sum_line(translated_line))
    print("part 1: {}\npart 2: {}".format(calibration_pt1, calibration_pt2))
