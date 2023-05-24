import subprocess

def show_notification(title, message):
    command = [
        'osascript',
        '-e',
        f'display notification "{message}" with title "{title}"'
    ]
    subprocess.Popen(command)

# Example usage
show_notification("Hello", "This is a notification message 5.")

if __name__ == "main__":
    pass