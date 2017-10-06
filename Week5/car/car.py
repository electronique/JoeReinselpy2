class car(object):
        def __init__(self,price,speed, mileage,fuel,tax):
                self.price = price
                self.speed = speed
                self.mileage = mileage
                self.fuel = fuel
                self.tax = tax
                
        def displayAll(self):
            print "Price: "+str(self.price)
            print "Miles per Hour: "+str(self.speed)
            print "Mileage: "+str(self.mileage)
            print "Fuel: "+str(self.fuel)
            if self.price > 10000:
                    
            print "Tax: "+str(self.tax)


auto = car(2000,"35 mph","Full","15 mpg",.12)

print auto.displayAll()