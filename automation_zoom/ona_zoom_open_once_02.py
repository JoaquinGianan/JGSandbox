# this script opens the zoom meeting link in the default browser, bur using a function to do it

import os

# define the meeting id with the full url from the invitation link
def launch_zoom_chat():
    meeting_id = "https://us02web.zoom.us/j/82967180791?pwd=b3kyNHo1a2tuYVNFSEgxb25ob3hqZz09"
    os.system(f"open -a zoom.us '{meeting_id}'")


if __name__ == "__main__":
    launch_zoom_chat()