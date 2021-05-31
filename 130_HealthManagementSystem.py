'''HEALTH MANAGEMENT SYSTEM'''

import datetime
def get_dt_now():
    return datetime.datetime.now()

class HMS:
    def option(self, cname):
        self.cname = cname
        welcomeMsg = '''\n\t| Database of Health Management System |
Choose one option:-
\t\t1.  Show your Data
\t\t2.  Add Food Data
\t\t3.  Add Excercise Data
\t\t4.  Quit'''
        print(welcomeMsg)
        try:
            self.op = int(input("Enter either 1, 2 or 3: "))
            if self.op ==1:
                self.showDetails()
            elif self.op ==2:
                self.addDetails_eat()
            elif self.op ==3:
                self.addDetails_exc()
            elif self.op == 4:
                print("Exiting.....")
                exit()
            else:
                print("Enter only numbers from 1 to 4")
                self.option(self.cname)    
        except Exception as e:
            print("Make sure you enter just numbers.")
            self.option(self.cname)
    
    def showDetails(self):

        eat_file_name = "HMS/" + self.cname + "_eat.txt"
        exc_file_name = "HMS/" + self.cname + "_exc.txt"

        try:
            with open(exc_file_name, "r") as f:
                print(f"{self.cname} excercise related data\n{f.read()}\n")
        except:
            print("No excercise data exists!!")

        try:
            with open(eat_file_name, "r") as f:
                print(f"{self.cname} food related data\n{f.read()}\n")
        except:
            print("No eat data exists!!")

        self.option(self.cname)
        
    
    def addDetails_eat(self):

        eat_file_name = "HMS/" + self.cname + "_eat.txt"
        with open(eat_file_name, "a") as f:
            val = input("Enter what you ate below\n")
            f.write(f"[{str(get_dt_now())}] : {val}\n")
            print("Successfully entered in your log!!")

        self.option(self.cname)

            
    def addDetails_exc(self):
        exc_file_name = "HMS/" + self.cname + "_exc.txt"

        with open(exc_file_name, "a") as f:
            val = input("Enter what excercise you did\n")
            f.write(f"[{str(get_dt_now())}] : {val}\n")
            print("Successfully entered in your log!!")

        self.option(self.cname)


class Client:
    ct_name = ["Mannu", "Puru", "Pulkit"]
    
    def __init__(self):
        print('''\n~~~~~| Welcome to Health Management System |~~~~~
\t\tWelcome back!!''') 
    
    def inputClient(self):
        try:
            print("Our Clients:-")
            for i,j in enumerate(self.ct_name):
                print(f"\t\t{i+1}.  {j}")
            self.ct = int(input("Enter the client number from above options: "))
            if (self.ct <= len(self.ct_name) and self.ct>0):
                return self.ct_name[self.ct-1]
        except Exception as e:
            print("Please enter a valid input!!")
            exit()


if __name__ == "__main__":
    hms = HMS()
    clnt = Client()
    hms.option(clnt.inputClient())