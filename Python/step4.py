# Using sets to find distinct word count.
# Using sets to find common words via intersection


phrases = []
phrases.append("Its a small world with technology yet a vast place to travel, Hello")
phrases.append("Trust is like paper.. once crumpled, it cant be perfect again, Hello")
phrases.append("Three difficult things to do: Hello")

commonWords = set()
commonWords.update(phrases[0].split(" "))
print(commonWords)
for phrase in phrases:
    userCount = input("Count the distinct words in the paragraph: \n{}".format(phrase))
    distinctWordSet = set()
    wordArray = phrase.split(" ")
    distinctWordSet.update(wordArray)
    commonWords.intersection_update(distinctWordSet)
    if int(userCount)==len(distinctWordSet):
        print("Thats right!")
    else :
        print("This paragraph had {} distinct words".format(len(distinctWordSet)))
else:
    print("The list of words that were common to all the paragraphs is: {}".format(commonWords))
    
