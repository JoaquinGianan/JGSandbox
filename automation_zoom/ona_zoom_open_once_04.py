
# script lounches a schedule to open a recurrent zoom meetin, but first
# it checks to see if a zoom meeting is currently in place;
#  if not, it opens a new zoom meeting (a recurrent meeting),
#  if yes, displays a notice telling there is one
# still looking how to run this script as a background process



import os
import psutil
import schedule

def is_process_running():
    for p in psutil.process_iter(["cmdline"]):
        if p.info["cmdline"] is not None:
            if "/Applications/zoom.us.app/Contents/Frameworks/CptHost.app/Contents/MacOS/CptHost" in p.info["cmdline"]:
                message = "There is a zoom meeting already in place"
                script = f'display notification "{message}"'
                print(message)
                os.system(f"osascript -e '{script}'")
                return True
    return False


# define the meeting id with the full url from the invitation link
def launch_zoom_chat():
    meeting_id = "https://us02web.zoom.us/j/82967180791?pwd=b3kyNHo1a2tuYVNFSEgxb25ob3hqZz09"
    os.system(f"open -a zoom.us '{meeting_id}'")
    return schedule.CancelJob # needed to just run the job once


# Check if the process is already running before scheduling it.
if not is_process_running():
    schedule.every().day.at("17:57").do(launch_zoom_chat)  # runs a job at a certain time every day

while True:
    schedule.run_pending()



if __name__ == "__main__":
    pass


# print(__name__)