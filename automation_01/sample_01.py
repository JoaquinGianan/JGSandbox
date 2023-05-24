import os

def show_notification(title, message, sound_name=None):
    script = f'display notification "{message}" with title "{title}"'
    if sound_name:
        script += f' sound name "{sound_name}"'
    os.system(f"osascript -e '{script}'")

# Example usage
show_notification("Hello", "This is a notification message 1.", sound_name="Glass")

# script = f'display notification "Floo" with title "dos"'
# script += f' sound name "tres"'


if __name__ == "__main__":
    pass
   