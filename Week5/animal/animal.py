class animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health
    

    def displayhealth(self):
        print "The "+str(self.name)+" has "+str(self.health)+" health"
        return self
    def walk(self):
        self.health = self.health-1
        print str(self.name)+" has "+str(self.health)+" health"
        return self
    def run(self):
        self.health = self.health+5
        print "The "+str(self.name)+" has "+str(self.health)+" health"
        return self
        
class dog(animal):
    def pet(self):
        self.health= self.health+5
        print self.health
        return self

dog1 = dog("Poodle",150)

class dragon(animal):
    def fly(self):
        self.health = self.health-10
        print self.health
        return self
haku = dragon("Haku the Dragon",170)

haku.fly().fly().fly().displayhealth()


#dog1.walk().walk().walk().run().run().pet().displayhealth()
