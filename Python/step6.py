# Persist the phonebook to a file
phone_book = {}
phone_book_file = open("phonebook.csv", mode='a+')
def load_phone_book_from_file():
    phone_book_file.seek(0)
    for line in phone_book_file:
        nameAndNumber = line.split(",")
        phone_book[nameAndNumber[0]] = nameAndNumber[1].rstrip()
def update_phone_book():
    phone_book_file.seek(0)
    phone_book_file.truncate()
    for name in phone_book:
        line = "{},{}\n".format(name,phone_book[name])
        print("Writing this line to phonebook: ",line)
        phone_book_file.writelines(line)
load_phone_book_from_file()

def add_phone_book_entry():
    entryInput = input("Enter name and number comma separated: ")
    nameAndNumber = entryInput.split(sep=",")
    phone_book[nameAndNumber[0]] = nameAndNumber[1]
    
def lookup_phone_book_entry():
    name = input("Enter name to lookup: ")
    if not name in phone_book:
        print("{} does not exist in the phonebook".format(name))
    else:
        number = phone_book[name]
        print("Number for {} is {}".format(name,number))
def exit_prog():
    update_phone_book();
    phone_book_file.close()
    quit()
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
