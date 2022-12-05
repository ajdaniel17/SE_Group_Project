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
    def setName(obj, namey):
        obj.name=namey
    def setEmail(obj, namey):
        obj.email=namey
    def setPassword(obj, namey):
        obj.password=namey
    def setAddress(obj, namey):
        obj.address=namey
    def setPhone(obj, namey):
        obj.pnumber=namey    



# Test = User()
# Test.loaduser("real@email.com","PASS")
# print(Test.getname())