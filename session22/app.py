# GUI
# Tkinter
# main --> module --> package
import tkinter as tk
import main

window = tk.Tk()

frame = tk.Frame(master=window, width=500, height=500, bg="red")
frame.pack(fill=tk.Y, side=tk.LEFT)

username = tk.Label(
    master=frame,
    text="Username",
    fg="white",
    bg="black",
    width=20,
    height=2
)
username.place(x=0, y=0)


username_input = tk.Entry(master=frame,)
username_input.place(x=150, y=0)


def load_bank_system():
    main.main()

btn = tk.Button(
    master=frame,
    text='click me',
    width=25,
    height=2,
    bg="blue",
    fg="white",
    command=load_bank_system
)
btn.place(x=20, y=100)






window.mainloop()