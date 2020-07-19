import socket
import os
import tkinter.filedialog
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import socket
import threading
import glob
import sys
import struct
import shutil





# BUFFER_SIZE = 1024 # Standard chioce


# Initialise socket stuff
TCP_IP = "127.0.0.1" # Only a local server
TCP_PORT = 1456 # Just a random choice
BUFFER_SIZE = 1024 # Standard chioce
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



window = tk.Tk()
window.title("Client")
username = ""



topFrame = tk.Frame(window)
client_name_label = tk.Label(topFrame, text = "Enter Client Name:").pack(side=tk.LEFT)

client_name_entry = tk.Entry(topFrame)
client_name_entry.pack(side=tk.LEFT )


server_ip_label = tk.Label(topFrame, text = "Enter Server IP").pack(side=tk.LEFT)
# server_ip_label.grid(row =1, column=0)

server_ip_entry = tk.Entry(topFrame)
server_ip_entry.pack(side=tk.LEFT)


server_port_label = tk.Label(topFrame, text = "Enter server port" ).pack(side=tk.LEFT)
server_port_entry = tk.Entry(topFrame)
# server_port_entry.set("8080")
server_port_entry.pack(side=tk.LEFT , padx=5, pady = 5)

connect_button = tk.Button(topFrame,text="Connect", command=lambda : connect()).pack(side=tk.LEFT)
#btnConnect.bind('<Button-1>', connect)
topFrame.pack(side=tk.TOP )

displayFrame = tk.Frame(window)
lblLine = tk.Label(displayFrame, text="*********************************************************************").pack( fill="x")


scrollBar = tk.Scrollbar(displayFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(displayFrame, height=20, width=56)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))


var2 = tk.StringVar()
# var2.set((1,2,3,4))
download_image_listbox = tk.Listbox(displayFrame, listvariable=var2 , width=30, height = 20)

# lb.insert("Select a file " , 1)

download_image_listbox.pack(side=tk.LEFT)

def print_selection():
    value = download_image_listbox.get(download_image_listbox.curselection())
    print("value is ")
    print(value)

    client_folder = value.replace(client_name_entry.get(), client_name_entry.get()+"downloaded")

    shutil.copyfile(value, client_folder)
    # tk.dis
    # var1.set(value)  


def view_selection():
    value = download_image_listbox.get(download_image_listbox.curselection())
    print("hi")

    image = tk.PhotoImage(file=value)
    label = tk.Label(image=image)
    label.pack()

 
download_selected_button = tk.Button(window, text='download Selected image', width=20, height=2, command=print_selection)
download_selected_button.pack( side=tk.RIGHT , padx=(10))

view_selected_button = tk.Button(window, text='View Selected image', width=15, height=2, command=view_selection)
view_selected_button.pack( side=tk.RIGHT , padx=(10))

tkDisplay.tag_config("tag_your_message", foreground="blue")
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(yscrollcommand=scrollBar.set, background="#F4F6F7", highlightbackground="grey", state="disabled")
displayFrame.pack(side=tk.TOP)


bottomFrame = tk.Frame(window)
upload_image_button = tk.Button(bottomFrame, height=2, width=20 , text="Upload" , command = lambda  : select_file_to_upload())
upload_image_button.pack(side=tk.LEFT, padx=5, pady=5)
upload_image_button.config(highlightbackground="blue", state="normal")
# upload_image_button.bind("<Return>", (lambda event: select_file_to_upload()))
bottomFrame.pack(side=tk.BOTTOM)



download_button = tk.Button(bottomFrame, text = "Download Image" ,  height=2, width=20 , command = lambda  : select_file_to_download())
download_button.pack(side=tk.LEFT, padx=5, pady=5)

# download_button.bind("<Return>", (lambda event: select_file_to_download()))

share_image_button = tk.Button(bottomFrame , text = "Share Image", height=2, width=20 ,command = lambda  : select_file_to_share())
share_image_button.pack(side=tk.LEFT, padx=5, pady=5)
# share_image_button.bind("<Return>", (lambda event: select_file_to_share()))


view_image_button = tk.Button(bottomFrame, text = "View Image" ,  height=2, width=20 , command = lambda  : view_image())

view_image_button.pack(side=tk.LEFT, padx=5, pady=5)


def connect():
    global username

    server_ip = server_ip_entry.get()

    server_port = int(server_port_entry.get())
    
    client_name = client_name_entry.get()


    if (len(client_name) < 1) or (len(server_ip) < 1) :
        tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter correct details ")
    else:
        connect_to_server(client_name , server_ip , server_port)

