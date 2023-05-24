import os

def show_notification(title, message, sound_names=None):
    script = f'display notification "{message}" with title "{title}"'
    if sound_names:
        sound_commands = [f' sound name "{sound_name}"' for sound_name in sound_names]
        script += ' '.join(sound_commands)
    # print(script)    
    os.system(f"osascript -e '{script}'")

# Example usage


if __name__ == "__main__":
    show_notification("Hello", "This is anoter notification message 4 .  With two ring tones.", sound_names=["Glass", "Basso"])

# must fix the double sound definition \\ check osascript sintax


