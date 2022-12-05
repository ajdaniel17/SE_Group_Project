#https://www.youtube.com/watch?v=yuuDJ3-EdNQ&ab_channel=Codemy.com
#https://www.youtube.com/watch?v=zU6ElvwaZIs&ab_channel=TkinterHub

import tkinter as tk
import os
import sqlite3 
from tkinter import *
#from PIL import ImageTk,IMAGE
from tkinter import ttk
import user
import formatCheck

Accounts= ["Admin", "AdminPass"] 
root = tk.Tk()
#              Xaxis, Yaxis
root.geometry('1000x600')
root.title('Tkinter hub')

global startvar

fileName= "UserDatabase.txt"
tempName ='admin'
state = '' 
movieState=0
Customer = user.User()
UsersName=''

#########################
movies= ["Avengers","Iron Man","Thor","Star Wars","Harry Potter"]
numMoviesSold=0





#################################   File stuff    #########################################################
def updateList():
    global Accounts
    Accounts= ["Admin", "AdminPass"] 
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

def verifyAccount(username, password):
  size = len(Accounts)
  for x in range(size):
    if (x % 2 ==0):
      if(Accounts[x]==username):
        if(Accounts[x+1]==password):
          print("Found string")
          return 1
        else:  
          return 0

def register_account(email, password,username,address,pnumber):
    try:
        with open (fileName, 'a')as file:
            file.write("\n")
            file.write(email)
            file.write(",")
            file.write(password)
            file.write(",")
            file.write(username)
            file.write(",")
            file.write(address)
            file.write(",")
            file.write(pnumber)
            file.write(",User,")
            file.close()
            pass
        return True
    except Exception as error:    
        return False

def Purchase_Box(num):
    message_frame = tk.Frame(root, relief=tk.SOLID, highlightthickness=2,highlightbackground='gray')

    close_btn = tk.Button(message_frame, text='X', font=('Bold',12), bd=0,
                            command=lambda: message_frame.destroy())
    close_btn.pack(side=tk.TOP, anchor=tk.E)

    message_lb = tk.Label(message_frame, text = f'You have purchased\n {num} tickets', font=('Bold',15) )
    message_lb.pack(pady=20)
    global numMoviesSold
    numMoviesSold=numMoviesSold + int(num)
    print(f"Total Tickets sold is: {numMoviesSold}")

    message_frame.place(x=40,y=100, width=230, height=180)


#################################   Message Box    ###################################################

def message_box(msg):
    message_frame = tk.Frame(root, relief=tk.SOLID, highlightthickness=2,highlightbackground='gray')

    close_btn = tk.Button(message_frame, text='X', font=('Bold',12), bd=0,
                            command=lambda: message_frame.destroy())
    close_btn.pack(side=tk.TOP, anchor=tk.E)

    message_lb = tk.Label(message_frame, text = msg, font=('Bold',15) )
    message_lb.pack(pady=20)

    message_frame.place(x=40,y=100, width=230, height=180)

def displayQR():
    #my_img = ImageTk.PhotoImage(Image.open("qr.png"))

    message_frame = tk.Frame(root, relief=tk.SOLID, highlightthickness=2,highlightbackground='gray')

    close_btn = tk.Button(message_frame, text='X', font=('Bold',12), bd=0,
                            command=lambda: message_frame.destroy())
    close_btn.pack(side=tk.TOP, anchor=tk.E)

    message_lb = tk.Label(message_frame, text = msg, font=('Bold',15) )
    message_lb.pack(pady=20)

    message_frame.place(x=40,y=100, width=230, height=180)






