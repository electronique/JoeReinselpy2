class cheese(object):
        def __init__(self,price,c_type,weight,brand,status,tax,returnstatus,openbox):
                
                self.price = price * tax +price
                self.c_type = c_type
                self.weight = weight
                self.brand = brand
                self.tax = tax
                self.openbox = openbox
                self.returnstatus = returnstatus
                if self.openbox == 1:
                        self.price = price /.20+price
                if status == 0:
                    self.status = "For Sale"
                else:
                    self.status = "Sold"
                if returnstatus == 1:
                    self.returnstatus = "Item has been returned"
                    self.status = "For Sale"
                else:
                    self.status = "Sold"
                   
        def displayinfo(self):
           
                print 'Price: ' + str(self.price)
                print 'Cheese Type: ' + str(self.c_type)
                print 'Weight: ' + str(self.weight)
                print 'Brand: ' + str(self.brand)
                print "Status: "+ str(self.status)
                return self
        def returning(self):
               print "Return Status: " + str(self.returnstatus)
               print "Status: "+ str(self.status)
               return self
        def openedbox(self):
               if self.openbox == 0:
                print "opened box"
                return self
   
              
               
                      
# 1 = SOLD
# 0 = For Sale

gouda = cheese(5.00,"aged gouda",3,"Swiss",0,.06,1,1)

gouda.displayinfo().returning().openedbox()