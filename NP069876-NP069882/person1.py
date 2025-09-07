import random 
from datetime import datetime
def introduction():
    print("Hello everyone!")
    print("In this group we are only two members.")
    print("A. Manish Yonjan (LEADER)")
    print("B. Nishan GC")
    print("****************************************************************")
introduction()
def main():   #Main function of this program
    while True:
        print("Select one of the following options.")
        print("----------------------------------------------------------------")
        print("1. Create Superuser account")
        print("2. Superuser Login")
        print("3. Staff Login")
        print("4. Customer Login")
        print("----------------------------------------------------------------")

        user_input = input("Enter number[1,2,3,4 or 'exit']: ")
        if user_input.lower() == "exit" :
            print("Thank you for choosing us!!")
            break
        print("----------------------------------------------------------------")
        try:
            n = int(user_input)
            if n == 1:
                create_superuser_account()
                print()
                Thank_you()
            elif n == 2:
                supersuer_login()
                print()
            elif n == 3:
                staff_login()
                print()
            
            elif n == 4:
                user_login()
                print()
                
            else:
                print("Please enter number 1, 2 , 3 or 4.")
        except:
            print("Invalid input. Please input a valid number.")
            
#FUNCTIONS SECTIONS
def create_superuser_account():
    print("Fill up the form.")
    gmail = input("Enter your gmail account: ")
    gmail_password = input("Enter your gmail password: ")
    contact_number = int(input("Enter your contact number: "))
 
    f = open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\superuser.txt","a")
    f.write(f"{gmail} {gmail_password} {contact_number}\n")
    f.close()
    
def supersuer_login():
    gmail_su = input("Enter supersuer email address: ")
    gmail_pass_su = input("Enter supersuer gmail password: ")
    f =open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\superuser.txt","r")
    read = f.readlines()
    
    f = 0
    for suser1 in read:
        gmail_to_check_su, pass_to_check_su, contact_to_check_su = suser1.split(" ")
        while True:
            if gmail_su == gmail_to_check_su and gmail_pass_su == pass_to_check_su:
                print("Superuser login successful!!")
                select()
                f = 1
                break
            else:
                break
        if f == 1:
            break
    if f == 0:
        print("Superuser not found plz login valid supersuer.")
    
def staff_login():
    gmail_s = input("Enter staff email address: ")
    gmail_pass_s = input("Enter staff gmail password: ")
    f =open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\staff.txt","r")
    read1 = f.readlines()
    
    f = 0
    for stuser1 in read1:
        gmail_to_check_s, pass_to_check_s, contact_to_check_s = stuser1.split(" ")
        while True:
            if gmail_s == gmail_to_check_s and gmail_pass_s == pass_to_check_s:
                print("Staff login successful!!")
                staff_main()
                f = 1
                break
            else:
                break
        if f == 1:
            break
    if f == 0:
        print("Staff account not found plz login valid id.")
        
def user_login():
    gmail_u = input("Enter customer email address: ")
    gmail_pass_u = input("Enter customer gmail password: ")
    f =open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\user.txt","r")
    read2 = f.readlines()
    
    f = 0
    for user in read2:
        gmail_to_check_u, pass_to_check_u, contact_to_check_u = user.split(" ")
        while True:
            if gmail_u == gmail_to_check_u and gmail_pass_u == pass_to_check_u:
                print("Customer login successful!!")
                user_main()
                f = 1
                break
            else:
                break
        if f == 1:
            break
    if f == 0:
        print("User account not found plz login valid user account.")
def Thank_you():
    print("Superuser account created successful!!!")
    print()
    print("*"*100)
    
# FUNCTION WHICH IS INSIDE THE SUPERUSER LOGIN FUNCTION
def select():
    while True:
        print("1. Create Staff Account")
        print("2. Create user account")
        inputbysu = input("Enter option 1,2 or'exit': ")
        if inputbysu.lower() == "exit":
            break
        try: 
            s = int(inputbysu)
            if s == 1:
                create_staff_account()
                print()
            elif s == 2:
                create_user_account()
                print()
            else:
                print("Please enter a valid input.")
        except:
            print("Invalid input. Please input a valid number.")
