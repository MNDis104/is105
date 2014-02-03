# -*- coding: utf-8 -*-
# Is-205 LAB2

import sys

gruppe = { 'student1': 'Simon Eriksen', \
'student2': 'Minh Nguyen Dinh', \
            'student3': '-', \
}

# Oppgave1: printer ut ascii_fugl
def ascii_fugl():
    print """
       \/_
  \,   /( ,/
   \\\' ///
    \_ /_/
    (./
     '`
          """
pass          
            
# Oppgave2/ oppgave3: retunerer verdiene x og y(definert nedenfor)
def bitAnd(x, y):
    return x&y

#Oppgave 4: returnerer verdiene x og y(definert nedenfor)
def bitXor(x, y):
    return x^y

#Oppgave 5:returnerer verdiene x og y(definert nedenfor)
def bitOr(x, y):
    return x|y     

#Oppgave 6: returnerer "bokstaven" som binær kode.  
def ascii8Bin(bokstav):
    binary = ord(bokstav)   
    return '{0:08b}'.format(binary) 
      
#Oppgave 7: printer ut en setning som binær kode
def transferBin(string):
    l = list(string) 
    for c in l:
        print ascii8Bin(c) 
    pass

#oppgave 8: ascii2Hex printer ut "bokstav" som hexadesimalt kode
            # transferHex printer ut en setning som hexadesimalt kode
def ascii2Hex(bokstav):
    hexy = ord(bokstav)
    return '{0:02x}'.format(hexy)
    
def transferHex(string): 
    l = list(string)
    for c in l:
        print ascii2Hex(c)
    pass
        
#Verdiene defineres for oppgave 2 - 5:

And = bitAnd(6, 5) 
Xor = bitXor(4, 5)
Or  = bitOr(0, 1)
 
#Run Oppgave 1:
print "\n#Oppgave 1"
print "ascii_fugl() resultat:"
ascii_fugl()

#Run Oppgave 2&3:
print "\n#Oppgave 2&3:"
print "bitAnd (6 & 5) = %d" % (And) 

#Run Oppgave 4:
print "\n#Oppgave 4:"
print "bitXor (4 ^ 5) = %d" % (Xor)

#Run Oppgave 5:
print "\n#Oppgave 5:"
print "bitOr (0 | 1) = %d" % (Or)

#Run Oppgave 6:
print "\n#Oppgave 6:"
print "ascii8Bin: Bokstaven (F) i binær kode:"
print ascii8Bin("F") 

#run Oppgave 7:
print "\n#Oppgave 7:"
print "transferBin(\"Python<3\") resultat:"
transferBin("Python<3")

#Run Oppgave 8:
print "\n#oppgave 8"
print "ascii2Hex('G') resultat:"
print ascii2Hex('G')

print "\ntransferHex('Ja, vi elsker!') resultat:"
transferHex('Ja, vi elsker!') 
  
