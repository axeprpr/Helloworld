#!/usr/bin/python

from Tkinter import *
import ConfigParser
import random
import urllib2


server = "unknown"
my_id = "null"

def connect_desktop():
    if server == "unknown":
        return
    else:
        pass




# try:
conf = ConfigParser.ConfigParser()
conf.read("frp/frpc.ini")
server_addr = conf.get("common", "server_addr")
server_port = conf.get("common", "server_port")

server_tcp_url = "http://" + server_addr + ":7500" + "/api/proxy/tcp"
print server_tcp_url
request = urllib2.Request(server_tcp_url)
response = urllib2.urlopen(request).read()
print response
my_id = conf.get("rdp", "remote_port")
server = server_addr+":"+server_port
# except:
#     pass



root = Tk()
root.title("AstuteRemoteDesktop")
width ,height= 300, 85
root.geometry('%dx%d+%d+%d' % (width,height,(root.winfo_screenwidth() - width ) / 2, (root.winfo_screenheight() - height) / 2))
root.maxsize(300,85)


Label(root, text="Server:").grid(row=2, column=0, sticky="W")
Label(root, text=server).grid(row=2, column=1, sticky="W")
Entry(root,  width=10).grid(row=4, column=1, sticky="W")
# Button(root, text="..", command=set_server).grid(row=2, column=2, sticky="W")

Label(root, text="Your ID:").grid(row=3, column=0, sticky="W")
Label(root, text=my_id, fg="red").grid(row=3, column=1, sticky="W")

Label(root, text="Connect To:").grid(row=4, column=0, sticky="W")
Entry(root,  width=10).grid(row=4, column=1, sticky="W")
Button(root, text="Connect", command=connect_desktop).grid(row=4, column=2, sticky="W")

root.mainloop()

