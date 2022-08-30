print ('\033[2;31;40m jaiii')

red = "\033[0;31;40m"
df ="\033[0;37;40m"
green="\033[0;32;40"
blue="\033[0;34;40"

pin=int(input("\033[0;34;40","enter the ATM pin:",df,sep=""))
if (pin!=2211):
    print(red,"you are pin is invalied",df,sep="")
elif(pin==2211):
        print("WElCOME TO INDIAN BANK ATM")
        options=int(input(blue" 1. Balance enqiery\n 2. withdraw amount\n 3. deposit amount\n Choose your option :",sep=""))
        a=6000
        if (options==1):
            print("your balance is :",a)
        elif (options==2):
            b=int(input("\033[0;34;40","Enter the amount :",sep=""))
            if a<b :
                print ("your Balance is insuffient")
            if a>b:
                print("Balance amount :",(a-b))
                print("Thank you")
        elif(options==3):
            c=int(input("\033[0;34;40","Enter the Deposit amount :",sep=""))
            print("your current balance",a+c)
            print("Thank you for visiting\n INDIAN BANK ATM\n         ☺")
        else:
            print("Invalid option")
