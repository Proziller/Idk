import tkinter as tk

def handle_key(event):
    print(f"Key pressed: {event.keysym}")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()

root.bind("<KeyRelease>", handle_key)

root.mainloop()
