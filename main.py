import getpass
import string
import os

# creating a lists of users, their PINs and bank statements
users = ['dhruv', 'harshit', 'aryan']
pins = ['1234', '1234', '1234']
amounts = [1000, 2000, 3000]
count = 0
# while loop checks existance of the enterd username
while True:
    user = input('\nENTER USER NAME: ')
    if user in users:
        n = users.index(user)
        break
    else:
        print('----------------')
        print('****************')
        print('INVALID USERNAME')
        print('****************')
        print('----------------')

# comparing pin
while count < 3:
    print('------------------')
    print('******************')
    pin = str(getpass.getpass('PLEASE ENTER PIN: '))
    print('******************')
    print('------------------')
    if pin.isdigit():
        if pin == pins[n]:
            break
        else:
            count += 1
            print('-----------')
            print('***********')
            print('INVALID PIN')
            print('***********')
            print('-----------')
            print()
    else:
        print('------------------------')
        print('************************')
        print('PIN CONSISTS OF 4 DIGITS')
        print('************************')
        print('------------------------')
        count += 1
    
# in case of a valid pin- continuing, or exiting
if count == 3:
    print('-----------------------------------')
    print('***********************************')
    print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
    print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
    print('***********************************')
    print('-----------------------------------')
    exit()

print('-------------------------')
print('*************************')
print('LOGIN SUCCESFUL, CONTINUE')
print('*************************')
print('-------------------------')
print()
print('--------------------------')
print('**************************')    
print(str.capitalize(users[n]), 'welcome to ATM')
print('**************************')
print('----------ATM SYSTEM-----------')

menu_msg  = '''SELECT FROM FOLLOWING OPTIONS:
1. Statement
2. Withdraw
3. Lodgement
4. Change PIN
5. Quit
Enter your choice: '''

while True:
    print('-------------------------------')
    print('*******************************')
    response = input(menu_msg)
    print('*******************************')
    print('-------------------------------')
    if response == '1':
        print('---------------------------------------------')
        print('*********************************************')
        print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n],'RUPEES ON YOUR ACCOUNT.')
        print('*********************************************')
        print('---------------------------------------------')
    elif response == '2':
        print('---------------------------------------------')
        print('*********************************************')
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        print('*********************************************')
        print('---------------------------------------------')
        if cash_out%10 != 0:
            print('------------------------------------------------------')
            print('******************************************************')
            print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 RUPEES NOTES')
            print('******************************************************')
            print('------------------------------------------------------')
        elif cash_out > amounts[n]:
            print('-----------------------------')
            print('*****************************')
            print('YOU HAVE INSUFFICIENT BALANCE')
            print('*****************************')
            print('-----------------------------')
        else:
            amounts[n] = amounts[n] - cash_out
            print('-----------------------------------')
            print('***********************************')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
            print('***********************************')
            print('-----------------------------------')
    elif response == '3':
        print()
        print('---------------------------------------------')
        print('*********************************************')
        cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
        print('*********************************************')
        print('---------------------------------------------')
        print()
        if cash_in%10 != 0:
            print('----------------------------------------------------')
            print('****************************************************')
            print('AMOUNT YOU WANT TO LODGE MUST TO MATCH 10 RUPEES NOTES')
            print('****************************************************')
            print('----------------------------------------------------')
        else:
            amounts[n] = amounts[n] + cash_in
            print('----------------------------------------')
            print('****************************************')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
            print('****************************************')
            print('----------------------------------------')
    elif response == '4':
        print('-----------------------------')
        print('*****************************')
        new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
        print('*****************************')
        print('-----------------------------')
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
            print('------------------')
            print('******************')
            new_ppin = str(getpass.getpass('CONFIRM NEW PIN: '))
            print('*******************')
            print('-------------------')
            if new_ppin != new_pin:
                print('------------')
                print('************')
                print('PIN MISMATCH')
                print('************')
                print('------------')
            else:
                pins[n] = new_pin
                print('NEW PIN SAVED')
        else:
            print('-------------------------------------')
            print('*************************************')
            print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
            print('*************************************')
            print('-------------------------------------')
    elif response == '5':
        exit()
    else:
        print('------------------')
        print('******************')
        print('RESPONSE NOT VALID')
        print('******************')
        print('------------------')