################################ Admin ###########################
def AdminDashboard():
    print("Welcome admin")
    def logout():
        display_frame.destroy()
        global state
        state = 'Login'
        mainMenu()

    def forward_Add_Remove(): 
        display_frame.destroy()
        global state
        state = 'AdminAddRemove'
        mainMenu()

    def forward_Edit(): 
        display_frame.destroy()
        global state
        state = 'EditMovieList'
        mainMenu()

    """    
    def forward_upcomming_page():
        display_frame.destroy()
        global state
        state = 'UpcomingMovies'
        mainMenu()
    def forward_current_page():
        display_frame.destroy()
        global state
        state = 'CurrentMovies'
        mainMenu()    
    def forward_search_page():
        display_frame.destroy()
        global state
        state = 'SearchMovie'
        mainMenu()   
    """    

    display_frame = tk.Frame(root)

    #messages
    message = tk.Label(display_frame, text= f'Admin\nHome Page', font=('Bold',12))
    message.place(x=100,y=0)

    summaryText="Here you do admin stuff,\nYeah"
    sumary = tk.Label(display_frame, text= summaryText, font=('Bold',12))
    sumary.place(x=100,y=50)
   
    #Buttons
    AddRemove_btn = tk.Button(display_frame, text='Add/Remove Movies',command=forward_Add_Remove,
                         font=('Bold',12),bg= 'green', fg='white', )
    AddRemove_btn.place(x=100, y=150, width=150)   
    Edit_btn = tk.Button(display_frame, text='Add Details',command=forward_Edit, font=('Bold',12),
                            bg= 'green', fg='white', )
    Edit_btn.place(x=100, y=250, width=150)   
    search_btn = tk.Button(display_frame, text='Search Movie', font=('Bold',12),
                            bg= 'green', fg='white', command=forward_Edit)
    search_btn.place(x=100, y=350, width=150)   

    logout_btn = tk.Button(display_frame, text='Logout',command=logout, font=('Bold',12),
                            bg= 'red', fg='black', )
    logout_btn.place(x=100, y=450, width=150)  

    display_frame.pack(pady=10)
    display_frame.pack_propagate(False)
    display_frame.configure(height=600, width=1000)
    print(Customer.getname())

def AddRemoveMovie():
    def forward_Admin_dashboard_page():
        display_frame.destroy()
        global state
        state = 'AdminDashboard'
        mainMenu()
    def forward_display_page(movieNum):
        display_frame.destroy()
        global movieState
        movieState=movieNum
        global state
        state = 'Display'
        mainMenu()
    def verifyAdd():
        if search_movie.get() != '':
            if(search_movie.get() in movies):
                message_box(msg='Movie already Exists!')
            else:
                movies.append(search_movie.get() )
                message_box(msg=f'{ search_movie.get() } \nhas been Added')  
        else:
            message_box(msg='Entry Empty')

    def verifyRemove():
        if search_movie.get() != '':
            if(search_movie.get() in movies):
                movies.remove(search_movie.get())
                message_box(msg=f'{search_movie.get()}\nhas been Removed')  
            else:
                message_box(msg='No such movie exists')  
        else:
            message_box(msg='Entry Empty')           
        
    display_frame = tk.Frame(root)

    #messages
    message = tk.Label(display_frame, text= f'Add or Remove movie', font=('Bold',12))
    message.place(x=100,y=0)

    #Buttons
    #search_btn = tk.Button(display_frame, text='Search Movie', font=('Bold',12),
     #                       bg= 'green', fg='white', )
    #search_btn.place(x=0, y=300, width=150)  
    # Display text message 
    search_movie_lb =tk.Label(display_frame, text='Enter Movie to add or remove', font=('Bold',12))
    search_movie_lb.place(x=100, y=50) 

    #text entry box
    search_movie = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    search_movie.place(x=100, y=100, width=250, height=30) 

    #actual Add button
    Add_btn = tk.Button(display_frame, text='Add',command=verifyAdd, font=('Bold',12),
                            bg= 'green', fg='black', )
    Add_btn.place(x=100, y=200, width=150)  

    #actual Remove button
    Remove_btn = tk.Button(display_frame, text='Remove',command=verifyRemove, font=('Bold',12),
                            bg= 'green', fg='black', )
    Remove_btn.place(x=100, y=300, width=150)  

    #Dashboard button
    dash_btn = tk.Button(display_frame, text='Go To Dashboard',command=forward_Admin_dashboard_page, font=('Bold',12),
                            bg= 'yellow', fg='black', )
    dash_btn.place(x=100, y=400, width=150)  

    display_frame.pack(pady=10)
    display_frame.pack_propagate(False)
    display_frame.configure(height=600, width=1000)
    print(Customer.getname())        

