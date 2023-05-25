import schedule
import os
import psutil

def launch_zoom_chat(meeting_url):
    os.system(f"open -a zoom.us --args -url '{meeting_url}'")

def is_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

# Set the day and time for the Zoom chat launch (e.g., every Monday at 10:00 AM).
day_of_week = 'monday'
time_of_day = '10:00'

# Specify the recurring meeting URL or ID.
meeting_url = 'https://zoom.us/j/meetingID'  # Replace 'meetingID' with the actual meeting ID or URL.

# Check if the process is already running before scheduling it.
if not is_process_running('launch-zoom-chat.py'):
    schedule.every().tuesday.at(time_of_day).do(launch_zoom_chat, meeting_url=meeting_url)

# Run the scheduled tasks.
while True:
    schedule.run_pending()
