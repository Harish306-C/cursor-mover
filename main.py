import tkinter as tk
import threading
import pyautogui
import time

running = False

def move_cursor():
    global running

    while running:
        pyautogui.moveRel(10, 0, duration=0.1)
        pyautogui.moveRel(-10, 0, duration=0.1)
        time.sleep(1)

def start():
    global running

    if not running:
        running = True
        threading.Thread(target=move_cursor, daemon=True).start()
        status_label.config(text="Running")

def stop():
    global running

    running = False
    status_label.config(text="Stopped")

root = tk.Tk()
root.title("Cursor Tool")

# Small floating window
root.geometry("200x120")

# Always stay on top
root.attributes("-topmost", True)

start_btn = tk.Button(root, text="Start", command=start, width=15)
start_btn.pack(pady=5)

stop_btn = tk.Button(root, text="Stop", command=stop, width=15)
stop_btn.pack(pady=5)

status_label = tk.Label(root, text="Stopped")
status_label.pack(pady=5)

root.mainloop()