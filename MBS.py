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
import random
import numpy as np
import moviesClass

Accounts= ["Admin", "AdminPass"] 
root = tk.Tk()
#              Xaxis, Yaxis
root.geometry('1000x600')
root.title('Movie Booking system')

global startvar

fileName= "UserDatabase.txt"
tempName ='admin'
state = '' 
movieState=0
Customer = user.User()
UsersName=''

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
                if(Accounts[x]==stringThing):
                    return 1;
    return 0;        
    file.close()

def verifyAccount(username, password):
  size = len(Accounts)
  for x in range(size):
    if (x % 2 ==0):
      if(Accounts[x]==username):
        if(Accounts[x+1]==password):
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

def Purchase_Box(num, nameThing):
    message_frame = tk.Frame(root, relief=tk.SOLID, highlightthickness=2,highlightbackground='gray')

    close_btn = tk.Button(message_frame, text='X', font=('Bold',12), bd=0,
                            command=lambda: message_frame.destroy())
    close_btn.pack(side=tk.TOP, anchor=tk.E)

    rando = random.randint(1000,9999)
    message_lb = tk.Label(message_frame, text = f'You have purchased\n {num} tickets\n Confirmation#\n {rando}',
     font=('Bold',15) )
    message_lb.pack(pady=20)
    global numMoviesSold
    numMoviesSold=numMoviesSold + int(num)
    Customer.setMovie(nameThing,num)
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

    def forward_viewStats():
        display_frame.destroy()
        global state
        state = 'viewStats'
        mainMenu()       

    display_frame = tk.Frame(root)

    #messages
    message = tk.Label(display_frame, text= f'Admin\nHome Page', font=('Bold',12))
    message.place(x=100,y=0)

    sumary = tk.Label(display_frame, text= "Here you do admin stuff,\nYeah", font=('Bold',12))
    sumary.place(x=100,y=50)
   
    #Buttons
    AddRemove_btn = tk.Button(display_frame, text='Add/Remove Movies',command=forward_Add_Remove,
                         font=('Bold',12),bg= 'green', fg='white', )
    AddRemove_btn.place(x=100, y=150, width=150)   
    Edit_btn = tk.Button(display_frame, text='Add Details',command=forward_Edit, font=('Bold',12),
                            bg= 'green', fg='white', )
    Edit_btn.place(x=100, y=250, width=150)  

    view_stats_btn = tk.Button(display_frame, text='View stats', font=('Bold',12),
                            bg= 'green', fg='white', command=forward_viewStats)
    view_stats_btn.place(x=100, y=350, width=150)   

    logout_btn = tk.Button(display_frame, text='Logout',command=logout, font=('Bold',12),
                            bg= 'red', fg='black', )
    logout_btn.place(x=100, y=450, width=150)  

    display_frame.pack(pady=10)
    display_frame.pack_propagate(False)
    display_frame.configure(height=600, width=1000)
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
    def verifyAddCurrent():
        if search_movie.get() != '':
            if( moviesClass.findMovie(search_movie.get()) !=None ):
                message_box(msg='Movie already Exists!')
            else:
                moviesClass.addMovie(moviesClass.movie(search_movie.get(),
                director_entry.get(), genre_entry.get(), price_entry.get(),time_entry.get(),'0','0',1 ))

                moviesClass.updateMovie()
                moviesClass.movieObjects.clear()
                moviesClass.loadMovies()
                message_box(msg=f'{ search_movie.get() } \nhas been Added')  
        else:
            message_box(msg='Entry Empty')
    def verifyAddUpcomming():
        if search_movie.get() != '':
            if( moviesClass.findMovie(search_movie.get()) !=None ):
                message_box(msg='Movie already Exists!')
            else:
                moviesClass.addMovie(moviesClass.movie(search_movie.get(),
                director_entry.get(), genre_entry.get(), price_entry.get(),time_entry.get(),'0','0',0 ))

                moviesClass.updateMovie()
                moviesClass.movieObjects.clear()
                moviesClass.loadMovies()
                message_box(msg=f'{ search_movie.get() } \nhas been Added')  
        else:
            message_box(msg='Entry Empty')
    def verifyRemove():
        if search_movie.get() != '':
            if(moviesClass.findMovie(search_movie.get()) !=None ):
                moviesClass.deleteMovie(search_movie.get())
                #movies.remove(search_movie.get())
                moviesClass.updateMovie()
                moviesClass.movieObjects.clear()
                moviesClass.loadMovies()
                message_box(msg=f'{search_movie.get()}\nhas been Removed')  
            else:
                message_box(msg='No such movie exists')  
        else:
            message_box(msg='Entry Empty')           
        
    display_frame = tk.Frame(root)

    #messages
    message = tk.Label(display_frame, text= f'Add or Remove movie', font=('Bold',12))
    message.place(x=100,y=0)
 
    search_movie_lb =tk.Label(display_frame, text='Enter Movie to\n add or remove', font=('Bold',12))
    search_movie_lb.place(x=100, y=50) 
    #text entry box
    search_movie = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    search_movie.place(x=350, y=50, width=250, height=30) 

    genre_lb =tk.Label(display_frame, text='Genre', font=('Bold',12))
    genre_lb.place(x=100, y=100) 
    genre_entry = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    genre_entry.place(x=350, y=100, width=250, height=30) 

    director_lb =tk.Label(display_frame, text='Director', font=('Bold',12))
    director_lb.place(x=100, y=150) 
    director_entry = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    director_entry.place(x=350, y=150, width=250, height=30)

    time_lb =tk.Label(display_frame, text='Time', font=('Bold',12))
    time_lb.place(x=100, y=200) 
    time_entry = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    time_entry.place(x=350, y=200, width=250, height=30)

    price_lb =tk.Label(display_frame, text='Price', font=('Bold',12))
    price_lb.place(x=100, y=250) 
    price_entry = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    price_entry.place(x=350, y=250, width=250, height=30)

    #actual Add button

    Add_btn = tk.Button(display_frame, text='Add Current',command=verifyAddCurrent, font=('Bold',12),
                            bg= 'green', fg='black', )
    Add_btn.place(x=100, y=300, width=150)

    Add_btn = tk.Button(display_frame, text='Add Upcomming',command=verifyAddUpcomming, font=('Bold',12),
                            bg= 'green', fg='black', )
    Add_btn.place(x=300, y=300, width=150)  

    #actual Remove button
    Remove_btn = tk.Button(display_frame, text='Remove',command=verifyRemove, font=('Bold',12),
                            bg= 'green', fg='black', )
    Remove_btn.place(x=100, y=350, width=150)  

    #Dashboard button
    dash_btn = tk.Button(display_frame, text='Go To Dashboard',command=forward_Admin_dashboard_page, font=('Bold',12),
                            bg= 'yellow', fg='black', )
    dash_btn.place(x=100, y=400, width=150)  

    display_frame.pack(pady=10)
    display_frame.pack_propagate(False)
    display_frame.configure(height=600, width=1000)

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
    
    global movies
    for thing in range( moviesClass.totalMovies() ):
        Button(second_frame, text = f'{thing} {moviesClass.movieObjects[thing].getName() }',
        command=lambda number=thing: forward_EditMovie(number) ).grid(row=thing, column=0, pady=10,padx=10 )

    Button(second_frame, text = f'Go to Dashboard',bg= '#158aff', fg='black',font= ('Bold'),
                command= Forward_AdminDashboard).grid(row=thing+1, column=0, pady=10,padx=10 )

