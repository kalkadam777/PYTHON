class Human:
    
    def __init__(self, name, surname, weight, height, city,) -> None:
        self.name = name
        self.surname = surname
        self.weight = int(weight)
        self.height = int(height)
        self.city = city
        
    def __str__(self) -> str:
        return '{} {} {} {} {}'.format(self.name, self.surname, self.weight, self.height,self.city)
    
    
class Employee(Human):
    def __init__(self, name, surname, weight, height, city, job, salary) -> None:
        super().__init__(name, surname, weight, height, city)
        self.job = job
        self.salary = int(salary)
    
    def __str__(self) -> str:
        return super().__str__()+' '+self.job+' '+self.salary
    
    
h1 = Employee('Alzhan', 'Daribaev', 60, 180,'Deli','Teacher',2304000)
h2 = Employee('Daulet', 'Darmen', 60, 187,'Almaty','Oilman',100000000)
h3 = Employee('Erkebulan', 'Koishybai', 65,183,'Almaty','Backend developer', 50000000)

l = [h1,h2,h3]

for i in l:
    print(i.salary)






# l = [h1,h2,h3]



    
        
        