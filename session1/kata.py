# Session1 kata module

def format_row(length, value, on, off):
    result = ''
    for i in range(0, value):
        result = result + on
    for i in range(value, length):
        result = result + off
    return result

def first_row(seconds):
    return format_row(1, seconds % 2, 'O', 'Y')

def second_row(hours):
    return format_row(4, int(hours / 5), 'R', 'O')

def third_row(hours):
    return format_row(4, hours % 5, 'R', 'O')
