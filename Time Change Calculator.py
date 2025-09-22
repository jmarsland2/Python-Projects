# John Marsland last edited 9/22/25

def add_time(start, duration, day=''):

    # Define starting day
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    start_day = days.index(day.lower()) if day else 0

    # Define 24 hr start time for hour
    start_hour = int(start[0]) if len(start) == 7 else int(start[0:2])

    # adjust hour for AM/PM
    if start[-2:] == 'PM':
        if start_hour != 12:
            start_hour += 12

    # Define minute count of start time
    start_mins = int(start[-5:-3])

    # Define hours and minutes of change
    change = duration.split(':')
    hour_change = int(change[0])
    min_change = int(change[1])

    # Initialize end time calculation
    end_hour = start_hour + hour_change
    end_min = start_mins + min_change
    day_count = 0
    end_day = start_day

    # Adjust end time and end date to follow formatting
    while end_min >= 60:
        end_min -= 60
        end_hour += 1

    while end_hour >= 24:
        end_hour -= 24
        day_count += 1    

    # Optional conditional for when day is specified
    day_message = ''
    days_past = ''
    if day:
        end_day = start_day + day_count
        while end_day >= 7:
            end_day -= 7
        end_day = days[end_day]
        end_day = end_day[0].upper() + end_day[1:]
        day_message = f', {end_day}'
 
    # Begin formatting of hour
    # Format for AM vs PM
    if end_hour >= 12:
        part_day = 'PM'
        final_hour = end_hour - 12 if end_hour != 12 else end_hour
    else:
        part_day = 'AM'
        final_hour = end_hour
        # Check if its midnight
        final_hour = 12 if final_hour == 0 else final_hour

    # base form time message
    if end_min < 10:
        time_message = f'{final_hour}:0{end_min} {part_day}'
    else: 
        time_message = f'{final_hour}:{end_min} {part_day}'
    
    # Include current day if necessary
    if day_message:
        time_message += day_message

    # include day count if necessary
    if day_count == 1:
        time_message += ' (next day)'
    elif day_count > 1:
        time_message += f' ({day_count} days later)'

    return time_message

print('''Enter the current time, time to add, and the current day of the week.''')
start_time = input('Enter start time [hour:minute] [AM/PM]: ')
change_time = input('Enter hours and minutes to add [hours:minutes]: ')
current_day = input('Enter the current day of the week: ')
print(add_time(start_time, change_time, current_day))
