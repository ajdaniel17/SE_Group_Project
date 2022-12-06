class movie():    
    def __init__(self, name = "" , director = "", genre = "", price = "", time = [], upvotes = "", ratingTotal = "", state = 0):
        self.name = name
        self.director = director
        self.genre = genre
        self.price = price

        mat = []
        timeData = time.split(", ")
        for n in range(len(timeData)):
            mat.append(timeData[n])
        self.time = mat

        self.upvotes = upvotes
        self.ratingTotal = ratingTotal
        self.state = state

    
    # Getters
    def getName(self):
        return(self.name)

    def getDirector(self):
        return(self.director)

    def getGenre(self):
        return(self.genre)

    def getPrice(self):
        return(self.price)

    def getTime(self):
        mat = []
        for n in range(len(self.time)):
            mat.append(self.time[n])
        return(mat)
    
    def getUpvotes(self):
        return(self.upvotes)

    def getTotalVotes(self):
        return(self.ratingTotal)

    def getState(self):
        return(self.state)

    # Setters
    def setName(self, inputName):
        self.name = inputName
    
    def setDirector(self, inputDirector):
        self.director = inputDirector
    
    def setGenre(self, inputGenre):
        self.genre = inputGenre
    
    def setPrice(self, inputPrice):
        self.price = inputPrice
    
    def setTime(self, inputTime):
        self.time = inputTime
    
    def setUpvotes(self, inputUpvotes):
        self.time = inputUpvotes

    def setTotalVotes(self, inputTotalVotes):
        self.time = inputTotalVotes

    def setState(self, inputState):
        self.time = inputState

##############################################################################
### Movie manipulation functions ###

# Global variable conataining movie data
movieObjects = []

# More specific getters
def findDirector(title):
    pos = findMovie(title)
    if pos == None:
        return
    return movieObjects[pos].getDirector()

def findGenre(title):
    pos = findMovie(title)
    if pos == None:
        return
    return movieObjects[pos].getGenre()

def findPrice(title):
    pos = findMovie(title)
    if pos == None:
        return
    return movieObjects[pos].getPrice()

def findTime(title):
    pos = findMovie(title)
    if pos == None:
        return
    return movieObjects[pos].getTime()

def findUpvotes(title):
    pos = findMovie(title)
    if pos == None:
        return
    return movieObjects[pos].getUpvotes()

def findTotalVotes(title):
    pos = findMovie(title)
    if pos == None:
        return
    return movieObjects[pos].getTotalVotes()

def findState(title):
    pos = findMovie(title)
    if pos == None:
        return
    return movieObjects[pos].getState()

# More specific setters
def replaceDirector(title, director):
    pos = findMovie(title)
    if pos == None:
        return
    movieObjects[pos].setDirector(director)

def replaceGenre(title, genre):
    pos = findMovie(title)
    if pos == None:
        return
    movieObjects[pos].setGenre(genre)

def replacePrice(title, price):
    pos = findMovie(title)
    if pos == None:
        return
    movieObjects[pos].setPrice(price)

def replaceTime(title, time):
    pos = findMovie(title)
    if pos == None:
        return
    movieObjects[pos].setTime(time)

def replaceUpvotes(title, upvotes):
    pos = findMovie(title)
    if pos == None:
        return
    movieObjects[pos].setUpvotes(upvotes)

def replaceTotalVotes(title, totalVotes):
    pos = findMovie(title)
    if pos == None:
        return
    movieObjects[pos].setTotalVotes(totalVotes)

def replaceState(title, state):
    pos = findMovie(title)
    if pos == None:
        return
    movieObjects[pos].setState(state)

# Reads data from MovieDatabase.txt and puts it into movieList
def loadMovies():
    global movieObjects
    with open("MovieDatabase.txt") as inputFile:
        next(inputFile) #skip first line
        for line in inputFile:
            if line != "\n":
                data = line.split("; ")
                mat = []
                for n in data: # removes newlines
                    mat.append(n.replace("\n", ""))
                movieObjects.append(movie(mat[0], mat[1], mat[2], mat[3], mat[4], mat[5], mat[6], mat[7]))
    inputFile.close

