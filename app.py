from tkinter import *
import subprocess


root = Tk()

root.geometry("600x200")

# SSH into other PC and modify page content
def editWebpage():
    subprocess.Popen(f"ssh {userName}@{hostName} {cmd}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

# Test SSH connection by running ls
cmd = 'ls'
userName = Entry(root, text="user")
userName.insert(END, 'User')
userName.pack()
hostName = Entry(root, text="host")
hostName.insert(END, 'Host')
hostName.pack()

submit = Button(root, text="Edit Page", command=lambda: editWebpage())
submit.pack()





root.mainloop()