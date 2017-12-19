import random

class fishing:

    existingfishes = [('casper',10),('sushi',7),('bubbles',10),('nemo',8),('comet',10),('shadow',16),
                      ('charlie',19),('pumpkin',6),('goldie',9),('sea mullt',15),('wahoo',6),('snaper',17),
                      ('tuna',8),('traut',10),('searobin',19),('spadefish',4),('stringray',14),('stripedbass',12),
                      ('tough',3),('whale',18)]

    def fish_details(self):                        #getting fish details & total strength
        print "fish dtails"
        times = int(raw_input("how many fishes  you are going to enter :")) 
        for i in range(times):
            fishtype = str(raw_input("Enter the fish name:"))
            fishsize = int(raw_input("enter the fish size in cms:"))
            self.existingfishes.append((fishtype, fishsize))
        countoffish = [x[0] for x in self.existingfishes]
        strength = len(countoffish)
        print strength
        self.emptyspacecalculation(strength)
        return strength,countoffish
    
    def executeonce(self,strength):                 #getting the pond capacity only once                  
        flag = True
        if flag:
            self.capacity = int(raw_input("enter the maximum fishes can be stored:"))
            print self.existingfishes
            self.emptyspacecalculation(strength)
            flag = False
        else:
            pass
        return flag,self.capacity

    def emptyspacecalculation(self,strength):          #calculating empty space in  the pond
        emptyspace = self.capacity - len(self.existingfishes)
        self.pondscapacity(strength,emptyspace)
        return emptyspace

    def pondscapacity(self,strength,emptyspace):        # showing wether user can add  some fishes
        if strength < self.capacity:                        
            print "you have %d empty space in the pond" %emptyspace
            self.addingfishes(emptyspace)
        elif strength == self.capacity:
            print "you can't add any more pond is full"
            self.fisher(fish_list)
        else:
            print "your strength is greater than capacity"
        return emptyspace
    
    def addingfishes(self,emptyspace):                  # user adding new fishes to the pond according to his wish
        
        ischoice = True
        print "do you want to add some more"
        choice=str(raw_input("""y: Yes,n: No,Enter your choice:"""))
        if (choice =='y') or (choice =='Y'):
           self.fish_details()               
        elif  (choice =='n') or (choice =='N'):            
            print "thankyou"
            self.gofishing()
        else:
            print "you have entered a wrong key"
            self.addingfishes(emptyspace)
        ischoice =False
        
    def catchfish(self):                                  # caching fishes by no.of chances
        totalchances = int(raw_input("Chance:"))
        fish_list= []
        for chance in range(totalchances):
            if chance <= totalchances:
                fish_list += random.sample(self.existingfishes, 10)
        self.sort_fish = fish_list
        self.sort_by_size(totalchances)
        return totalchances
       

    def sort_by_size(self,totalchances):                               #selecting fishes by prefered size
        selectlist = []
        sizeprefered = int(raw_input("enter the prefered size:"))
        for fish in self.sort_fish:
            if fish[1] >= sizeprefered :
                selectlist.append(fish)
            else:
                self.existingfishes.append(fish)
        print "in given %d chances" %totalchances
        print"fishes you got is %r:" %selectlist
        return selectlist
    
          
    def gofishing(self):                                   # fisher withe a name going to a selected pond
        pondname = "naile"
        selectlist = []
        fishername = str(raw_input("enter the name of the fisher:"))
        nameofpond = str(raw_input("enter the name of the pond's name:"))
        if nameofpond == pondname:
            print "Hi %s you have entered the correct pond name:" %fishername
            self.catchfish()   
        else:
            print "sorry  you have entered the wrong pond name"
            self.gofishing()
        return nameofpond

if __name__== '__main__':
    p = fishing()
    p.executeonce(1)

    