def EditMovieList():
    def Forward_AdminDashboard():
        main_frame.destroy()
        second_frame.destroy()
        my_canvas.destroy()
        global state
        state = 'AdminDashboard'
        mainMenu()

    def forward_EditMovie(movieNum):
        main_frame.destroy()
        second_frame.destroy()
        my_canvas.destroy()
        
        global movieState
        movieState=movieNum
        global state
        state = 'EditMovie'
        mainMenu()

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
    #
    message = tk.Label(second_frame, text= f'Edit the following Movies', 
    font=('Bold',12)).grid(row=0, column=2, pady=10,padx=10 )
    #message.place(x=120,y=0)
    
    global movies
    for thing in range( len(movies) ):
        Button(second_frame, text = f'{thing} {movies[thing] }',command=lambda number=thing: forward_EditMovie(number) ).grid(row=thing, column=0, pady=10,padx=10 )

    Button(second_frame, text = f'Go to Dashboard',bg= '#158aff', fg='black',font= ('Bold'),
                command= Forward_AdminDashboard).grid(row=thing+1, column=0, pady=10,padx=10 )
    print(Customer.getname())

def EditMovie(movie):
    def forward_dashboard_page():
        display_frame.destroy()
        global state
        state = 'AdminDashboard'
        mainMenu()
    def forward_purchase_page():
        display_frame.destroy()
        global state
        state = 'PurchaseTickets'
        mainMenu()
    display_frame = tk.Frame(root)

    #messages
    message = tk.Label(display_frame, text= f'Movie: {movies[movie]}', font=('Bold',12))
    message.place(x=100,y=0)

    time = tk.Label(display_frame, text= "Movie Time", font=('Bold',12))
    time.place(x=100,y=100)

    time_entry = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    time_entry.place(x=200, y=100, width=250, height=30) 

    price = tk.Label(display_frame, text= "Price", font=('Bold',12))
    price.place(x=100,y=200)

    price_entry = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    price_entry.place(x=200, y=200, width=250, height=30) 



    #Buttons
    return_to_dashboard = tk.Button(display_frame, text='Return to Dashboard', font=('Bold',12),
                            bg= '#158aff', fg='white', command=forward_dashboard_page)
    return_to_dashboard.place(x=100, y=400, width=150)  

    update_info_btn = tk.Button(display_frame, text='Update Info', font=('Bold',12),
                            bg= 'green', fg='white', command=forward_purchase_page)
    update_info_btn.place(x=100, y=300, width=150)   
    #Time 
    #Price


    display_frame.pack(pady=10)
    display_frame.pack_propagate(False)

    display_frame.configure(height=600 , width=1000)
    print(Customer.getname())


