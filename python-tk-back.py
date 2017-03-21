#!/usr/bin/python

import Tkinter as tk

## Functions ##
def get_screen_size(window):
    return window.winfo_screenwidth(),window.winfo_screenheight()

def get_window_size(window):
    return window.winfo_reqwidth(),window.winfo_reqheight()

def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    # print(size)
    root.geometry(size)


## Rendering ##
root = tk.Tk()

root.title("Astute-Cloud-Desktop-Installer")

center_window(root, 360, 360)
root.maxsize(360, 360)
root.minsize(360, 360)
background_image=tk.PhotoImage("./bg.gif")

driver_var1 = tk.IntVar()
DR_1 = tk.Checkbutton(root, text = "AT-J60", variable = driver_var1, onvalue = 1, offvalue = 0, height=3, width = 20).grid(row=1, column=0)

driver_var2 = tk.IntVar()
DR_2 = tk.Checkbutton(root, text = "AT-Z221/AT-Z340", variable = driver_var2, onvalue = 1, offvalue = 0, height=3, width = 20).grid(row=2, column=0)

driver_var3 = tk.IntVar()
DR_3 = tk.Checkbutton(root, text = "AT-Remix", variable = driver_var3, onvalue = 1, offvalue = 0, height=3, width = 20).grid(row=3, column=0)

root.mainloop()

