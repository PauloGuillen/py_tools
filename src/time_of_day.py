from datetime import datetime


def get_time_of_day():
    time = datetime.now()
    if 0 <= time.hour < 6:
        return 'Nigth'
    if 6 <= time.hour < 12:
        return 'Morning'
    if 12 <= time.hour < 18:
        return 'Afternoon'
    return 'Evening'
