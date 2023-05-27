# checks if a zoom meeting is being held by the host 

import psutil

def is_process_running():
    for p in psutil.process_iter(["cmdline"]):
        if p.info["cmdline"] is not None:
            if "/Applications/zoom.us.app/Contents/Frameworks/CptHost.app/Contents/MacOS/CptHost" in p.info["cmdline"]:
                print("There is a zoom in place")
                return True
    return False
         
           


if __name__ == "__main__":
    is_process_running()



# for p in psutil.process_iter(["name", "exe", "cmdline"]):
#         if name == p.info['name'] or \
#                 p.info['exe'] and os.path.basename(p.info['exe']) == name or \
#                 p.info['cmdline'] and p.info['cmdline'][0] == name: