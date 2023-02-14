class Animal:
    
    def __init__(self, legs, tail, voice, color) -> None:
        self.legs = int(legs)
        self.tail = int(tail)
        self.voice = voice
        self.color = color
        
    def __str__(self) -> str:
        return '{} {} {} {}'.format(self.legs,self.tail,self.voice,self.color)
    
    # def giveVoice():
    #     print('Woof!')
    
class Cat(Animal):
    
    def __init__(self,name, legs, tail, voice, color) -> None:
        self.name = name
        super().__init__(legs, tail, voice, color)
        
        
    def __str__(self) -> str:
        return '{}'.format(self.name)+' '+super().__str__()
h1 = Cat('Tom',4,1,'Meaw','Black')
h2 = Cat('Murzik',4,1,'Meaw',"White")
l = [h1,h2] 

print(h1)