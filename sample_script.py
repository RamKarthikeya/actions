import os
from datetime import datetime

# Debug: Print the current working directory
print(f"Current working directory: {os.getcwd()}")

# Create or overwrite output.txt
with open("output.txt", "w") as f:
    f.write(f"Script ran at: {datetime.now()}\n")

print("Output file created successfully.")