################################## Main User #########################
def dashboard():
    def logout():
        display_frame.destroy()
        global state
        state = 'Login'
        mainMenu()       
    def forward_upcomming_page():
        display_frame.destroy()
        global state
        state = 'UpcomingMovies'
        mainMenu()
    def forward_current_page():
        display_frame.destroy()
        global state
        state = 'CurrentMovies'
        mainMenu()    
    def forward_search_page():
        display_frame.destroy()
        global state
        state = 'SearchMovie'
        mainMenu()   
    def forward_display_info_page():
        display_frame.destroy()
        global state
        state = 'displayInfo'
        mainMenu()
    def forward_show_Purchases_page():
        display_frame.destroy()
        global state
        state = 'showPurchases'
        mainMenu()
        
    display_frame = tk.Frame(root)

    #messages
    message = tk.Label(display_frame, text= f'Home Page', font=('Bold',12))
    message.place(x=100,y=0)

    summaryText="Here you can go to the Current Movies page, \n Upcoming Movies page,\n or Search Movies page"
    sumary = tk.Label(display_frame, text= summaryText, font=('Bold',12))
    sumary.place(x=100,y=50)

    #Buttons
    current_btn = tk.Button(display_frame, text='Current Movies',command=forward_current_page, font=('Bold',12),
                            bg= 'green', fg='white', )
    current_btn.place(x=100, y=150, width=150)   
    upcomming_btn = tk.Button(display_frame, text='Upcoming movies',command=forward_upcomming_page, font=('Bold',12),
                            bg= 'green', fg='white', )
    upcomming_btn.place(x=100, y=200, width=150)   
    search_btn = tk.Button(display_frame, text='Search Movie', font=('Bold',12),
                            bg= 'green', fg='white', command=forward_search_page)
    search_btn.place(x=100, y=250, width=150)   
    View_Info_btn = tk.Button(display_frame, text='Account Info',command=forward_display_info_page,
                 font=('Bold',12), bg= 'green', fg='white', )
    View_Info_btn.place(x=100, y=300, width=150)  

    View_Purchases_btn = tk.Button(display_frame, text='Your Purchases',command=forward_show_Purchases_page,
                 font=('Bold',12), bg= 'green', fg='white', )
    View_Purchases_btn.place(x=100, y=350, width=150)

    logout_btn = tk.Button(display_frame, text='Logout',command=logout, font=('Bold',12),
                            bg= 'red', fg='black', )
    logout_btn.place(x=100, y=450, width=150)  

    display_frame.pack(pady=10)
    display_frame.pack_propagate(False)
    display_frame.configure(height=600, width=1000)
    print(Customer.getname())

def currentMovies():
    def forward_dashboard_page():
        main_frame.destroy()
        second_frame.destroy()
        my_canvas.destroy()

        global state
        state = 'Dashboard'
        mainMenu()

    def display(movieNum):
        main_frame.destroy()
        second_frame.destroy()
        my_canvas.destroy()

        global movieState
        movieState=movieNum
        global state
        state = 'Display'
        mainMenu()

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
    #
    message = tk.Label(second_frame, text= f'Current \nMovies', 
    font=('Bold',12)).grid(row=0, column=2, pady=10,padx=10 )
    #message.place(x=120,y=0)
    
    global movies
    for thing in range( len(movies) ):
        Button(second_frame, text = f'{thing} {movies[thing] }',
        command=lambda number=thing: display(number) ).grid(row=thing, column=0, pady=10,padx=10 )

    Button(second_frame, text = f'Go to Dashboard',bg= '#158aff', fg='black',font= ('Bold'),
                command= forward_dashboard_page).grid(row=thing+1, column=0, pady=10,padx=10 )
    print(Customer.getname())

def upcomingMovies():
    def forward_dashboard_page():
        main_frame.destroy()
        second_frame.destroy()
        my_canvas.destroy()

        global state
        state = 'Dashboard'
        mainMenu()

    def display(movieNum):
        main_frame.destroy()
        second_frame.destroy()
        my_canvas.destroy()
        
        global movieState
        movieState=movieNum
        global state
        state = 'Display'
        mainMenu()

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
    #
    message = tk.Label(second_frame, text= f'Upcoming\nMovies', 
    font=('Bold',12)).grid(row=0, column=2, pady=10,padx=10 )
    #message.place(x=120,y=0)
    
    global movies
    for thing in range( len(movies) ):
        Button(second_frame, text = f'{thing} {movies[thing] }',command=lambda number=thing: display(number) ).grid(row=thing, column=0, pady=10,padx=10 )

    Button(second_frame, text = f'Go to Dashboard',bg= '#158aff', fg='black',font= ('Bold'),
                command= forward_dashboard_page).grid(row=thing+1, column=0, pady=10,padx=10 )
    print(Customer.getname())

