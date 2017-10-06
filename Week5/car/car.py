class car(object):
<<<<<<< HEAD
        def __init__(self,price,speed, mileage,fuel,tax):
=======
        def __init__(self,price,speed,fuel,mileage,tax):
>>>>>>> 147172b0f5e4cb25f646fc6f38f2d6cb3c1a1364
                self.price = price
                self.speed = speed
                self.mileage = mileage
                self.fuel = fuel
                self.tax = tax
                
        def displayAll(self):
            print "Price: "+str(self.price)
<<<<<<< HEAD
            print "Miles per Hour: "+str(self.speed)
            print "Mileage: "+str(self.mileage)
            print "Fuel: "+str(self.fuel)
            if self.price > 10000:
                    
            print "Tax: "+str(self.tax)


auto = car(2000,"35 mph","Full","15 mpg",.12)

print auto.displayAll()
=======
            print "MPH: " +str(self.speed)
            print "MPG: "+str(self.mileage)
            print "Fuel: "+str(self.fuel)
            if self.price > 10000:
                     self.tax = .15
            else:
                     self.tax = .12
            print "Tax: "+str(self.tax)

auto = car(2000,"35 mph","Full","15mpg",0)
auto2= car(2000,"5 mph","Not Full","15mpg",0)
auto3= car(2000,"15 mph","Kind of full","95mpg",0)
auto4= car(2000,"25 mph","Full","25mph",0)
auto5= car(2000,"45mph","Empty","25mpg",0)
auto6= car(20000,"35mph","Empty","15mpg",0)
print auto.displayAll()
print auto2.displayAll()
print auto3.displayAll()
print auto4.displayAll()
print auto5.displayAll()
print auto6.displayAll()
>>>>>>> 147172b0f5e4cb25f646fc6f38f2d6cb3c1a1364