def EditMovie(movie):
    def forward_admin_dashboard_page():
        display_frame.destroy()
        global state
        state = 'AdminDashboard'
        mainMenu()
    def forward_self():
        display_frame.destroy()
        global movieState
        state = 'EditMovie'
        mainMenu()
    def updateInfo():
        moviesClass.movieObjects[movie].setTime( str(time_entry.get()) )
        moviesClass.movieObjects[movie].setPrice(str(price_entry.get()))
        moviesClass.updateMovie()
        moviesClass.movieObjects.clear()
        moviesClass.loadMovies()
        forward_self()
        
    display_frame = tk.Frame(root)
    #messages
    message = tk.Label(display_frame, text= f'Movie: {moviesClass.movieObjects[movie].getName()}', font=('Bold',12))
    message.place(x=100,y=0)

    time = tk.Label(display_frame, text= f"Movie Time: {moviesClass.movieObjects[movie].getTime()}", font=('Bold',12))
    time.place(x=100,y=100)

    time_entry = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    time_entry.place(x=400, y=100, width=250, height=30) 

    price = tk.Label(display_frame, text= f"Price : {moviesClass.movieObjects[movie].getPrice()}", font=('Bold',12))
    price.place(x=100,y=200)

    price_entry = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    price_entry.place(x=400, y=200, width=250, height=30) 

    #Buttons
    return_to_dashboard = tk.Button(display_frame, text='Return to Dashboard', font=('Bold',12),
                            bg= '#158aff', fg='white', command=forward_admin_dashboard_page)
    return_to_dashboard.place(x=100, y=400, width=150)  

    update_info_btn = tk.Button(display_frame, text='Update Info', font=('Bold',12),
                            bg= 'green', fg='white', command=updateInfo)
    update_info_btn.place(x=100, y=300, width=150)   

    display_frame.pack(pady=10)
    display_frame.pack_propagate(False)

    display_frame.configure(height=600 , width=1000)


