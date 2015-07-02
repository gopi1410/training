class InvalidPhonebookVersion(Exception):
    def __init__(self, arg):
        self.arg = arg
        
def divide(x,y):
    return x/y

def checkVersion():
    return True
try:
    file = open("except.py")
    print(divide(5, 5))
    if checkVersion():
        raise InvalidPhonebookVersion("Version 3 needed")
except FileNotFoundError as e:
    print(e)
finally:
    print("Attempting to close the file")
    if file:
        file.close()
    
print(divide(4, 2))
print(divide(15, 5))