def searchMovie():
    def forward_dashboard_page():
        display_frame.destroy()
        global state
        state = 'Dashboard'
        mainMenu()
    def forward_display_page(movieNum):
        display_frame.destroy()
        global movieState
        movieState=movieNum
        global state
        state = 'Display'
        mainMenu()
    def verify():
       if search_movie.get() != '':
        if(search_movie.get() in movies):
            forward_display_page( movies.index(search_movie.get())  )
            print("Forwarding display page")
        else:
            message_box(msg='No such movie exists')    
        
    display_frame = tk.Frame(root)

    #messages
    message = tk.Label(display_frame, text= f'Purchase Tickets', font=('Bold',12))
    message.place(x=100,y=0)

    summaryText="Here you may purchase tickets"
    sumary = tk.Label(display_frame, text= summaryText, font=('Bold',12))
    sumary.place(x=100,y=50)

    #Buttons
    #search_btn = tk.Button(display_frame, text='Search Movie', font=('Bold',12),
     #                       bg= 'green', fg='white', )
    #search_btn.place(x=0, y=300, width=150)  
    # Display text message 
    search_movie_lb =tk.Label(display_frame, text='Search movie', font=('Bold',12))
    search_movie_lb.place(x=100, y=150) 

    #text entry box
    search_movie = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    search_movie.place(x=100, y=200, width=250, height=30) 

    #actual search button
    Search_btn = tk.Button(display_frame, text='Search',command=verify, font=('Bold',12),
                            bg= 'green', fg='black', )
    Search_btn.place(x=100, y=300, width=150)  

    #Dashboard button
    dash_btn = tk.Button(display_frame, text='Go To Dashboard',command=forward_dashboard_page, font=('Bold',12),
                            bg= 'blue', fg='white', )
    dash_btn.place(x=100, y=400, width=150)  

    display_frame.pack(pady=10)
    display_frame.pack_propagate(False)
    display_frame.configure(height=600, width=1000)
    print(Customer.getname())        

def displayInfo():
    def forward_dashboard_page():
        display_frame.destroy()
        global state
        state = 'Dashboard'
        mainMenu()
    def forward_display_page(movieNum):
        display_frame.destroy()
        global movieState
        movieState=movieNum
        global state
        state = 'Display'
        mainMenu()
    def forward_self():
        display_frame.destroy()
        global movieState
        state = 'displayInfo'
        mainMenu()

    def update_List():
        if(email_entry.get()!='' ):
            Customer.setEmail(str(email_entry.get()))
        
        if(name_entry.get()!='' ):
            Customer.setName(str(name_entry.get()))

        if(address_entry.get()!='' ):
            Customer.setAddress(str(address_entry.get()))

        if(phone_entry.get()!='' ):
            Customer.setPhone(str(phone_entry.get()))

        if(password_entry.get()!='' ):
            Customer.setPassword(str(password_entry.get()))    
        forward_self()    # this ensures that the list updates in real time



    display_frame = tk.Frame(root)

    #Labels
    email_lb = tk.Label(display_frame, text= f'On this page,\nYou can view and edit your info ',
     font=('Bold',12))
    email_lb.place(x=100,y=0)

    email_lb = tk.Label(display_frame, text= f'Welcome: {Customer.getemail()} ', font=('Bold',12))
    email_lb.place(x=100,y=100)
    
    email_entry = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    email_entry.place(x=400, y=100, width=250, height=30) 

    tempName=Customer.getname()
    name_lb = tk.Label(display_frame, text= f"Name: {Customer.getname()}", font=('Bold',12))
    name_lb.place(x=100,y=150)
    name_entry = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    name_entry.place(x=400, y=150, width=250, height=30) 

    address_lb =tk.Label(display_frame, text=f'Adress: {Customer.getaddress()}', font=('Bold',12))
    address_lb.place(x=100, y=200)
    address_entry = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    address_entry.place(x=400, y=200, width=250, height=30) 

    phone_lb =tk.Label(display_frame, text= f'Phone #: {Customer.getpnumber()}', font=('Bold',12))
    phone_lb.place(x=100, y=250) 
    phone_entry = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    phone_entry.place(x=400, y=250, width=250, height=30) 

    password_lb =tk.Label(display_frame, text= f'Password: {Customer.getpassword()}', font=('Bold',12))
    password_lb.place(x=100, y=300) 
    password_entry = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    password_entry.place(x=400, y=300, width=250, height=30) 


    dash_btn = tk.Button(display_frame, text='Save Changes',command=update_List, font=('Bold',12),
                            bg= 'green', fg='black', )
    dash_btn.place(x=100, y=350, width=150)

    #Dashboard button
    dash_btn = tk.Button(display_frame, text='Go To Dashboard',command=forward_dashboard_page, font=('Bold',12),
                            bg= 'blue', fg='white', )
    dash_btn.place(x=100, y=400, width=150)  

    display_frame.pack(pady=10)
    display_frame.pack_propagate(False)
    display_frame.configure(height=600, width=1000)
    print(Customer.getname())            

