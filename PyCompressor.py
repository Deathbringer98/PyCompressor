import os
import subprocess
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox


def collect_files(folders, extensions):
    collected_files = []
    for folder in folders:
        for file in os.listdir(folder):
            if any(file.endswith(ext) for ext in extensions):
                collected_files.append(os.path.join(folder, file))
    return collected_files


def create_zip_archive(files, output_zip):
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for file in files:
            zipf.write(file, arcname=os.path.basename(file))
    messagebox.showinfo("Success", f"Created ZIP archive at {output_zip}")


def create_rar_archive(files, output_rar):
    command = ["C:\\Program Files\\WinRAR\\WinRAR.exe", "a", "-r", output_rar] + files
    try:
        subprocess.run(command, check=True)
        messagebox.showinfo("Success", f"Created RAR archive at {output_rar}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred while creating the RAR archive: {e}")
    except FileNotFoundError:
        messagebox.showerror("Error", "WinRAR not found. Please ensure WinRAR is installed and in your PATH.")


def start_compression():
    format_choice = compression_format.get()
    if format_choice not in {'zip', 'rar'}:
        messagebox.showwarning("Warning", "Please select a compression format.")
        return

    # Collect folders and file types
    extensions = file_types_entry.get().split(',')
    extensions = [ext.strip() for ext in extensions if ext.strip()]
    if not extensions:
        messagebox.showwarning("Warning", "Please enter at least one file type.")
        return

    files_to_compress = collect_files(selected_folders, extensions)
    if not files_to_compress:
        messagebox.showwarning("Warning", "No files found with the specified file types.")
        return

    output_file = filedialog.asksaveasfilename(defaultextension=f".{format_choice}",
                                               filetypes=[("RAR files", "*.rar"), ("ZIP files", "*.zip")])
    if not output_file:
        return

    if format_choice == 'zip':
        create_zip_archive(files_to_compress, output_file)
    elif format_choice == 'rar':
        create_rar_archive(files_to_compress, output_file)


def add_folder():
    folder = filedialog.askdirectory()
    if folder:
        selected_folders.append(folder)
        folders_listbox.insert(tk.END, folder)


def clear_folders():
    selected_folders.clear()
    folders_listbox.delete(0, tk.END)


def reset_app():
    compression_format.set('')
    file_types_entry.delete(0, tk.END)
    clear_folders()


# Initialize main window
root = tk.Tk()
root.title("File Compressor")
root.geometry("500x400")

selected_folders = []

# Compression format selection
tk.Label(root, text="Choose Compression Format:").pack(pady=5)
compression_format = tk.StringVar()
tk.Radiobutton(root, text="ZIP", variable=compression_format, value="zip").pack()
tk.Radiobutton(root, text="RAR", variable=compression_format, value="rar").pack()

# File type input
tk.Label(root, text="Enter File Types to Include (e.g., .mp3, .txt):").pack(pady=5)
file_types_entry = tk.Entry(root, width=50)
file_types_entry.pack()

# Folder selection
tk.Label(root, text="Selected Folders:").pack(pady=5)
folders_listbox = tk.Listbox(root, width=50, height=6)
folders_listbox.pack()

# Folder buttons
folder_buttons_frame = tk.Frame(root)
folder_buttons_frame.pack(pady=5)
tk.Button(folder_buttons_frame, text="Add Folder", command=add_folder).grid(row=0, column=0, padx=5)
tk.Button(folder_buttons_frame, text="Clear Folders", command=clear_folders).grid(row=0, column=1, padx=5)

# Start and Reset buttons
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)
tk.Button(buttons_frame, text="Start Compression", command=start_compression).grid(row=0, column=0, padx=5)
tk.Button(buttons_frame, text="Reset", command=reset_app).grid(row=0, column=1, padx=5)

# Run the application
root.mainloop()
