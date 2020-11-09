#basic print for python2
print ("Hello World")

name = "Jay"
print (name)
name = "Tommy"
print (name)


#string manip

word = "Panama"
print (word + " Canal")
print (word[0])
print (word[-2])
print (word[0:3])
print (len(word))
for c in word: 
    print (c)

print (word.find( "Pan"))
print (word.upper())
print (word.split("m")) #Useful
print (word.split("a")) #Useful


#Formatting
print ("a %s parrot" % "dead")

