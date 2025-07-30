import os
import time

# Directory containing the files
directory = "H:/o/"

# Iterate through files in the directory
while True:
    try:
        time.sleep(1)
        for filename in os.listdir(directory):
            if filename.startswith("1_") and filename.endswith(".mp4"):
                new_name = filename[2:]  # Remove the "e_" prefix
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_name)
                os.rename(old_path, new_path)
                if new_name.endswith(".mp4.mp4"):
                    final_name = new_name[:-4]  # Remove the extra ".mp4"
                    final_path = os.path.join(directory, final_name)
                    os.rename(new_path, final_path)
                    print(f'Renamed: {filename} -> {final_name}')
                else:
                    print(f'Renamed: {filename} -> {new_name}')
    except:
        pass