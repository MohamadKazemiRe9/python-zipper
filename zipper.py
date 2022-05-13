import os
import zipfile
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import END, Label, messagebox

window = tk.Tk()
window.minsize(200, 200)
window.maxsize(200, 200)

def open_file():
    filename = askopenfilename(title="Select a zip file",filetypes = (("Zip file", "*.zip"),("All files", "*.*")))
    try:
        with zipfile.ZipFile(filename, mode="r") as archive:
            # archive.printdir()
            lbl_file_address["text"] = filename
    except:
        print("file not found")

def extract_file():
    save_address = askdirectory()
    lbl_destination_address["text"] = save_address

    if ent_folder_name.get() != "":
        file_name = ent_folder_name.get()
    else:
        file_name = os.path.basename(lbl_file_address["text"]).split(".")[0]
    print(file_name)
    dest_address = os.path.join(save_address, file_name)
    
    try:
        with zipfile.ZipFile(lbl_file_address["text"], mode="r") as archive:
            # archive.printdir()
            archive.extractall(dest_address)
    except:
        print("Can't extract file")

menubar = tk.Menu(window)
file = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='Open', command = open_file)

# open_btn = tk.Button(window, text="Open" ,command=open_file)
# open_btn.grid(row=0,)

extract_btn = tk.Button(window, text="Extract" ,command=extract_file)
extract_btn.grid(row=0,)

lbl_file_address = tk.Label(window)
lbl_destination_address = tk.Label(window)

lbl_file_address.grid(row=1)
lbl_destination_address.grid(row=2)

lbl_extract = Label(window, text="Enter folder name")
lbl_extract.grid(row=3)

ent_folder_name = tk.Entry(window)
# ent_folder_name.insert(0, 'Enter folder name')
ent_folder_name.grid(row=4)

extract_btn.grid(row=5)

window.config(menu = menubar)
window.mainloop()