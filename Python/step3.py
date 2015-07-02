
#------------------------------
# Use of loops to process a list

phrases = []
phrases.append("Its a small world with technology yet a vast place to travel. \
World is like a book, if you do not travel, its like you have read just one page.")
phrases.append("Trust is like paper.. once crumpled, it cant be perfect again")
phrases.append("Three difficult things to do: You cant count your hair, \
you cant wash your eyes with soap, you cant breathe with your tongue out. \
Now please put your tongue back in")

for phrase in phrases:
    userCount = input("Count the words in the paragraph: \n{}".format(phrase))
    wordArray = phrase.split(" ")
    if int(userCount)==len(wordArray):
        print("Thats right!")
    else :
        print("This paragraph had {} words".format(len(wordArray))) 
        
