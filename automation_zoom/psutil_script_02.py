import psutil

# Iterate over all running processes
for process in psutil.process_iter(['pid', 'name']):
    # Get the process ID and name
    process_id = process.info['pid']
    process_name = process.info['name']
    print(f"Process ID: {process_id}, Name: {process_name}")


if __name__ == '__main__':
    pass
