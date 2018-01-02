import random
class Fish:
    
    def __init__(self,name,size):
        self.fish_name = name
        self.fish_size = size

Pike = Fish('Pike', 10)
Sushi = Fish('Sushi', 12)
Bubbles = Fish('Bubbles', 8)
Casper = Fish('Casper', 6)
Shadow = Fish('Shadow',11 )
Comet = Fish('Comet', 6)
Charlie = Fish('Charlie', 11)
Goldie = Fish('Goldie',1 )
Nemo = Fish('Nemo',5 )
Pumpkin = Fish('Pumpkin', 15)
traut = Fish('traut', 15)
tuna = Fish('tuna', 15)
searobin = Fish('searobin', 15)
whale = Fish('whale', 15)
tough = Fish('tough', 15)
spadefish = Fish('spadefish', 15)

class pond:
    
    pondsname = str(raw_input("enter the pond name:"))
    def __init__(self,pondsname=None,capacity=0):
        self.fishlist=[]
        self.pond_name = pondsname
        self.pond_capacity = capacity
        
    def __addfish__(self,fish):
        self.fishlist.append((fish.fish_name, fish.fish_size))
        
    def pondcapacity(self):
        strength = len(self.fishlist)
        emptyspace = self.pond_capacity - strength
        print "you have %r emptyspace in this pond" %emptyspace
        return self.fishlist      
    
naile = pond("naile",10)
naile.__addfish__(Pike)
naile.__addfish__(Sushi)
naile.__addfish__(Bubbles)
naile.__addfish__(tuna)
naile.__addfish__(traut)
naile.__addfish__(searobin)

lotus = pond("lotus",10)
lotus.__addfish__(Casper)
lotus.__addfish__(Shadow)
lotus.__addfish__(Comet)
lotus.__addfish__(tuna)
lotus.__addfish__(tough)
lotus.__addfish__(whale)

brook = pond("brook",10)
brook.__addfish__(Charlie)
brook.__addfish__(Goldie)
brook.__addfish__(Nemo)
brook.__addfish__(Pumpkin)
brook.__addfish__(tuna)
brook.__addfish__(spadefish)
brook.__addfish__(Pike)

class fisher():
      
    def fisher_details(self,fishlist):
        fishername = str(raw_input("enter the fisher name:"))
        if p.pondsname == "naile":
            self.selectedpond=naile.pondcapacity()
            print "naile", self.selectedpond
        elif p.pondsname == "lotus":
            self.selectedpond= lotus.pondcapacity()
            print "lotus", self.selectedpond
        elif p.pondsname == "brook":
            self.selectedpond = brook.pondcapacity()
            print "brook", self.selectedpond
            
        else:
            print"you have entered wrong pond"
       
    def catchfish(self):
        self.randomfish = random.choice(self.selectedpond)
        self.selectedpond.remove(self.randomfish)
        print self.randomfish
        print self.selectedpond
        return self.randomfish

    def checkfishsize(self):
         selectedfish = []
         if self.randomfish[1] >=10:
             selectedfish.append(self.randomfish)
         else:
             print "you got nothing"
             self.selectedpond.append(self.randomfish)
            
         print selectedfish
         print self.selectedpond     
     
if __name__== '__main__':
    p = pond()
    f = fisher()
    f.fisher_details(1)
    print len(naile.pondcapacity())
    f.catchfish()
    print len(naile.pondcapacity())
    f.checkfishsize()
    
    
