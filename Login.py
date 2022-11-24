#<a href="https://www.flaticon.com/free-icons/show-password" title="show password icons">Show password icons created by Freepik - Flaticon</a>

import tkinter as tk
import os
import sqlite3 

Accounts= ["Admin", "AdminPassword"] 
root = tk.Tk()
root.geometry('300x400')
root.title('Tkinter hub')

global startvar

fileName= "passowrds.txt"




def updateList():
    #Accounts= ["Admin", "AdminPassword"] 
    with open(fileName,'r') as file:
        # reading each line    
        for line in file:
            # reading each word        
            for word in line.split():
                if(word=="Username" or word=="Password"):
                    continue
                else:  
                    Accounts.append(word)  
    file.close() 

#    varNum= 1 for password, 0 for username, stringThing is search name
def searchList(varNum, stringThing):
    with open(fileName, 'r') as file:
        size = len(Accounts)
        for x in range(size):
            if (x % 2 ==varNum):
                print(Accounts[x])
                if(Accounts[x]==stringThing):
                    print("Found string")
                    return 1;
    return 0;        
    file.close()





def message_box(msg):
    message_frame = tk.Frame(root, relief=tk.SOLID, highlightthickness=2,highlightbackground='gray')

    close_btn = tk.Button(message_frame, text='X', font=('Bold',12), bd=0,
                            command=lambda: message_frame.destroy())
    close_btn.pack(side=tk.TOP, anchor=tk.E)

    message_lb = tk.Label(message_frame, text = msg, font=('Bold',15) )
    message_lb.pack(pady=20)

    message_frame.place(x=40,y=100, width=230, height=180)

def register_account(username, password):
    try:
        with open (fileName, 'a')as file:
            file.write("Username ")
            file.write(username)
            file.write(" Password ")
            file.write(password)
            file.write("\n")
            file.close()
            pass
        return True
    except Exception as error:    
        return False
def login_page():
    def forward_register_page():
        login_frame.destroy()
        register_page()

    login_frame = tk.Frame(root)

    username_lb = tk.Label(login_frame, text='Enter Username', font=('Bold',12))
    username_lb.place(x=60,y=20)

    username = tk.Entry(login_frame, font=('Bold', 15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    username.place(x=50, y=60, width=150, height=30)

    password_lb =tk.Label(login_frame, text='Enter Password', font=('Bold',12))
    password_lb.place(x=60, y=120) 

    password = tk.Entry(login_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')

    password.place(x=50, y=160, width=150, height=30)                    

    login_btn = tk.Button(login_frame, text='Login', font=('Bold',12),
                            bg= '#158aff', fg='white')
    login_btn.place(x=50, y=220, width=150)   

    register_page_link = tk.Button(login_frame, text='Register',
                        font=('Bold',12), fg='#158aff', bd=0,underline=True, command=forward_register_page)                     
    register_page_link.place(x=90, y=260) 

    


    login_frame.pack(pady=10)
    login_frame.pack_propagate(False)

    #login_frame.configure(height=400, width=250, bg='gray')
    login_frame.configure(height=400, width=250)

def register_page():
    def forward_login_page():
        register_frame.destroy()
        login_page()
    def verify():
        if username.get() != '':    #if username not empty and password not empty
            if password.get() != '':
                if repeat_password.get() == password.get():
                    # send a 0 for passwords, 
                    if searchList(0, username.get()) ==0 :
                        response = register_account(username = username.get(), password= password.get())
                        print("running register")
                        if response:
                            username.delete(0, tk.END)
                            password.delete(0, tk.END)
                            repeat_password.delete(0, tk.END)
                            message_box(msg='Account Created') 
                    else:
                         message_box(msg='Username \n already exists')     
                else:
                    message_box(msg='Error: Passwords dont match')    
            else:
                message_box(msg='Error: Password empty')        
        else:
            message_box(msg='Error: Username empty')
    register_frame =tk.Frame(root)

    username_lb = tk.Label(register_frame, text='Enter Username', font=('Bold',12))
    username_lb.place(x=60,y=20)

    username = tk.Entry(register_frame, font=('Bold', 15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    username.place(x=50, y=60, width=150, height=30)

    password_lb =tk.Label(register_frame, text='Enter Password', font=('Bold',12))
    password_lb.place(x=60, y=115) 

    password = tk.Entry(register_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')

    password.place(x=50, y=155, width=150, height=30)     

    repeat_password_lb =tk.Label(register_frame, text='Repeat Password', font=('Bold',12))
    repeat_password_lb.place(x=60, y=210) 

    repeat_password = tk.Entry(register_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')

    repeat_password.place(x=50, y=250, width=150, height=30)     

    register_btn = tk.Button(register_frame, text='Register', font=('Bold',12),
                            bg= '#158aff', fg='white',command =verify)
    register_btn.place(x=50, y=315, width=150)

    login_page_link = tk.Button(register_frame, text= 'Login', fg='#158aff',underline=True,
                                font=('Bold', 12), bd=0, command=forward_login_page)

    login_page_link.place(x=100, y=350 )                            

    register_frame.pack()
    register_frame.pack_propagate(False)
    register_frame.configure(height= 400, width = 250)

with open ("UserDatabase.txt", 'r')as file:
    var=file.read()
    print(var)
    file.close()
    pass
updateList()
print(searchList(0, "tim"))
#updateList()

print(Accounts)          

#create_database()
login_page()
#register_page()
#message_box('Error')
root.mainloop()