def create_staff_account():
    print("Fill up the form.")
    gmail1 = input("Enter your gmail account: ")
    while True:
        if '@gmail.com' in gmail1:
            break
        else:
            print("Invalid email addrerss please enter a valid email address")
            gmail1 = input("Enter your gmail account: ")
    gmail_password1 = input("Enter your gmail password: ")
    contact_number1 = input("Enter your contact number: ")
    len_s = len(contact_number1)
    test = "**********"
    len2_s = len(test)
    while True:
        if len_s == len2_s:
            break
        else:
            print("Invalid contact number please enter a valid number")
            contact_number1 = input("Enter your contact number: ")
            len_s = len(contact_number1)
    
    f = open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\staff.txt","a")
    f.write(f"{gmail1} {gmail_password1} {contact_number1}\n")
    f.close()
def create_user_account():
    print("Fill up the form.")
    gmail2 = input("Enter your gmail account: ")
    while True:
        if '@gmail.com' in gmail2:
            break
        else:
            print("Invalid email addrerss please enter a valid email address")
            gmail2 = input("Enter your gmail account: ")
    gmail_password2 = input("Enter your gmail password: ")
    contact_number2 = input("Enter your contact number: ")
    len1 = len(contact_number2)
    tst = "**********"
    len2 = len(tst)
    while True:
        if len1 == len2:
            break
        else:
            print("Invalid contact number please enter a valid number")
            contact_number2 = input("Enter your contact number: ")
            len1 = len(contact_number2)
    
    f = open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\user.txt","a")
    f.write(f"{gmail2} {gmail_password2} {contact_number2}\n")
    f.close()
#FUNCTION INSIDE STAFF LOGIN
def staff_main():
    while True:
        print("1. Gerate Account number for user")
        print("2. Modify user detail")
        staff_opt = input("Enter a number 1, 2 or 'exit': ")
        if staff_opt.lower() == 'exit':
            break
        try:
            staff_opt = int(staff_opt)
            if staff_opt == 1:
                generate_ac()
                print()
            elif staff_opt == 2:
                modify()
                print()
            else:
                print("Please choose a number 1, 2 or 'exit': ")
        except:
            print("Invalid input. Please enter valid input.")
#FUNCTION INSIDE USER LOGIN FUNCTION
def user_main():
    while True:
        print("1. Registretion Form")
        print("2. Bank login")
        user_opt = input("Enter a number 1, 2 or 'exit': ")
        if user_opt.lower() == 'exit':
            break
        try:
            user_opt = int(user_opt)
            if user_opt == 1:
                registeration_form()
                print()
            elif user_opt == 2:
                bank_login()
                print()
            else:
                print("Please choose a number 1, 2 or 'exit': ")
        except:
            print("Invalid input. Please enter valid input.")

#FUNCTION INSIDE USER_MANI FUNCTION
def registeration_form():
    print("Fill up the registeration form!!")
    print("----------------------------------------------------------------")
    reg_first = input("Enter your first name: ")
    reg_last = input("Enter your last name: ")
    reg_contact_number = input("Enter your contact number: ")
    lenreg = len(reg_contact_number)
    tst1 = "**********"
    lenreg2 = len(tst1)
    while True:
        if lenreg == lenreg2:
            break
        else:
            print("Invalid contact number please enter a valid number")
            reg_contact_number = input("Enter your contact number: ")
            lenreg = len(reg_contact_number)
    reg_email = input("Enter your email address: ")
    while True:
        if '@gmail.com' in reg_email:
            break
        else:
            print("Invalid email addrerss please enter a valid email address")
            reg_email = input("Enter your gmail account: ")
    reg_DOB = input("Enter your DOB (DD/MM/YYYY): ")
    reg_address = input("Enter your address: ")
    reg_gender = input("Enter your gender: ")
    reg_status = input("Enter your status: ")
    
    f2 = open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\userdetails.txt","a")
    f2.write(f"{reg_first} {reg_last} {reg_contact_number} {reg_email} {reg_DOB} {reg_address} {reg_gender} {reg_status}\n")
    f2.close()
    print("Registeration successful!!")
    

    
