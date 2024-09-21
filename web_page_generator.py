
import tkinter as tk
from tkinter import *
import webbrowser
import os

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command= self.defaultHTML)
        self.btn.grid(padx=(10,10) , pady=(10,10))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    if __name__ == "__main__":
        root = tk.Tk()
        App = ParentWindow(root)
        root.mainloop()

    def generate_webpage():
    # Get user input from the text entry widget
    user_input = text_entry.get("1.0", tk.END).strip()
    
    if user_input:
    # Create HTML content with the user input
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Generated Page</title>
</head>
<body>
    <h1>User Input</h1>
    <p>{user_input}</p>
</body>
</html>"""

    # Write the HTML content to a file
    file_path = 'generated_page.html'
    with open(file_path, 'w') as file:
    file.write(html_content)

    # Open the generated web page in a new tab
    webbrowser.open_new_tab('file://' + os.path.realpath(file_path))

    # Create the main application window
    root = tk.Tk()
    root.title("Random Web Page Generator")

    # Create a text entry widget for user input
    text_entry = tk.Text(root, height=10, width=50)
    text_entry.pack(pady=20)

    # Create a button to generate the web page
    generate_button = tk.Button(root, text="Generate Web Page", command=generate_webpage)
    generate_button.pack(pady=10)

    # Start the GUI event loop
    if __name__ == "__main__":
        root = tk.Tk()
        App = ParentWindow(root)
        root.mainloop()

