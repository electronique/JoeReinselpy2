class Bike(object):
        def __init__(self,price, max_speed, miles):
                self.price = price
                self.max_speed = max_speed
                self.miles = miles


        def displayinfo(self):
                self.price = 250
                self.max_speed = 100
                self.miles = 0
                return self
                
        def ride(self):
              print "riding"
              self.miles = 20
              return self

        def reverse(self):
                print "reversing"
                self.miles = 0
                return self

bicycle = Bike(10,200,30)

print bicycle.displayinfo().price
print bicycle.displayinfo().max_speed
print bicycle.displayinfo().miles 
print bicycle.ride().miles
print bicycle.reverse().miles
        

