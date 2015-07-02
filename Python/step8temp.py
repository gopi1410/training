#----------------------------
# Include address in the phone book and make the dictionary hold an array instead of a string
#----------------------------
phone_book = {}
phone_book_file = open("phonebook.csv", mode='a+')

class PhoneRecord:
    'This is a class that represents a single phone record'
    def __init__(self,nm,nu,ad):
        self.name=nm
        self.number = nu
        self.address = ad

def add_phone_book_entry():
    entryInput = input("Enter name, number and address comma separated: ")
    nameNumberAddress = entryInput.split(sep=",")
    phone_book[nameNumberAddress[0]] = PhoneRecord(nameNumberAddress[0],nameNumberAddress[1],nameNumberAddress[2])

def lookup_phone_book_entry():
    name = input("Enter name to lookup: ")
    if not name in phone_book:
        print("{} does not exist in the phonebook".format(name))
    else:
        numberAdress = phone_book[name]
        print("Number for {} is {}. And address: {}".format(name,numberAdress.number,numberAdress.address))

def load_phone_book_from_file():
    phone_book_file.seek(0)
    for line in phone_book_file:
        nameNumberAddress = line.split(sep=",")
        phone_book[nameNumberAddress[0]] = PhoneRecord(nameNumberAddress[0],nameNumberAddress[1],nameNumberAddress[2])

def update_phone_book():
    phone_book_file.seek(0)
    phone_book_file.truncate()
    for name in phone_book:
        line = "{},{},{}\n".format(name,phone_book[name].number,phone_book[name].address)
        print("Writing this line to phonebook: ",line)
        phone_book_file.writelines(line)
        
def exit_prog():
    update_phone_book();
    phone_book_file.close()
    quit()
        

load_phone_book_from_file()

while True:
    print("Choose an action:")
    print("1. Add a phone book entry")
    print("2. Lookup a phone book entry")
    print("3. Exit")
    choice = input("Enter choice: ")
    choice = int(choice)
    if choice==1:
        add_phone_book_entry()
    elif choice==2:
        lookup_phone_book_entry()
    elif choice==3:
        exit_prog()
