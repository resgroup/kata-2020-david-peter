# Session1 kata module
import sys
import datetime

def format_row(length, value, on, off):
    return on * value + off * (length - value)

def first_row(seconds):
    return format_row(1, seconds % 2, 'O', 'Y')

def second_row(hours):
    return format_row(4, hours // 5, 'R', 'O')

def third_row(hours):
    return format_row(4, hours % 5, 'R', 'O')

def fourth_row(minutes):
    return format_row(11, minutes // 5, 'Y', 'O')    

def fifth_row(minutes):
    return format_row(4, minutes % 5, 'Y', 'O')

def berlin_clock(hours, minutes, seconds):
    return f'{first_row(seconds)}\n{second_row(hours)}\n{third_row(hours)}\n{fourth_row(minutes)}\n{fifth_row(minutes)}'

def parse_time(time_str):
    return map(int, time_str.split(':'))

if __name__ == '__main__':
    inputString = datetime.datetime.now().strftime("%H:%M:%S")
    if (len(sys.argv) == 2):
        inputString = sys.argv[1]
    hours, minutes, seconds = parse_time(inputString)
    print(berlin_clock(hours, minutes, seconds))