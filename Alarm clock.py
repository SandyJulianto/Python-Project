# Import required modules
from datetime import datetime
from playsound import playsound
# Input alarm time
set_alarm = input("Enter alarm time in format 'HH:MM:SS AM/PM' : ")
# Detail of hour, minutes, seconds and period
alarm_hour = set_alarm[0:2]
alarm_minute = set_alarm[3:5]
alarm_second = set_alarm[6:8]
alarm_period = set_alarm[9:]
# Will occur if input format is incorrect and vice versa
if len(set_alarm) != 11:
    print("Invalid format, Please enter again...")
else:
    print("Setup a alarm...")
# Loops for checking current time
while True:
    n = datetime.now()
    current_hour = n.strftime("%I")
    current_minute = n.strftime("%M")
    current_second = n.strftime("%S")
    current_period = n.strftime("%p")
    # Happen when alarm time and current time match
    if current_hour == alarm_hour:
        if current_minute == alarm_minute:
            if current_second == alarm_second:
                if current_period == alarm_period:
                    print("Wake Up!!!")
                    playsound()
                    # Stopping
                    break