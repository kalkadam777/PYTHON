class Animal():
    legs=4
    tail=1
    
    def init(self,col,voic):
        self.color=col
        self.voice=voic
    
    def give_voice(self):
        g="Legs num: {} \nTail num: {} \nVoice type: {} \nColor: {}"
        print(g.format(self.legs,self.tail,self.voice,self.color))
    
    def set_name(self,name):
        self.name=name
    
    def get_name(self):
        print(self.name)
        
class Cat(Animal):
    
    def set_breed(self, breed):
        self.breed=breed
   
    def give_voice(self): 
        g="Legs num: {} \nTail num: {} \nVoice type: {} \nColor: {}\nBreed : {}"
        print(g.format(self.legs,self.tail,self.voice,self.color,self.breed))
        print("Meow")
     
col=input("color:")
voice=input("voice:")        
Cat1=Cat(col,voice)
Cat1.give_voice()
Cat1.set_name()
Cat1.get_name()