import random
import string
import os
import reader

def passwordman():

    ask = input('LOOKING UP OR ADDING? ')
    answ = ask

    if answ == 'lookup':
        reader.readfiles()



    # FUNCTION THAT WILL CREATE A 12 CHARACTER PASSWORD THAT HAS UPPERCASE, LOWERCASE, AND NUMBERS
    def create_pass():

    # WILL ASK THE USER FOR THE SERVICE AND FOR THE ACCOUNT NAME
        account_input = input("WHAT IS THE NAME OF THE ACCOUNT?: ")

        password = (''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits +
                                                string.ascii_lowercase) for i in range(12)))
        password = str("THE PASSWORD FOR " + account_input + " is: " + password)
        return password


    # CREATE THE FILE
    def write():
        #path = '/home/linux/Desktop'
        #fullpath = os.path.join(path, 'passwords.txt')
        passfile = open('passwords', 'a')
        passfile.write(create_pass() + "\n")
        passfile.close()


    write()



    cont = input("WOULD YOU LIKE TO ADD MORE PASSWORDS? ")
    cont = cont.lower()

    while cont == "yes":
        path = '/home/linux/Desktop'
        fullpath = os.path.join(path, 'passwords.txt')
        passfile = open(fullpath, 'a')
        passfile.write(create_pass() + "\n")
        passfile.close()

        cont = input("WOULD YOU LIKE TO ADD MORE PASSWORDS? ")
        cont = cont.lower()
passwordman()