def viewStats():
    def Forward_AdminDashboard():
        display_frame.destroy()
        global state
        state = 'AdminDashboard'
        mainMenu()
    def forward_self():
        display_frame.destroy()
        global movieState
        state = 'displayInfo'
        mainMenu()

    display_frame = tk.Frame(root)
    #Labels
    email_lb = tk.Label(display_frame, text= f'On this page, you can view stats ',
     font=('Bold',12))
    email_lb.place(x=100,y=0)

    email_lb = tk.Label(display_frame, text= f'Welcome: {Customer.getemail()} ', font=('Bold',12))
    email_lb.place(x=100,y=100)
    
    tempName=Customer.getname()
    global numMoviesSold
    name_lb = tk.Label(display_frame, text= f"Number of tickets\npurchased today: {numMoviesSold}",
     font=('Bold',12))
    name_lb.place(x=100,y=150)
   
    dash_btn = tk.Button(display_frame, text='Go To Dashboard',command=Forward_AdminDashboard, font=('Bold',12),
                            bg= 'blue', fg='white', )
    dash_btn.place(x=100, y=400, width=150)  

    display_frame.pack(pady=10)
    display_frame.pack_propagate(False)
    display_frame.configure(height=600, width=1000)

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
    for thing in range( moviesClass.totalMovies() ):
        if(moviesClass.movieObjects[thing].getState() == "1"):    
            Button(second_frame, text = f' {moviesClass.movieObjects[thing].getName() }',
            command=lambda number=thing: display(number) ).grid(row=thing, column=0, pady=10,padx=10 )

    Button(second_frame, text = f'Go to Dashboard',bg= '#158aff', fg='black',font= ('Bold'),
                command= forward_dashboard_page).grid(row=thing+1, column=0, pady=10,padx=10 )

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
        state = 'displayUpcommingMovie'
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
    
    for thing in range( moviesClass.totalMovies() ):
        if(moviesClass.movieObjects[thing].getState() == "0"):    
            Button(second_frame, text = f' {moviesClass.movieObjects[thing].getName() }',
            command=lambda number=thing: display(number) ).grid(row=thing, column=0, pady=10,padx=10 )

    Button(second_frame, text = f'Go to Dashboard',bg= '#158aff', fg='black',font= ('Bold'),
                command= forward_dashboard_page).grid(row=thing+1, column=0, pady=10,padx=10 )

