class User():
    def __init__(self):
        self.password = ""
        self.email = ""
        self.address = ""
        self.name = ""
        self.pnumber = ""
        self.type = ""
    
    def loaduser(self,em,pa):
        with open('UserDatabase.txt') as f:
            for line in f:
                data = line.split(",")
                print(data)
                if data[0] == em and data[1] == pa:
                    self.email = data[0]
                    self.password = data[1]
                    self.name = data[2]
                    self.address = data[3]
                    self.pnumber = data[4]
                    self.type = data[5]
                    return True
                elif data[0] == em:
                    print("INCORRECT PASSWORD!")
                    return False
            print("USER NOT FOUND!")
            return False    

    def update(self):
        print("updated user database")
        newdata = ','.join([self.email,self.password,self.name,self.address,self.pnumber,self.type])
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
######################### Setter ##########################       
    def setName(self, newname):
        self.name = newname
        self.update()
    def setPassword(self, newpass):
        self.password=newpass
        self.update()
    def setAddress(self, newadd):
        self.address=newadd
        self.update()
    def setPhone(self, newphone):
        self.pnumber=newphone  
        self.update()



# Test = User()
# Test.loaduser("real","PASS")
# print(Test.getname())
# Test.setName("REAL JIBIN")
# print(Test.getname())
# Test.setName("Jibin")
# print(Test.getname())