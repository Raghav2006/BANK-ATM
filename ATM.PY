class ATM:
    def _init_(self,cardnumber,pin):
        self,cardnumber = cardnumber
        self.pin 


    def check_balance(self):
        print("your balance is 50000")

    def withdrawl(self,amount):
        new_amount =50000 - amount
        print("you have withdrawn amount "+str(amount) +". your remaining balence is +"str(new_amount))
    
def main ():
    card_number =input ("insert your card number:- ")
    pin_number  =input ("enter your pin number:- ")


    new_user = Atm(card_number ,pin_number)

     print("choose your activity")
     print("1.balance enquriy 2.withdrawl")
     activity = int(input("enter activity number:-"))

    if (activity == 1):
        new_user .check balance()
    elif (activity == 2):
         amount =  int(input("enter the number:-")) 
         new_user.withdrawl(amount)
    else:
         print("enter a valid number")

    if _name_=="_main_":
        main()