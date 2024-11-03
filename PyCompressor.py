import os
import subprocess

# Set the directory containing MP3 files and the output RAR file
# Update these paths as needed
mp3_folder = r"Your\Path\To\MP3_Folder"
output_rar = r"Your\Path\To\Output\Archive.rar"

# Collect all .mp3 files in the specified directory
mp3_files = [os.path.join(mp3_folder, file) for file in os.listdir(mp3_folder) if file.endswith('.mp3')]


def create_rar_archive(mp3_folder, output_rar):
    """
    Creates a RAR archive containing all .mp3 files in the specified folder.

    Parameters:
    mp3_folder (str): Path to the folder containing .mp3 files.
    output_rar (str): Path where the .rar file will be saved.
    """
    # Replace with the full path to WinRAR.exe if it's not in your system PATH
    command = [r"C:\Program Files\WinRAR\WinRAR.exe", "a", "-r", output_rar, os.path.join(mp3_folder, "*.mp3")]

    try:
        # Run the WinRAR command and create the archive
        subprocess.run(command, check=True)
        print(f"Created RAR archive at {output_rar}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while creating the archive: {e}")
    except FileNotFoundError:
        print("WinRAR not found. Please ensure WinRAR is installed and added to your PATH.")


if __name__ == "__main__":
    if mp3_files:
        create_rar_archive(mp3_folder, output_rar)
    else:
        print("No MP3 files found in the specified directory.")
