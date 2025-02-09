import time
import random
import threading
import tkinter as tk
from tkinter import messagebox

# Define Websites to Block
blocked_sites = ['www.youtube.com']

# Define Hosts File Path
HOSTS_PATH = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
REDIRECT_IP = "127.0.0.1"

# Function to Block Websites
def Block():
    with open(HOSTS_PATH, 'r+') as file:
        content = file.read()
        for site in blocked_sites:
            if site not in content:
                file.write(f'{REDIRECT_IP} {site}\n')
    print('Websites blocked successfully')

# Function to Unblock Websites
def Unblock():
    with open(HOSTS_PATH, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not any(site in line for site in blocked_sites):
                file.write(line)
        file.truncate()
    print('Websites unblocked successfully')

# Reward System
def Reward_user():
    messages = ["Great job! You are studying well!", "You are becoming powerful!", "Good job, keep studying!"]
    reward = random.choice(messages)
    messagebox.showinfo("Reward", reward)

# Function to Start Blocking
def Start_blocking():
    try:
        delay = int(entry.get()) * 60  # Convert minutes to seconds
        entry.delete(0, tk.END)  # Clear input field
        root.withdraw()  # Hide the Tkinter window instead of destroying it
        
        Block()
        threading.Thread(target=wait_and_unblock, args=(delay,), daemon=True).start()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of minutes.")

# Function to Unblock after delay
def wait_and_unblock(delay):
    time.sleep(delay)
    Unblock()
    Reward_user()
    root.quit()

# Tkinter GUI Setup
root = tk.Tk()
root.title("Study Session Blocker")
root.geometry("400x200")

label = tk.Label(root, text="Enter study session duration (minutes):", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

start_button = tk.Button(root, text="Start", command=Start_blocking, font=("Arial", 12), bg="green", fg="white")
start_button.pack(pady=10)

root.mainloop()