name = input("Your name: ")
age = input("... and how old did you say you were? ")
age = int(age)
if age>50 :
    print("Hello {} you are never too old to learn python at {}".format(name,age))
elif age>40 :
    print("Hello {} how did you get by for {} years without python!".format(name,age))
else :
    print("Hello ",name," today is a great day to learn python")
    