def connect_to_server(username , server_ip, server_port):

    # Connect to the server
    print("Sending server request...")
    try:
        # socket.connect((server_ip,server_port))
        # print("Connection sucessful")
        socket.connect((server_ip, int(server_port)))
        print("Connection sucessful")

        client_folder = "./" +username 
        if not os.path.exists(client_folder):
            os.makedirs(client_folder)
    except Exception as e:
        print("Connection unsucessful. Make sure the server is online.")
        print(e)
    print("hi " + username)
    print(type(username))

def select_file_to_upload():
    # file = tk.askopenfile(mode ='r', filetypes =[('Python Files', '*.py')])
    file = tk.filedialog.askopenfilename(initialdir = "./", multiple = True , filetypes =(("Images", "*.jpeg"),))
    print(file)
    if file is not None: 
        upld(file)

        # with open(file) as f1:

def select_file_to_download():
    client_name = client_name_entry.get()
    
    folder = './' + client_name + 'downloaded'
    if not os.path.exists(folder):
        os.makedirs(folder)

    socket.send("DWLD".encode())
    socket.send(client_name.encode())
    data = socket.recv(49096)
    data = data.decode('utf-8')

    data = eval(data)
    print("data type is ")
    
    print(type(data))

    # list_items = [11,22,33,44]
    for item in data:
        download_image_listbox.insert('end', item)
   

def select_file_to_share():
    file = tk.filedialog.askopenfilename(initialdir = "./shared_directory" , multiple = True , filetypes =(("Images", "*.jpeg"),))
    if file is not None: 
        share(file)


def view_image():
    #  file = tk.filedialog.askopenfile(initialdir = "./shared_directory",mode="r" , multiple = True , filetypes =(("Images", "*.jpeg"),))
    clear_listbox()

    socket.send("VIEW".encode())

    # socket.recv(10000).
    data = socket.recv(10000)
    data = data.decode('utf-8')

    data = eval(data)
    print("data type is ")
    
    print(type(data))

    # list_items = [11,22,33,44]
    for item in data:
        download_image_listbox.insert('end', item)


def upld(file_name):
    # Upload a file
    print("\nUploading file: {}...".format(file_name))
    final_name = "".join(file_name)
    try:
        # Check the file exists
        content = open(final_name, "rb")
    except Exception as e:
        print(e)
        print("Couldn't open file. Make sure the file name was entered correctly.")
        return
    try:
        # Make upload request
        socket.send("UPLD".encode())
    except Exception as e:
        print(e)
        print("Couldn't make server request. Make sure a connection has bene established.")
        return
    try:
        # Wait for server acknowledgement then send file details
        # Wait for server ok
        socket.recv(BUFFER_SIZE)
        # Send file name size and file name
        file_size = sys.getsizeof(final_name)
        socket.send(str(file_size).encode())
        socket.send(final_name.encode())
        socket.recv(1024)
        socket.send(client_name_entry.get().encode())
        server_response =socket.recv(BUFFER_SIZE)
        print("Server Response is " + server_response.decode())
        socket.send("OK".encode())
    except Exception as e:
        print(e)
        print("Error sending file details")
  
    return


def share(file_name):
    # Upload a file
    print("\nUploading file: {}...".format(file_name))
    final_name = "".join(file_name)
    try:
        # Check the file exists
        content = open(final_name, "rb")
    except Exception as e:
        print(e)
        print("Couldn't open file. Make sure the file name was entered correctly.")
        return
    try:
        # Make upload request
        socket.send("SHARE".encode())
    except Exception as e:
        print(e)
        print("Couldn't make server request. Make sure a connection has bene established.")
        return
    try:
        # Wait for server acknowledgement then send file details
        # Wait for server ok
        socket.recv(BUFFER_SIZE)
        # Send file name size and file name
        file_size = sys.getsizeof(final_name)
        socket.send(str(file_size).encode())
        socket.send(final_name.encode())
        socket.recv(1024)
        socket.send(client_name_entry.get().encode())
        server_response =socket.recv(BUFFER_SIZE)
        print("Server Response is " + server_response.decode())
        socket.send("OK".encode())
    except Exception as e:
        print(e)
        print("Error sending file details")
  
    return

def clear_listbox():
    download_image_listbox.delete(0, 'end')


window.mainloop()
