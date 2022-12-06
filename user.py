import numpy as np
class User():
    def __init__(self):
        self.password = ""
        self.email = ""
        self.address = ""
        self.name = ""
        self.pnumber = ""
        self.type = ""
        self.MovieList = np.empty((0,2),str)
    
    def loaduser(self,em,pa):
        with open('UserDatabase.txt') as f:
            for line in f:
                data = line.split(",")
                # print(data)
                # print(len(data))
                if data[0] == em and data[1] == pa:
                    self.email = data[0]
                    self.password = data[1]
                    self.name = data[2]
                    self.address = data[3]
                    self.pnumber = data[4]
                    self.type = data[5]
                    Movieamount = int((len(data)-7)/2)
                    for i in range(Movieamount):
                        temp = [data[6+(i*2)],data[7+(i*2)]]
                        self.MovieList = np.append(self.MovieList,np.array([temp]),0)
                    return True
                elif data[0] == em:
                    print("INCORRECT PASSWORD!")
                    return False
            print("USER NOT FOUND!")
            return False    

    def update(self):
        print("updated user database")
        newdata = ','.join([self.email,self.password,self.name,self.address,self.pnumber,self.type])
        newdata = newdata + ','
        row , col = self.MovieList.shape

        for i in range(row):
            newdata = newdata + self.MovieList[i][0] + ','+ self.MovieList[i][1] + ','
        f = open('UserDatabase.txt','r')
        filedata = f.read()
        f.seek(0)
        Lines = f.readlines()

        for line in Lines:
            data = line.split(",")
            if data[0] == self.email:
                olddata = line.rstrip()
        f.close()

        newdata = filedata.replace(olddata,newdata)

        f = open('UserDatabase.txt','w')
        f.write(newdata)
        f.close()

###########################  Getters ############################
    def getname(self):
        return(self.name)

    def getpassword(self):
        return(self.password)    
    
    def getaddress(self):
        return(self.address)

    def getemail(self):
        return(self.email)
    
    def getpnumber(self):
        return(self.pnumber)

    def gettype(self):
        return(self.type)
    
    def getMovieTicket(self):
        return(self.MovieList)

######################### Setter ##########################       
    def setName(self, newname):
        self.name = newname
        self.update()
        return True

    def setPassword(self, newpass):
        self.password=newpass
        self.update()
        return True

    def setAddress(self, newadd):
        self.address=newadd
        self.update()
        return True

    def setPhone(self, newphone):
        self.pnumber=newphone  
        self.update()
        return True

    def setMovie(self,moviename,num):
        row , col = self.MovieList.shape
        for i in range(row):
            if self.MovieList[i][0] == moviename:
                temp = int(self.MovieList[i][1])
                temp += num
                self.MovieList[i][1] = str(temp)
                self.update()
                return True
        temp = [moviename,num]
        self.MovieList = np.append(self.MovieList,np.array([temp]),0)
        self.update()
        return True
        



# Test = User()
# Test.loaduser("real","PASS")
# print(Test.getMovieTicket())
# Test.setMovie("Thor3",3)
# print(Test.getMovieTicket())
# Test.setName("REAL JIBIN")
# print(Test.getname())
# Test.setName("Jibin")
# print(Test.getname())