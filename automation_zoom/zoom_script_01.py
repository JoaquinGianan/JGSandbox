import schedule
import os

# launches a defined zoom meeting



def launch_zoom_chat():
    meeting_id = "https://us02web.zoom.us/j/82967180791?pwd=b3kyNHo1a2tuYVNFSEgxb25ob3hqZz09"
    os.system(f"open -a zoom.us '{meeting_id}'")

# Set the day and time for the Zoom chat launch (e.g., every Monday at 10:00 AM).
day_of_week = 'tuesday'
time_of_day = '10:30'

# Schedule the launch of the Zoom chat.
schedule.every().tuesday.at(time_of_day).do(launch_zoom_chat)

# Run the scheduled tasks.
while True:
    schedule.run_pending()

if __name__ == "__main__":
    # launch_zoom_chat()
    pass