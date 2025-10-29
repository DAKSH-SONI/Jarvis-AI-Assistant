import datetime
def get_datetime():
    """Return current date and time as a formatted string"""
    now = datetime.datetime.now()
    current_datetime = now.strftime("%I:%M %p \n %A, %B %d, %Y  ")
    return current_datetime