def showPurchases():
    def forward_dashboard_page():
        display_frame.destroy()
        global state
        state = 'Dashboard'
        mainMenu()
    def forward_display_page(movieNum):
        display_frame.destroy()
        global movieState
        movieState=movieNum
        global state
        state = 'Display'
        mainMenu()

    display_frame = tk.Frame(root)

    #Labels
    email_lb = tk.Label(display_frame, text= f'On this page,\nYou can view your purchases ',
     font=('Bold',12))
    email_lb.place(x=100,y=0)

    email_lb = tk.Label(display_frame, text= f'Welcome: EmailUsername ', font=('Bold',12))
    email_lb.place(x=100,y=100) 

    #Dashboard button
    dash_btn = tk.Button(display_frame, text='Go To Dashboard',command=forward_dashboard_page, font=('Bold',12),
                            bg= 'blue', fg='white', )
    dash_btn.place(x=100, y=400, width=150)  

    display_frame.pack(pady=10)
    display_frame.pack_propagate(False)
    display_frame.configure(height=600, width=1000)
    print(Customer.getname())           

def displayMovie(movie):
    def forward_dashboard_page():
        display_frame.destroy()
        global state
        state = 'Dashboard'
        mainMenu()
    def forward_purchase_page():
        display_frame.destroy()
        global state
        state = 'PurchaseTickets'
        mainMenu()
    display_frame = tk.Frame(root)

    #messages
    message = tk.Label(display_frame, text= f'Movie: {movies[movie]}', font=('Bold',12))
    message.place(x=100,y=0)

    summaryText="the man went into the world and looked for somethign \n grand but could not find it"
    sumary = tk.Label(display_frame, text= summaryText, font=('Bold',12))
    sumary.place(x=100,y=100)

    #Buttons
    return_to_dashboard = tk.Button(display_frame, text='Return to Dashboard', font=('Bold',12),
                            bg= '#158aff', fg='white', command=forward_dashboard_page)
    return_to_dashboard.place(x=100, y=300, width=150)  

    purchase_ticket = tk.Button(display_frame, text='Purchase Ticket', font=('Bold',12),
                            bg= 'green', fg='white', command=forward_purchase_page)
    purchase_ticket.place(x=100, y=400, width=150)   


    display_frame.pack(pady=10)
    display_frame.pack_propagate(False)

    display_frame.configure(height=600 , width=1000)
    print(Customer.getname())

def purchaseTickets():
    def forward_Dashboard():
        display_frame.destroy()
        global state
        state = 'Dashboard'
        mainMenu()
       #Purchase_Box
    def make_purchase():
        #Purchase_Box( purchase_entry.get()  )  
        if int(purchase_entry.get()) <=6:
            if int(purchase_entry.get()) > 0:
                if(formatCheck.creditCardCheck(credit_entry.get())):
                    Purchase_Box( int(purchase_entry.get())   ) 
                else:
                    message_box(msg= "Invalid Credit\nCard number")     

            else:
                message_box(msg= "Invalid amount")  
                print("Invalid Amount")   
        else:     
            message_box(msg= "You can only\nbook 6 tickets/nat a time")
            print("only purchase 6")
    display_frame = tk.Frame( )

    #messages
    message = tk.Label(display_frame, text= f'Purchase Tickets', font=('Bold',12))
    message.place(x=100,y=0)

    summaryText="Enter Ammount to Purchase"
    sumary = tk.Label(display_frame, text= summaryText, font=('Bold',12))
    sumary.place(x=100,y=100)

    purchase_entry = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    purchase_entry.place(x=100, y=150, width=250, height=30) 

    credit_lb = tk.Label(display_frame, text= "Enter Credit card", font=('Bold',12))
    credit_lb.place(x=100,y=200)
    credit_entry = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    credit_entry.place(x=100, y=250, width=250, height=30) 

    purchase_btn = tk.Button(display_frame, text='Add',command=make_purchase, font=('Bold',12),
                            bg= 'green', fg='black', )
    purchase_btn.place(x=100, y=300, width=150)
       
    logout_btn = tk.Button(display_frame, text='Go To Dashboard',command=forward_Dashboard, font=('Bold',12),
                            bg= 'blue', fg='white', )
    logout_btn.place(x=100, y=400, width=150)  

    display_frame.pack(pady=10)
    display_frame.pack_propagate(False)
    display_frame.configure(height=600, width=1000)
    print(Customer.getname())        






