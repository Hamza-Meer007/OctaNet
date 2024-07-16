from time import sleep
from os import system , name 
from tkinter import *
new = 1234
bal = 0.0
trans = []
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

def display():
    print('\t------------------------')
    print('\t --> Welcome to ATM <--')
    print('\t------------------------')
def pin():
    global new,bal,trans
    
    try:
        p = int(input('Enter your for digit pin number: '))
        if p == new:
            print('Welcome Sir')
            
            while True:
                options()
                opt = int(input('Enter your choice: '))
                match opt:
                    case 1:
                        print(f'Your Current Balance is {bal} ')
                        # clear()
                    case 2:
                        amount = float(input('Enter amount: '))
                        if amount > bal:
                            print(f'Invalid....Your Current Balance is {bal}')
                        else:
                            print('Cash Withdrawl Successfully....')
                            bal = bal - amount
                            trans.append(f'Withdrawal: {amount}') 
                            print(f'Your Current Balance is {bal}')
                        # clear()
                    case 3:
                        amount = float(input('Enter amount: '))
                        if amount > 0:
                            bal = bal + amount
                            print(f'Your Current Balance is {bal}')
                            trans.append(f'Deposit: {amount}') 
                        else:
                            print('Invalid amount')
                        # clear()
                    case 4:
                        for transaction in trans:
                            print(transaction)
                    case 5:
                        n = int(input('Enter your current pin: '))
                        if n == new :
                            new_pin = int(input('Enter New Pin: '))
                            con_pin = int(input('Confirm New Pin: '))
                            if new_pin == con_pin:
                                print('Pin updated successfully')
                                new =new_pin
                            else:
                                print('Double check your pin')
                        else:
                            print('inavlid pin')
                        # clear()
                    case 0:
                        print('Exiting......')
                        sleep(2)
                        # clear()
                        break
        else:
            print('Invalid Pin Number')
                    
    except :
        print('Invalid Number')
        

def options():
    print('''
        Press 1: For Balance Inquiry
        Press 2: For Cash Withdrawl
        Press 3: For Cash Deposit
        Press 4: For Transaction History
        Press 5: For Change Pin
        Press 0: For Exit
        ''')
    

display()
pin()


# root = Tk()
# root.title('Atm created by Hamza Meer')
# root.geometry('959x600+150+60')
# root.resizable(0,0)

# root.mainloop()
        





