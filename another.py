import os
import tkinter as tk
from tkinter import ttk
import shutil
import glob

from PIL import Image
from PIL import ImageTk
import tkinter

image = Image.open('bangashdownloaded\WhatsApp Image 2020-07-14 at 04.52.21.jpeg')
image = image.resize((20, 20))
image = ImageTk.PhotoImage(image)

canv = Canvas(root, width=80, height=80, bg='white')
canv.grid(row=2, column=3)

img = PhotoImage(file=image)


# # importing only those functions 
# # which are needed 
# from tkinter import *
# from tkinter.ttk import *

# # creating tkinter window 
# root = Tk() 

# # Adding widgets to the root window 
# Label(root, text = 'GeeksforGeeks', font =( 
# 'Verdana', 15)).pack(side = TOP, pady = 10) 

# # Creating a photoimage object to use image 
# photo = PhotoImage(file = r"bangashdownloaded\WhatsApp Image 2020-07-14 at 04.52.21.jpeg") 

# # here, image option is used to 
# # set image on button 
# Button(root, text = 'Click Me !', image = photo).pack(side = TOP) 

# mainloop() 


# import Tkinter as tk

# root = tk.Tk()
# image = tk.PhotoImage(file="bangashdownloaded\WhatsApp Image 2020-07-14 at 04.52.21.jpeg")
# label = tk.Label(image=image)
# label.pack()
# root.mainloop()
# # shutil.copyfile("/Slides/Data Communication and Computer Network/Data Communication and Networks/assignment 1/shahid/WhatsApp Image 2020-07-14 at 04.52.21.jpeg" , "/Slides/Data Communication and Computer Network/Data Communication and Networks/assignment 1/bangash/WhatsApp Image 2020-07-14 at 04.52.21.jpeg")



# master = tk.Tk()
# master.geometry('1200x800')
# master.title('Select a file')

# optmenu = ttk.Combobox(master,  state='readonly')
# optmenu.pack(fill='x')

# # master.mainloop()
# client_name = "bangash"

# user_file_list = glob.glob( client_name + "/*.txt")
# print("./" + client_name + "/*.jpeg")

# print("User file list is " )
# print(user_file_list)
