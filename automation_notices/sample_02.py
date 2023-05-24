import os

def show_notification(title, message):
    command = f'display notification "{message}" with title "{title}"'
    os.system(f"osascript -e '{command}'")

# Usage example
show_notification("Notification Example 2", "Tell me when it is time to go!")


if __name__ == "__main__":
    pass
    print("Done")
 