def displayUpcommingMovie(movie):
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


    #messages moviesClass.movieObjects[movie].getTime()
    message = tk.Label(display_frame, text= f'Movie: {moviesClass.movieObjects[movie].getName()}', font=('Bold',12))
    message.place(x=100,y=0)

    genre_label = tk.Label(display_frame, text= f"Genre: {moviesClass.movieObjects[movie].getGenre()}", font=('Bold',12))
    genre_label.place(x=100,y=50)

    director_label = tk.Label(display_frame, text= f"Director: {moviesClass.movieObjects[movie].getDirector()}", font=('Bold',12))
    director_label.place(x=100,y=100)

    director_label = tk.Label(display_frame, text= f"Price: {moviesClass.movieObjects[movie].getPrice()}", font=('Bold',12))
    director_label.place(x=100,y=150)

    director_label = tk.Label(display_frame, text= f"Time: {moviesClass.movieObjects[movie].getTime()}", font=('Bold',12))
    director_label.place(x=100,y=200)
    #Buttons
    return_to_dashboard = tk.Button(display_frame, text='Return to Dashboard', font=('Bold',12),
                            bg= '#158aff', fg='white', command=forward_dashboard_page)
    return_to_dashboard.place(x=100, y=300, width=150)  

    display_frame.pack(pady=10)
    display_frame.pack_propagate(False)

    display_frame.configure(height=600 , width=1000)


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
    def forward_upcomming_display_page(movieNum):
        display_frame.destroy()
        global movieState
        movieState=movieNum
        global state
        state = 'displayUpcommingMovie'
        mainMenu()
        
    def verify():
       if search_movie.get() != '':
        if(moviesClass.findMovie(search_movie.get()) != None      ):
            if( moviesClass.findState(str(search_movie.get())) == "1"):
                forward_display_page(  moviesClass.findMovie(search_movie.get()) )
            else:
                forward_upcomming_display_page(moviesClass.findMovie(search_movie.get()))
        else:
            message_box(msg='No such movie exists')    
        
    display_frame = tk.Frame(root)

    search_movie_lb =tk.Label(display_frame, text='Search movie       \n\nEnter movie name below:', font=('Bold',12))
    search_movie_lb.place(x=100, y=140) 

    #Movie entry
    search_movie = tk.Entry(display_frame, font=('Bold',15), bd=0, highlightcolor='#158aff',
                        highlightthickness=2, highlightbackground='gray')
    search_movie.place(x=100, y=200, width=250, height=30) 

    #Search for movie button
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
        
        if(name_entry.get()!='' ):
            Customer.setName(str(name_entry.get()))

        if(address_entry.get()!='' ):
            Customer.setAddress(str(address_entry.get()))

        if(phone_entry.get()!='' ):
            Customer.setPhone(str(phone_entry.get()))
        
        if(password_entry.get()!='' ):
            Customer.setPassword(str(password_entry.get()))    
        forward_self()    # this ensures that the list updates in real time

    #Display stuff
    display_frame = tk.Frame(root)

    email_lb = tk.Label(display_frame, text= f'Welcome: {Customer.getemail()} ', font=('Bold',12))
    email_lb.place(x=100,y=0)

    email_lb = tk.Label(display_frame, text= f'On this page,\n\nYou can view and edit your info ',
     font=('Bold',12))
    email_lb.place(x=100,y=50)

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

    dash_btn = tk.Button(display_frame, text='Go To Dashboard',command=forward_dashboard_page, font=('Bold',12),
                            bg= 'blue', fg='white', )
    dash_btn.place(x=100, y=400, width=150)  

    display_frame.pack(pady=10)
    display_frame.pack_propagate(False)
    display_frame.configure(height=600, width=1000)

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

    email_lb = tk.Label(display_frame, text= f'Welcome:'+ Customer.getname(), font=('Bold',12))
    email_lb.place(x=100,y=100) 

    row, col = (Customer.getMovieTicket()).shape
    # print(row)
    ticket_lb = []
    for i in range(row):
        ticket_lb.append(tk.Label(display_frame,text= (Customer.getMovieTicket())[i][0] + ' : ' + (Customer.getMovieTicket())[i][1], font=('Bold',12)))
        ticket_lb[i].place(x=100,y=100+(20*(i+1)))
    ticket_lb.clear()
    # print(ticket_lb)
    #Dashboard button
    dash_btn = tk.Button(display_frame, text='Go To Dashboard',command=forward_dashboard_page, font=('Bold',12),
                            bg= 'blue', fg='white', )
    dash_btn.place(x=100, y=400, width=150)  

    display_frame.pack(pady=10)
    display_frame.pack_propagate(False)
    display_frame.configure(height=600, width=1000)

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
    def forward_self():
        display_frame.destroy()
        global movieState
        state = 'Display'
        mainMenu()

    def upVote():
        upVotes = int(moviesClass.movieObjects[movie].getUpvotes()) + 1
        totalVotes = int(moviesClass.movieObjects[movie].getTotalVotes()) + 1
        moviesClass.movieObjects[movie].setUpvotes(str(upVotes))
        moviesClass.movieObjects[movie].setTotalVotes(str(totalVotes))
        moviesClass.updateMovie()
        forward_self()

    def downVote():   
        totalVotes = int(moviesClass.movieObjects[movie].getTotalVotes()) + 1
        moviesClass.movieObjects[movie].setTotalVotes(str(totalVotes))
        moviesClass.updateMovie()
        forward_self()

    display_frame = tk.Frame(root)

    #messages
    message = tk.Label(display_frame, text= f'Movie: {moviesClass.movieObjects[movie].getName()}', font=('Bold',12))
    message.place(x=100,y=0)

    genre_label = tk.Label(display_frame, text= f"Genre: {moviesClass.movieObjects[movie].getGenre()}", font=('Bold',12))
    genre_label.place(x=100,y=50)

    director_label = tk.Label(display_frame, text= f"Director: {moviesClass.movieObjects[movie].getDirector()}", font=('Bold',12))
    director_label.place(x=100,y=100)

    director_label = tk.Label(display_frame, text= f"Price: {moviesClass.movieObjects[movie].getPrice()}", font=('Bold',12))
    director_label.place(x=100,y=150)

    director_label = tk.Label(display_frame, text= f"Time: {moviesClass.movieObjects[movie].getTime()}", font=('Bold',12))
    director_label.place(x=100,y=200)

    rating_label = tk.Label(display_frame, text= f"Rating: {moviesClass.movieObjects[movie].getUpvotes()}/{moviesClass.movieObjects[movie].getTotalVotes()}", font=('Bold',12))
    rating_label.place(x=350,y=0)
    up_rating_btn = tk.Button(display_frame, text='Up Vote', font=('Bold',12),
                            bg= '#158aff', fg='white', command=upVote )
    up_rating_btn.place(x=350, y=50, width=150)  
    down_rating_btn = tk.Button(display_frame, text='Down Vote', font=('Bold',12),
                            bg= '#158aff', fg='white', command=downVote )
    down_rating_btn.place(x=350, y=100, width=150) 


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