def bank_login():
    Bank_ac = input("Enter your account number: ")
    ac_pass = input("Enter customer password: ")
    fac = open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\useraccountnumandpass.txt","r")
    readbank = fac.readlines()
    
    f = 0
    for userac in readbank:
        reg_name,bank_account, account_pass = userac.strip().split(" ")
        while True:
            if Bank_ac == bank_account and ac_pass == account_pass:
                print("Customer login successful!!")
                opt_for_user()
                print()
                f = 1
                break
            else:
                break
        if f == 1:
            break
    if f == 0:
        print("User account not found plz login valid user account.")
        
#FUNCTION INSIDE STAFF_MAIN
def generate_ac():
    Name_Custumers = input("Name of the Custumers: ")
    account_number = ''.join(str(random.randint(0, 9)) for _ in range(14))
    password = ''.join(str(random.randint(0, 9)) for _ in range(10))
    f1 = open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\useraccountnumandpass.txt","a")
    f1.write(f"{Name_Custumers} {account_number} {password} \n")
    f1.close()
    
def modify():
    email_to_modify = input("Enter your email address: ")
    while True:
        if '@gmail.com' in email_to_modify:
            break
        else:
            print("Invalid email addrerss please enter a valid email address")
            email_to_modify = input("Enter your gmail account: ")
    f = open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\userdetails.txt", "r")
    re = f.readlines()
    
    f1 = open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\userdetails.txt", "w")
    for line in re:
        details = line.strip().split(" ")
        if details[3] == email_to_modify:
            details[2] = input("Enter your contact number(modify): ")
            details[3] = input("Enter your email address(modify): ")
            details[4] = input("Enter your DOB(modify): ")
            details[5] = input("Enter your address(modify): ")
            details[6] = input("Enter your gender(modify): ")
            details[7] = input("Enter your status(modify): ")
            f1.write(" ".join(details) + "\n")
        else:
            f1.write(line)
    print("Custumer detail modify sucessfully!!")
#Function inside bank_login function
def opt_for_user():
    while True:
        print("1. Saving account")
        print("2. Current account")
        print("3. Change account password: ")
        input_for_chosing_bank = input("Enter 1, 2, 3 or 'exit': ")
        if input_for_chosing_bank.lower() == "exit" :
            print("Thank you for choosing us!!")
            break
        print("----------------------------------------------------------------")
        try:
            n = int(input_for_chosing_bank)
            if n == 1:
                saving_account()
                print()
            elif n == 2:
                current_account()
                print()
            elif n == 3:
                acc_pass_change()
                print()
            else:
                print("Please enter 1, 2, 3 or 'exit'.")
        except ValueError:
            print("Error: Value error.")

#function inside opt_for_user
def saving_account():
    while True:
        print("1.Deposite money")
        print("2.Withdraw money")
        print("3. Statement for deposite")
        print("4. Statement for withdraw")
        print("5. Change account password.")
        saving_input = input("Enter 1, 2, 3, 4 or 'exit':")
        if saving_input.lower() == "exit":
            print("Saving account closed!!")
            break
        print("----------------------------------------------------------------")
        try:
            n = int(saving_input)
            if n == 1:
                deposite_money, deposite_moneyd2 = saving_deposite()
                print()
            elif n == 2:
                withdraw_money, withdraw_money2 = saving_withdraw()
                print()
            elif n == 3:
                statement_sd(deposite_money, deposite_moneyd2)
                print()
            elif n == 4:
                statements(withdraw_money, withdraw_money2)
            else:
                print("Please enter 1, 2 ,3, 4 or 'exit'.")
        except ValueError:
            print("Error: Value error.")
            
def current_account():
    while True:
        print("1.Deposite money")
        print("2.Withdraw money")
        print("3. Statement for deposite")
        print("4. Statement for withdraw")
        current_input = input("Enter 1, 2, 3, 4 or 'exit':")
        if current_input.lower() == "exit":
            print("Current account closed!!")
            break
        print("----------------------------------------------------------------")
        try:
            n = int(current_input)
            if n == 1:
                deposite_money2, deposite_moneyd3 = current_deposite()
                print()
            elif n == 2:
                withdraw_money2b, withdraw_money3 = current_withdraw()
                print()
            elif n == 3:
                statement_wd(deposite_money2, deposite_moneyd3)
                print()
            elif n == 4:
                statementc(withdraw_money2b, withdraw_money3)
            else:
                print("Please enter 1, 2 ,3 or 'exit'.")
        except ValueError:
            print("Error: Value error.")
            
