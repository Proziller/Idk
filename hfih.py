import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root, bg='gray', width=400, height=400)
frame.grid(row=0, column=0)

# Add widgets to the Frame
label = tk.Label(frame, text="Hello")
label.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=1, column=0)

button = tk.Button(frame, text="Submit")
button.grid(row=2, column=0)

root.mainloop()