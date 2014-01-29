# -- coding: utf-8 -- 
x = "There are %d types of people." % 10 #%10 definerer %d
binary = "binary" #bin = bin
do_not = "don't" #do_not= don't
y = "Those who know %s and those who %s." % (binary, do_not)#definerer begge%s i parantes etter rekkefølge 

print x #printer x
print y #printer y

print "I said: %r." % x #reforteller statement x
print "I also said: '%s'." % y #reforteller statement y MED string within a string

hilarious = False
joke_evaluation ="Isn't that joke so funny?! %r" 

print joke_evaluation % hilarious #printer joke og hilarious 

w="This is the left side of..."
e="a string with a right side."

print w+e #printer w + e 