def purchaseTickets(CurrentMovie):
    def forward_Dashboard():
        display_frame.destroy()
        global state
        state = 'Dashboard'
        mainMenu()
       #Purchase_Box
    def make_purchase():
        #Purchase_Box( purchase_entry.get()  )  
        if int(purchase_entry.get()) <=10:
            if int(purchase_entry.get()) > 0:
                if(formatCheck.creditCardCheck(credit_entry.get())):
                    Purchase_Box( int(purchase_entry.get()), moviesClass.movieObjects[CurrentMovie].getName()  ) 
                else:
                    message_box(msg= "Invalid Credit\nCard number")     

            else:
                message_box(msg= "Invalid amount")  
        else:     
            message_box(msg= "You can only\nbook 10 tickets/nat a time")
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

    credit_lb = tk.Label(display_frame, text= "Enter 16 digit Credit card #", font=('Bold',12))
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
                            if response:
                                username.delete(0, tk.END)
                                password.delete(0, tk.END)
                                email.delete(0,tk.END)
                                address.delete(0,tk.END)
                                pnumber.delete(0,tk.END)
                                updateList()
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
    file.close()
    pass

########################### Main Loop ###############################################
updateList()
login_page()
moviesClass.loadMovies()
moviesClass.printMovie()

#state block

def mainMenu():
    if state == 'Login':
        login_page()
    elif state == "Register":
        register_page() 

    ####################Admin###################    
    elif state == "AdminDashboard":
        AdminDashboard()
    elif state == "AdminAddRemove":
        AddRemoveMovie()
    elif state == "EditMovieList":
        EditMovieList()        
    elif state == "EditMovie":
        EditMovie(movieState) 
    elif state == "viewStats":
        viewStats()             
    ####################Regular People#################   
    
    #################### Dashboard ####################
    elif state == "Dashboard":
        dashboard() 
    elif state == "CurrentMovies":
        currentMovies()
    elif state == "UpcomingMovies":
        upcomingMovies()
    elif state == "displayUpcommingMovie":  #Child function of Upcomming movies
        displayUpcommingMovie(movieState)
    elif state == "SearchMovie":            
        searchMovie()  
    elif state == "displayInfo":            #Child function Current Movies and SearchMovie
        displayInfo()   
    elif state =="showPurchases":           # Child function of displayInfo
        showPurchases()    
     #################### Child functions ####################    
    elif state == "Display":
        displayMovie(movieState)
    elif state == "PurchaseTickets":
        purchaseTickets(movieState)
    else:
        print("Goodbye")
mainMenu()

root.mainloop()