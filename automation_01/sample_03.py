import subprocess

def show_message(title, message):
    line = ['osascript' , '-e' , f'display notification "{message}" with title "{title}"']
    subprocess.Popen(line)
show_message("This is a notification", "This is the message 3")

if __name__ == '__main__':
    pass

