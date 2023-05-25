# this script opens the zoom meeting link in the default browser, you must declare in the zoom app to open automatically

import os
import psutil


# check to see if a zoom meeting is currently in place
def is_process_running():
    for p in psutil.process_iter(["cmdline"]):
        if p.info["cmdline"] is not None:
            if "/Applications/zoom.us.app/Contents/Frameworks/CptHost.app/Contents/MacOS/CptHost" in p.info["cmdline"]:
                print("There is a zoom in place") # add a notification also
                return True
    return False


# define the meeting id with the full url from the invitation link
def launch_zoom_chat():
    meeting_id = "https://us02web.zoom.us/j/82967180791?pwd=b3kyNHo1a2tuYVNFSEgxb25ob3hqZz09"
    os.system(f"open -a zoom.us '{meeting_id}'")


# Check if the process is already running before scheduling it.
if not is_process_running():
    launch_zoom_chat()


if __name__ == "__main__":
    pass