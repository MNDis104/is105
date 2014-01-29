# -- coding: utf-8 -- 
formatter = "%r %r %r %r" # forteller hvor mange ganger det skal printes

print formatter % (1, 2, 3, 4) #printer verdi
print formatter % ("one", "two", "three", "four") #printer verdi
print formatter % (True, False, False, True) #printer verdi
print formatter % (formatter, formatter, formatter, formatter) #printer formatter 4 ganger(dvs 16 ganger)
print formatter % ( #printer statement i rekkefølge"
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)


