import schedule
import os

def launch_zoom_chat(meeting_url):
    os.system(f"open -a zoom.us --args -url '{meeting_url}'") #must change this line

# Set the day and time for the Zoom chat launch (e.g., every Monday at 10:00 AM).
day_of_week = 'monday'
time_of_day = '10:00'

# Specify the recurring meeting URL or ID.
meeting_url = 'https://zoom.us/j/meetingID'  # Replace 'meetingID' with the actual meeting ID or URL.

# Schedule the launch of the Zoom chat with the specified recurring meeting.
schedule.every().monday.at(time_of_day).do(launch_zoom_chat, meeting_url=meeting_url)

# Run the scheduled tasks.
while True:
    schedule.run_pending()
