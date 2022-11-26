import tkinter as tk
import os
import sqlite3 
from tkinter import *
from tkinter import ttk


root = tk.Tk()

#root = Tk()
root.title('Scroll Bar')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("1000x600")

def printMessage():
    print("Worked")
######################################################################
def ScrollWindow():
    def logout():
        print("Logout Pressed")
    #main frame
    main_frame= Frame(root)
    main_frame.pack(fill=BOTH, expand=1)

    #Create a canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    #scroll bar
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command = my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    #Configure the canvas
    my_canvas.configure(yscrollcommand = my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all") ))

    #Create Another frame inside the canvas
    second_frame = Frame(my_canvas)

    #add frame
    my_canvas.create_window((0,0), window = second_frame, anchor = "nw")


    for thing in range(100):
        Button(second_frame, text = f'Button{thing} Yo!' ).grid(row=thing, column=0, pady=10,padx=10 )

    Button(second_frame, text = f'Avengers' ,font=('Bold',12), fg='red', bd=0,underline=True,
                         command=logout).grid(row=thing, column=0, pady=10,padx=10 )

    #login_btn = tk.Button(second_frame, text='Login', font=('Bold',12),
     #                       bg= '#158aff', fg='white', command=printMessage)
    #slogin_btn.place(x=50, y=220, width=150) 

    my_label = Label(second_frame, text="its friday").grid(row=3, column=2)


ScrollWindow()
root.mainloop()
