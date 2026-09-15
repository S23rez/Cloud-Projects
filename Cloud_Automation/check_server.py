import platform
import os

# Get the OS details of where this script is running
print(f"Server OS: {platform.system()} {platform.release()}")
# Show the current user on the droplet
print(f"Logged in as user: {os.getlogin()}")
# Confirm the directory on the droplet
print(f"Current server directory: {os.getcwd()}")
