# Session1 kata module

def first_row(seconds):
    if(seconds %2)==0:
        return 'Y'
    else:
        return 'O'

def second_row(hours):
    if (hours < 5):
        return 'OOOO'
    elif (hours < 10):
        return 'ROOO'
    elif (hours < 15):
        return 'RROO'
    elif (hours < 20):
        return 'RRRO'
    else:
        return 'RRRR'
