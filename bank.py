
from random import randint

class Bank:
    def __init__(self):
        self.name=input("Enter name: ")
        self.phone=int(input("Enter Phone number: "))
        self.acc_num=randint(100000,9000000)
        self.balance=0

    def show_info(self):
        print(f"Account number = {self.acc_num}")
        print(f"Full name = {self.name} ")
        print(f"Balance = {self.balance}\n")


    
    def check(self):
        print( f"Current balance is {self.balance}\n")

    def deposit(self):
        amount=int(input("Enter amount you want to deposit: "))
        self.balance+=amount
        print("Deposit Done ✔ \n")
    

    def withdraw(self):
        amount=int(input("Enter amount you want to withdraw: "))
        if self.balance<amount:
            print("insufficient balance 😒\n")
        else:
            
            self.balance-=amount
            print("Withdrawl Done ✔ \n")

bank=[]

def acc_exist(ac_no: int):
    global bank
    for obj in bank:
        if obj.acc_num==ac_no:
            return obj
    return None



while True:
    print("1. Create account.")
    print("2.Check account details")
    print("3.Deposit Amount")
    print("4.Withdraw Amount")
    print("5.Transfer Amount")
    print("6.Delete Account")
    print("7.Exit \n")

    choice=int(input("Enter your Choice: "))

   
   # Creating Account
    if choice==1:
        obj=Bank()
        bank.append(obj)
       
   
   #Check accounts details
    elif choice==2:
        if len(bank)==0:
            print("No account created yet")
        else:
            for account in bank:
                account.show_info()
   
   
    # Deposit Money
    elif choice==3:
        if len(bank)==0:
            print("no accounts created yet")
        else:
            ac_no=int(input("Enter account number:"))
            for i in bank:
                if i.acc_num==ac_no:
                    i.deposit()
                    break
    
    
    #Withdrawl Money
    elif choice==4:
        if len(bank)==0:
            print("No account created yet")
        else:
            ac_no=int(input("Enter account number: "))
            for i in bank:
                if i.acc_num==ac_no:
                    i.withdraw()
                    break

    

    #Transfer Money
    elif choice==5:
        from_acc_no=int(input("Enter acc_number from" \
        " which U want to transfer: "))

        to_acc_num=int(input("Enter acc_number in " \
        " which U want to transfer: "))
        
        
        from_acc_obj=acc_exist(from_acc_no)
        to_acc_obj=acc_exist(to_acc_num)
        
        if from_acc_no!=None and to_acc_num!=None:

            transfer_money=int(input("Enter transfer amount: "))

            if from_acc_obj.balance<transfer_money:

                print("insuffucient Balance 😒\n")

            else:
                from_acc_obj.balance-=transfer_money
                to_acc_obj.balance+=transfer_money
          
        else:
            print("Account doesn't exists")

    #Delete Account
    elif choice==6:
            if len(bank)==0:
                print("No account created yet")
            else:
                ac_no=int(input("Enter account number: "))
                for i in bank:
                    if i.acc_num==ac_no:
                        bank.remove(i)
                        print("Account Deleted Successfully ✔ \n")
                        break
                    else:
                        print("Account doesn't exists")
                        break

    #Exit 
    elif choice==7:
        print("Thank you for using our services✨")
        break
    else:
        print("Invalid Command")
    