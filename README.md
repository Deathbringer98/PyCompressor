PyCompressor
Description:
PyCompressor allows you to easily compress files from multiple folders into a single .rar or .zip file. The program provides a graphical interface (GUI) for selecting folders, file types, and output formats.

Instructions
Run the Program:

1. Start the program by running pycompactor.py. A GUI window will open.
Choose Compression Format:

2. Select either .zip or .rar as the output file format by clicking on the respective radio button.
Select Folders:

3. Click the "Add Folder" button to choose folders containing files you want to compress.
You can add multiple folders, and each selected folder will appear in the list.
To clear the list of folders, use the "Clear Folders" button.
Specify File Types:

4. Enter the file types you want to include, such as .mp3, .txt, etc., separated by commas.
For example, entering .mp3, .txt will include both MP3 and TXT files.
Start Compression:

5. Click "Start Compression". You will be prompted to select the output location and filename for the archive.
The program will collect the specified file types from the selected folders and create a .zip or .rar archive, depending on your choice.
Check for Success Messages:

6. A message will appear once the compression is completed successfully. If there are any issues, an error message will guide you to resolve them.
Repeat or Reset:

After compression, you can choose to compress more files by repeating the steps or click "Reset" to clear all selections for a new task.
Notes:
WinRAR Requirement: If you choose .rar as the output format, ensure that WinRAR is installed. Update the script path to WinRAR if it’s not in your system PATH (e.g., "C:\Program Files\WinRAR\WinRAR.exe").
File Collection: Only files with the specified extensions in the selected folders will be added to the archive.
Example Usage:
Select .zip as the format.
Add folders and enter .mp3, .txt to include all MP3 and TXT files from the chosen directories.
Choose an output location, and the program will create a single .zip file with the specified files.
