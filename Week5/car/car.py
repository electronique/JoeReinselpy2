class car(object):
        def __init__(self,price,speed, mileage,fuel,tax):
                self.price = price
                self.speed = speed
                self.mileage = mileage
                self.fuel = fuel
                self.tax = tax
                
        def displayAll(self):
            print auto.price
            print auto.speed
            print auto.mileage
            print auto.fuel
            print auto.tax

auto = car(2000,100,4000,"filled", .15)

print auto.displayAll()