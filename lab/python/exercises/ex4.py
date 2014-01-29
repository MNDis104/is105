# -- coding: utf-8 -- 
cars = 100 # definerer cars verdi
space_in_a_car = 4.0 #definerer hvor mye plass det er i bilen
drivers = 30 #antall drivere som er tilgjengelig
passengers = 90 #antall passasjerere
cars_not_driven = cars - drivers #definerer carsnotdriven tilgjengelig ved a ta 'cars' minus 'drivers'
cars_driven = drivers #definerer antall biler = antall 'drivers' 
carpool_capacity = cars_driven * space_in_a_car #bilens kapasitet = antall biler('drivers') multiplissert med plass i bilen
average_passengers_per_car = passengers / cars_driven #gjennomsnittlig pas pr bil = pas delt pa biler ('drivers')

print "There are", cars, "cars available." #print res. 'cars' tilgjengelig
print "There are only", drivers, "drivers available." #drivere til gjeng.
print "There will be", cars_not_driven, "empty cars today." #print res. av cars - drivers
print "We can transport", carpool_capacity, "people today." #print res. av cars driven * space in cars 
print "We have", passengers, "to carpool today." # print antall pass. de ma kjore
print "We need to put about", average_passengers_per_car, "in each car." # print res. av hvor mange pas. pr. bil 
