import tkinter as tk

root = tk.Tk()
list = [1,2,3]
# Create widgets
list[1] = tk.Button(root, text=list[1])
label2 = tk.Label(root, text=4)

# Place widgets in the grid
list[1].grid(row=0, column=0)
label2.grid(row=1, column=2)

root.mainloop()
print("hi")