def acc_pass_change():
    account_to_modify = input("Enter your account number: ")
    f = open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\useraccountnumandpass.txt", "r")
    re = f.readlines()
    
    f1 = open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\useraccountnumandpass.txt", "w")
    for line in re:
        details = line.strip().split(" ")
        if details[1] == account_to_modify:
            details[2] = input("Enter new password: ")
            confirmpass = input("Enter new password again:")
            if details[2] == confirmpass:
                f1.write(" ".join(details) + "\n")
                print("Account password modify sucessfully!!")
            else:
                print("Password does not match!!")
        else:
            f1.write(line)
            

            
            
#PERSON2
def saving_deposite():
    deposite_money = int(input("Enter the amount of money to deposite: "))
    f = open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\savingbalance.txt", "r")
    fd = f.readline().strip()
    fdint = int(fd)
    deposite_moneyd2 = deposite_money + fdint
    strg1 = str(deposite_moneyd2)
    f.close()
    
    f1= open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\savingbalance.txt", "w")
    f1.write(strg1)
    f1.close()
    return deposite_money, deposite_moneyd2
    
def saving_withdraw():
    withdraw_money = int(input("Enter the amount of money to withdraw: "))
    f = open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\savingbalance.txt", "r")
    fw = f.readline().strip()
    fwint = int(fw)
    withdraw_money2 = fwint - withdraw_money
    strg1 = str(withdraw_money2)
    f.close()
    
    f2= open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\savingbalance.txt", "w")
    f2.write(strg1)
    f2.close()
    return withdraw_money, withdraw_money2
    
def current_deposite():
    deposite_money2 = int(input("Enter the amount of money to deposite: "))
    f = open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\Currentbalance.txt", "r")
    fd2 = f.readline().strip()
    fdint2 = int(fd2)
    deposite_moneyd3 = deposite_money2 + fdint2
    strgd2 = str(deposite_moneyd3)
    f.close()
    
    f= open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\Currentbalance.txt", "w")
    f.write(strgd2)
    f.close()
    return deposite_money2, deposite_moneyd3

def current_withdraw():
    withdraw_money2b = int(input("Enter the amount of money to withdraw: "))
    f = open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\Currentbalance.txt", "r")
    fw2 = f.readline().strip()
    fwint2 = int(fw2)
    withdraw_money3 = fwint2 - withdraw_money2b
    strgw2 = str(withdraw_money3)
    f.close()
    
    f= open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\Currentbalance.txt", "w")
    f.write(strgw2)
    f.close()
    return withdraw_money2b, withdraw_money3

def statementc(withdraw_money2b, withdraw_money3):
    current_datetime = datetime.today().date()
    print(f"{current_datetime}: You have withdraw Rs {withdraw_money2b}. Now your new balance is {withdraw_money3}")
    f = open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\Currentstatement.txt", "a")
    f.write(f"{current_datetime} {withdraw_money2b} {withdraw_money3}(withdraw)\n")
    f.close

def statements(withdraw_money, withdraw_money2):
    current_datetime = datetime.today().date()
    print(f"{current_datetime}: You have withdraw Rs {withdraw_money}. Now your new balance is {withdraw_money2}")
    f = open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\Savingstatement.txt", "a")
    f.write(f"{current_datetime} {withdraw_money} {withdraw_money2} (Withdraw)\n")
    f.close

def statement_sd(deposite_money, deposite_moneyd2):
    current_datetime = datetime.today().date()
    print(f"{current_datetime}: You have deposite Rs {deposite_money}. Now your new balance is {deposite_moneyd2}")
    f = open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\Savingstatement.txt", "a")
    f.write(f"{current_datetime} {deposite_money} {deposite_moneyd2} (Deposite)\n")
    f.close

def statement_wd(deposite_money2, deposite_moneyd3):
    current_datetime = datetime.today().date()
    print(f"{current_datetime}: You have deposite Rs {deposite_money2}. Now your new balance is {deposite_moneyd3}")
    f = open("C:\\Users\\Acer\\OneDrive - Lord Buddha Education Foundation\\Python assesment\\NP069876-NP069882\\Currentstatement.txt", "a")
    f.write(f"{current_datetime} {deposite_money2} {deposite_moneyd3} (Deposite)\n")
    f.close

main()
