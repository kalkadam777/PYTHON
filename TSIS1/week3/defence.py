from Cars import Car 
class Toyota(Car):
    def __init__(self, model, engine, color, country, price) -> None:
        super().__init__(model, engine, color)
        self.country = country
        self.price = int(price)
        
    def __str__(self) -> str:
        return super().__str__()+' '+self.country+' '+str(self.price)
    
    def tryangle(n):
        for i in range(1,n+1):
            print()
            for j in range(1,i+1):
                print(j,end=' ')
   
   
c1 = Toyota('Hyundai', 1.6, 'White','Japan', 4500000)
c2 = Toyota('Toyota', 3.5, 'Black', 'Japan', 5000000)
c3 = Toyota('Nissan', 2.0, 'Blue', 'Japan', 5600000)
l = [c1,c2,c3]


Toyota.tryangle(5)
        



        