class User():
    def __init__(self):
        self.password = ""
        self.email = ""
        self.address = ""
        self.name = ""
        self.pnumber = ""
    
    def loaduser(self,em,pa):
        with open('UserDatabase.txt') as f:
            for line in f:
                data = line.split(",")
                if data[0] == em and data[1] == pa:
                    self.email = data[0]
                    self.password = data[1]
                    self.name = data[2]
                    self.address = data[3]
                    self.pnumber = data[4]
                    return True
                elif data[0] == em:
                    print("INCORRECT PASSWORD!")
                    return False
            print("USER NOT FOUND!")
            return False    

    def getname(self):
        return(self.name)
    
    def getaddress(self):
        return(self.address)

    def getemail(self):
        return(self.email)
    
    def getpnumber(self):
        return(self.pnumber)

# Test = User()
# Test.loaduser("real@email.com","PASS")
# print(Test.getname())