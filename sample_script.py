# sample_script.py

from datetime import datetime

# Print the current date and time to a file
with open("output.txt", "a") as file:
    file.write(f"Script ran at: {datetime.now()}\n")

print("Script executed successfully!")
