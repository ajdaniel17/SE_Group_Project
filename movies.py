class movie():    
    def __init__(self, name = "" , director = "", genre = "", price = "", time = []):
        self.name = name
        self.director = director
        self.genre = genre
        self.price = price

        mat = []
        timeData = time.split(", ")
        for n in range(len(timeData)):
            mat.append(timeData[n])
            
        self.time = mat
    
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

##############################################################################
### Movie manipulation functions ###

# Global variable conataining movie data
movieObjects = []

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
                movieObjects.append(movie(mat[0], mat[1], mat[2], mat[3], mat[4]))
    inputFile.close

# Add a movie into the movie list
def addMovie(obj):
    global movieObjects
    movieObjects.append(obj)

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
        print("\n------")

# Writes to output file
def updateMovie():
    global movieObjects
    outputFile = open("MovieDatabase.txt", "w")
    outputFile.write("(Movie) ; (Director) ; (Genre) ; (Price) ; (Times)\n")
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
        outputFile.write("\n")
    outputFile.close()
    
'''
def main():
    loadMovies()
    printMovie()
    print(findMovie("Avengers4"))
    deleteMovie("Avengers4")
    #mat = movieObjects[0].getTime()
    #print(mat)
    #print(str(movieObjects[0].getTime()))
    #updateMovie()
    #addMovie(movie("Avengers4", "Joss Wheden4", "Super Hero4", "15", "12:00, 3:00, 6:00, 9:00"))
    #printMovie()
    updateMovie()


if __name__ == "__main__":
    main()
'''
