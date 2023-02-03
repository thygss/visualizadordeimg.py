import tkinter as tk
from tkinter import filedialog
from PIL import Image

def convert_webp_to_png():
    filepath = filepath_entry.get()
    try:
        im = Image.open(filepath)
        png_filepath = filepath.replace('.webp', '.png')
        im.save(png_filepath)
        status_label.config(text='File converted successfully')
    except:
        status_label.config(text='Error: Invalid file or filepath')
        
def select_file():
    filepath = filedialog.askopenfilename()
    filepath_entry.delete(0, 'end')
    filepath_entry.insert(0, filepath)

root = tk.Tk()
root.config(bg='#2d2d2d')
root.title("Webp to PNG Converter")

filepath_label = tk.Label(root, text='Enter filepath:', bg='#2d2d2d', fg='white')
filepath_label.grid(row=0, column=0, padx=10, pady=10)

filepath_entry = tk.Entry(root, bg='#2d2d2d', fg='white', width=30)
filepath_entry.grid(row=0, column=1, padx=10, pady=10)

select_file_button = tk.Button(root, text='Select File', bg='#2d2d2d', fg='white', command=select_file)
select_file_button.grid(row=0, column=2, padx=10, pady=10)

convert_button = tk.Button(root, text='Convert to PNG', bg='#2d2d2d', fg='white', command=convert_webp_to_png)
convert_button.grid(row=1, columnspan=3, padx=10, pady=10)

status_label = tk.Label(root, text='', bg='#2d2d2d', fg='white')
status_label.grid(row=2, columnspan=3, padx=10, pady=10)

root.mainloop()