##########################################Account Stuff below#########################################################
def login_page():
    def forward_register_page():
        #register_page()
        global state
        state = 'Register'
        login_frame.destroy()
        mainMenu()

    def forward_dashboard():
        global state
        state = 'Dashboard'
        login_frame.destroy()
        mainMenu()

    def forward_admin_dashboard():
        global state
        state = 'AdminDashboard'
        login_frame.destroy()
        mainMenu()

    def verify():
        if username.get() !='':
            if password.get() !='':
                if(Customer.loaduser(username.get(), password.get())):
                    print("Sucessfully Logged in")
                    login_frame.destroy()
                    if(Customer.gettype() == "Admin"):
                        forward_admin_dashboard()
                    else:
                        #global UsersName
                        #UsersName = username.get()
                        forward_dashboard()
                else:
                    message_box(msg = "Password Inncorrect or User does not exist!")
            else:
                message_box(msg= "Password is required")
        else:
            message_box(msg= "Username is required")        

    login_frame = tk.Frame(root)

    username_lb = tk.Label(login_frame, text='Enter Email', font=('Bold',12))
    username_lb.place(x=160,y=20)

    username = tk.Entry(login_frame, font=('Bold', 15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    username.place(x=150, y=60, width=250, height=30)

    password_lb =tk.Label(login_frame, text='Enter Password', font=('Bold',12))
    password_lb.place(x=160, y=120) 

    password = tk.Entry(login_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    password.place(x=150, y=160, width=250, height=30)                    

    login_btn = tk.Button(login_frame, text='Login', font=('Bold',12),
                            bg= '#158aff', fg='white', command=verify)
    login_btn.place(x=150, y=220, width=150)   

    register_page_link = tk.Button(login_frame, text='Register',
                        font=('Bold',12), fg='#158aff', bd=0,underline=True, command=forward_register_page)                     
    register_page_link.place(x=190, y=260) 

    login_frame.pack(pady=10)
    login_frame.pack_propagate(False)

    #login_frame.configure(height=400, width=250, bg='gray')
    login_frame.configure(height=600, width=1000)

def register_page():
    def forward_login_page():
        register_frame.destroy()
        #login_page()
        global state
        state = 'Login'

        mainMenu()
    def verify():
        if username.get() != '':    #if username not empty and password not empty
            if password.get() != '':
                if formatCheck.emailCheck(email.get()) and formatCheck.phoneNumberCheck(pnumber.get()):
                    if repeat_password.get() == password.get():
                        # send a 0 for passwords, 
                        if searchList(0, username.get()) ==0 :
                            response = register_account(email=email.get(), password= password.get(),username = username.get(),address=address.get(),pnumber=pnumber.get())
                            print("running register")
                            if response:
                                username.delete(0, tk.END)
                                password.delete(0, tk.END)
                                email.delete(0,tk.END)
                                address.delete(0,tk.END)
                                pnumber.delete(0,tk.END)
                                updateList()
                                print(Accounts)
                                repeat_password.delete(0, tk.END)
                                message_box(msg='Account Created') 
                        else:
                            message_box(msg='Username \n already exists')     
                    else:
                        message_box(msg='Error: Passwords dont match')   
                else:
                        message_box(msg='Either Phone number \nor email format is invalid')     
            else:
                message_box(msg='Error: Password empty')        
        else:
            message_box(msg='Error: Username empty')
    ###        
    register_frame =tk.Frame(root)

    #enter email
    email_lb = tk.Label(register_frame, text='Enter Email', font=('Bold',12))
    email_lb.place(x=160,y=20)

    email = tk.Entry(register_frame, font=('Bold', 15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    email.place(x=150, y=60, width=250, height=30)
    #enter name
    username_lb = tk.Label(register_frame, text='Enter Username', font=('Bold',12))
    username_lb.place(x=160,y=100)

    username = tk.Entry(register_frame, font=('Bold', 15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    username.place(x=150, y=140, width=250, height=30)
    #enter address
    address_lb = tk.Label(register_frame, text='Enter Address', font=('Bold',12))
    address_lb.place(x=160,y=180)

    address = tk.Entry(register_frame, font=('Bold', 15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    address.place(x=150, y=220, width=250, height=30)
    #enter phone number
    pnumber_lb = tk.Label(register_frame, text='Enter Phone Number', font=('Bold',12))
    pnumber_lb.place(x=160,y=260)

    pnumber = tk.Entry(register_frame, font=('Bold', 15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    pnumber.place(x=150, y=300, width=250, height=30)
    #enter password
    password_lb =tk.Label(register_frame, text='Enter Password', font=('Bold',12))
    password_lb.place(x=160, y=340) 

    password = tk.Entry(register_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    password.place(x=150, y=380, width=250, height=30)     
    #repeat password
    repeat_password_lb =tk.Label(register_frame, text='Repeat Password', font=('Bold',12))
    repeat_password_lb.place(x=160, y=420) 

    repeat_password = tk.Entry(register_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    repeat_password.place(x=150, y=460, width=250, height=30)     

    register_btn = tk.Button(register_frame, text='Register', font=('Bold',12),
                            bg= '#158aff', fg='white',command =verify)
    register_btn.place(x=150, y=500, width=150)

    login_page_link = tk.Button(register_frame, text= 'Login', fg='#158aff',underline=True,
                                font=('Bold', 12), bd=0, command=forward_login_page)

    login_page_link.place(x=200, y=540 )                            

    register_frame.pack()
    register_frame.pack_propagate(False)
    register_frame.configure(height= 600, width = 1000)

with open ("UserDatabase.txt", 'r')as file:
    var=file.read()
    print(var)
    file.close()
    pass




########################### Main Loop ###############################################
updateList()
login_page()

#state block

def mainMenu():
    if state == 'Login':
        print("login State")
        login_page()
    elif state == "Register":
        print("Register State")
        register_page() 

    ####################Admin###################    
    elif state == "AdminDashboard":
        print("Admin Dashboard State")
        AdminDashboard()
    elif state == "AdminAddRemove":
        print("Admin Add/Remove State")
        AddRemoveMovie()
    elif state == "EditMovieList":
        print("Admin Edit List State")
        EditMovieList()        
    elif state == "EditMovie":
        print("Admin Edit State")
        EditMovie(movieState)         
    ####################Regular People#################   
    
    #################### Dashboard ####################
    elif state == "Dashboard":
        print("Dashboard State")
        dashboard() 
    elif state == "CurrentMovies":
        print("Current movie State")
        currentMovies()
    elif state == "UpcomingMovies":
        print("Upcoming movie State")
        upcomingMovies()
    elif state == "SearchMovie":
        print("Search movie State")  
        searchMovie()  
    elif state == "displayInfo":
        print("displayInfo state") 
        displayInfo()   
    elif state =="showPurchases":
        print("Showing purchases state") 
        showPurchases()    
     #################### Child functions ####################    
    elif state == "Display":
        print("Display movie State")
        displayMovie(movieState)
    elif state == "PurchaseTickets":
        print("Purchase movie State")
        purchaseTickets()
    else:
        print("Please choose correct answer")
mainMenu()


root.mainloop()