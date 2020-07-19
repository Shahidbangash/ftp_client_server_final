import socket
import threading
import tkinter.messagebox
import tkinter as tk
import sys
import time
import os
import struct
from shutil import copyfile
import shutil
import random
import string
import glob


window = tk.Tk()
window.title("Sever")

# Top frame consisting of two buttons widgets (i.e. btnStart, btnStop)
topFrame = tk.Frame(window)
server_start_button = tk.Button(topFrame, text="Connect", command=lambda : start_server())
server_start_button.pack(side=tk.LEFT)
server_stop_button = tk.Button(topFrame, text="Stop", command=lambda : stop_server(), state=tk.DISABLED)
server_stop_button.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP, pady=(5, 0))

# Middle frame consisting of two labels for displaying the host and port info
middleFrame = tk.Frame(window)
label_host = tk.Label(middleFrame, text = "Host: X.X.X.X")
label_host.pack(side=tk.LEFT)
lblPort = tk.Label(middleFrame, text = "Port:XXXX")
lblPort.pack(side=tk.LEFT)
middleFrame.pack(side=tk.TOP, pady=(5, 0))

# The client frame shows the client area
clientFrame = tk.Frame(window)
lblLine = tk.Label(clientFrame, text="**********Client List**********").pack()
scrollBar = tk.Scrollbar(clientFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(clientFrame, height=15, width=30)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(yscrollcommand=scrollBar.set, background="#F4F6F7", highlightbackground="grey", state="disabled")
clientFrame.pack(side=tk.BOTTOM, pady=(5, 10))


server = None
HOST_ADDR = input("Enter ip address")
HOST_PORT = int(input("ENter port"))
client_name = " "
clients = []
clients_names = []

TCP_IP = "127.0.0.1" # Only a local server
TCP_PORT = 1456 # Just a random choice
BUFFER_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((TCP_IP, TCP_PORT))
    print("Connected successfuly " + HOST_ADDR)
    tk.messagebox.showinfo("Success","Connected successfuly " + HOST_ADDR)  
    server.listen(5)  # server is listening for client connection
    conn, addr = server.accept()

    print("\nConnected to by address: {}".format(addr))


    
except  socket.error as e:
        print(e)

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))

    return result_str

    # print("Random string of length", length, "is:", result_str)

def start_server():

    global server, HOST_ADDR, HOST_PORT , TCP_IP , TCP_PORT # code is fine without this


    server_start_button.config(state=tk.DISABLED)
    server_stop_button.config(state=tk.NORMAL)



    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(socket.AF_INET)
    print(socket.SOCK_STREAM)

    try:
        server.bind((TCP_IP, TCP_PORT))
        print("Connected successfuly " + HOST_ADDR)
        tk.messagebox.showinfo("Success","Connected successfuly " + HOST_ADDR)  
        server.listen(5)  # server is listening for client connection
        conn, addr = server.accept()

        print("\nConnected to by address: {}".format(addr))


        while True:
            print("hi")
    except  socket.error as e:
        print(e)

    #     server.bind(loca)

    # threading._start_new_thread(accept_clients, (server, " "))

    # lblHost["text"] = "Host: " + HOST_ADDR
    # lblPort["text"] = "Port: " + str(HOST_PORT)

def stop_server():
    print("hi")
    server.close()
    server_start_button.config(state =tk.NORMAL)
    server_stop_button.config(state =tk.DISABLED)

    
def upld():
    # global conn
    # Send message once server is ready to recieve file details
    conn.send("1".encode())
    # Recieve file name length, then file name
    file_name_size = struct.unpack("h", conn.recv(2))[0]
    print(file_name_size)
    file_name = conn.recv(file_name_size).decode()
    print("Hi i am printing the name of file i recieved")
    print(file_name)

    conn.send("file recieved ".encode())

    client = conn.recv(1024)

    client_name = client.decode()

    print("CLient name is " +client_name)

    x = file_name.split(":", 1)

    print("\nRecieving...")
   
    client_folder = "./" + client_name + "/" + get_random_string(10) + ".jpeg"  
    print("\nRecieved file: {}".format(file_name))
    shutil.copyfile(str(x[1]), client_folder)

    conn.send("Your file has been uploaded to ".encode())
    return




# njmbn,mjn,mn,mnm,n,


def share():
    # global conn
    # Send message once server is ready to recieve file details
    conn.send("1".encode())
    # Recieve file name length, then file name
    file_name_size = struct.unpack("h", conn.recv(2))[0]
    print(file_name_size)
    file_name = conn.recv(file_name_size).decode()
    print("Hi i am printing the name of file i recieved")
    print(file_name)

    conn.send("file recieved ".encode())

    client = conn.recv(1024)

    client_name = client.decode()

    print("CLient name is " +client_name)

    x = file_name.split(":", 1)

    print("\nRecieving...")
   
    client_folder = "./" + "shared_directory" + "/" + get_random_string(10) + ".jpeg"  
    print("\nRecieved file: {}".format(file_name))
    shutil.copyfile(str(x[1]), client_folder)

    conn.send("Your file has been uploaded to ".encode())
    return

def download():

    client_name = conn.recv(1024).decode()

    print("Client name is " + client_name)
    user_file_list = glob.glob(client_name + "/*.jpeg")

    print("User file list is " )
    print(user_file_list)


    conn.send(str(user_file_list).encode())


def view_image():
    user_file_list = glob.glob("shared_directory" + "/*.jpeg")

    print("User file list is " )
    print(user_file_list)


    conn.send(str(user_file_list).encode())


    


while True:
    # Enter into a while loop to recieve commands from client
        print("\n\nWaiting for instruction")
        recieved_data = conn.recv(BUFFER_SIZE)
        print("\nRecieved instruction: {}".format(recieved_data))

        data = recieved_data.decode()
        
    # Check the command and respond correctly
        if data == "UPLD":
            upld()
        elif data == "SHARE":
            share()
            # print("list file to be implemented")
        # list_files()
        elif data == "DWLD":
            download()
            # dwld()
            print("Download function to be implemented")
        elif data == "VIEW":
            view_image()
            
        elif data == "QUIT":
            quit()
    # Reset the data to loop
        data = None


window.mainloop()