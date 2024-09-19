import tkinter as tk
from tkinter import Frame, Button, Entry, filedialog
import os
import shutil
import time

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master = master
        self.master.title("File Transfer")

        # Create buttons and entry widgets
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        self.source_dir = Entry(width=75)
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        self.destination_dir = Entry(width=75)
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    def sourceDir(self):
        selectSourceDir = filedialog.askdirectory()
        self.source_dir.delete(0, tk.END)
        self.source_dir.insert(0, selectSourceDir)

    def destDir(self):
        selectDestDir = filedialog.askdirectory()
        self.destination_dir.delete(0, tk.END)
        self.destination_dir.insert(0, selectDestDir)

    def transferFiles(self):
        source = self.source_dir.get()
        destination = self.destination_dir.get()
        current_time = time.time()

        # Get a list of files in the source directory
        source_files = os.listdir(source)

        # Check for files modified in the last 24 hours
        for file_name in source_files:
            file_path = os.path.join(source, file_name)
            if os.path.isfile(file_path):  # Ensure it's a file
                last_modified_time = os.path.getmtime(file_path)
                # Check if the file was modified in the last 24 hours (86400 seconds)
                if current_time - last_modified_time <= 86400:
                    shutil.move(file_path, destination)
                    print(f'{file_name} was successfully transferred.')

    def exit_program(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