# Prints everything in a specified movie
def movieDetails(title):
    pos = findMovie(title)
    mat = movieObjects[pos].getTime()
    print("\n------")
    print("Details for " + title + ":")
    print("Name: " + movieObjects[pos].getName() + 
        "\nDirector: " + movieObjects[pos].getDirector() + 
        "\nGenre: " + movieObjects[pos].getGenre() + 
        "\nPrice: " + movieObjects[pos].getPrice() + 
        "\nTimes: ", end = "")
    for i in range(len(mat)):
        print(str(mat[i]), end="") 
        if i < len(mat) - 1:
            print(", ", end = "")
    print("\nRating: " + str(movieObjects[pos].getUpvotes()) + "/" 
        + str(movieObjects[pos].getTotalVotes()), end ="")
    if movieObjects[pos].getState:
        print("\nState: Current", end = "")
    else:
        print("\nState: Upcomming", end = "")
    print("\n------")
    
# Add a movie into the movie list
def addMovie(obj):
    global movieObjects
    name = findMovie(obj.getName())
    if name == None:
        movieObjects.append(obj)
    else:
        print(str(obj.getName()) + " already exists!")

# Delete movie from movie list
def deleteMovie(title):
    global movieObjects
    title = title.lower()
    for n in range(len(movieObjects)):
        if title == (movieObjects[n].getName()).lower():
            del movieObjects[n]
            return

# Find movie position in movie list
def findMovie(title):
    global movieObjects
    title = title.lower()
    for n in range(len(movieObjects)):
        if title == (movieObjects[n].getName()).lower():
            return n
    # movie not found
    print(str(title) + " was not found")
    return None

# Print all information in movie object
def printMovie():
    global movieObjects
    print("\n\n***Movies***")
    for n in range(len(movieObjects)):
        mat = movieObjects[n].getTime()
        print("Name: " + movieObjects[n].getName() + 
        "\nDirector: " + movieObjects[n].getDirector() + 
        "\nGenre: " + movieObjects[n].getGenre() + 
        "\nPrice: " + movieObjects[n].getPrice() + 
        "\nTimes: ", end = "")
        for i in range(len(mat)):
            print(str(mat[i]), end="") 
            if i < len(mat) - 1:
                print(", ", end = "")
        print("\nRating: " + str(movieObjects[n].getUpvotes()) + "/" 
            + str(movieObjects[n].getTotalVotes()), end ="")
        if movieObjects[n].getState:
            print("\nState: Current", end = "")
        else:
            print("\nState: Upcomming", end = "")
        print("\n------")

# Writes to output file
def updateMovie():
    global movieObjects
    outputFile = open("MovieDatabase.txt", "w")
    outputFile.write("(Movie) ; (Director) ; (Genre) ; (Price) ; (Times) ; (Upvotes) ; (Total Votes) ; (State [upcomming/current])\n")
    for n in range(len(movieObjects)):
        mat = movieObjects[n].getTime()
        outputFile.write(movieObjects[n].getName() + "; " 
        + movieObjects[n].getDirector() + "; " 
        + movieObjects[n].getGenre() + "; " 
        + movieObjects[n].getPrice() + "; ")
        for i in range(len(mat)):
            outputFile.write(mat[i])
            if i < len(mat) - 1:
                outputFile.write(", ")
        outputFile.write("; " + str(movieObjects[n].getUpvotes()) + "; "
        + str(movieObjects[n].getTotalVotes()) + "; "
        + str(movieObjects[n].getState()))
        outputFile.write("\n")
    outputFile.close()
    
'''
def main():
    loadMovies()
    printMovie()
    #replaceDirector("avengers2", "Joss Wheden")
    #replaceGenre("avengers2", "Comedy")
    #replacePrice("avengers2", "15")
    #replaceTime("avengers2", ["12:30", "12:45"])
    #print(findMovie("Avengers4"))
    #deleteMovie("Avengers4")
    #movieDetails("avengers")
    #print(findDirector("avengers"))
    #print(findGenre("avengers"))
    #print(findPrice("avengers"))
    #print(findTime("avengers"))
    #mat = movieObjects[0].getTime()
    #print(mat)
    #print(str(movieObjects[0].getTime()))
    #updateMovie()
    #addMovie(movie("Avengers5", "Joss Wheden", "Super Hero", "19", "12:00, 3:00, 6:00, 9:00"))
    #printMovie()
    updateMovie()


if __name__ == "__main__":
    main()
'''