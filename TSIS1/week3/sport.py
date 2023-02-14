class Sportsman:
    
    def __init__(self, id, name) -> None:
        self.id = int(id)
        self.name = name
        
    def __str__(self) -> str:
        return '{} {}'.format(self.id, self.name)
    
    
class TeamSport(Sportsman):

    def __init__(self, id, name, type, num_playces) -> None:
        super().__init__(id, name)
        self.type = type
        self.num_playces = int(num_playces)
    
    def __str__(self) -> str:
        return super().__str__()+' '+'{} {}'.format(self.type,self.num_playces)
    
class classFootball(TeamSport):
    def __init__(self, id, name, type, num_playces,team_name,sport_id) -> None:
        super().__init__(id, name, type, num_playces)
        self.team_name=team_name
        self.sport_id=sport_id
    def __str__(self) -> str:
        return super().__str__()+' '+'{} {}'.format(self.team_name,self.sport_id)
    
s1 = classFootball(123456, 'Nefr', 'Football', 10,'Real Madrid','Spain')
s2 = classFootball(323452, 'Daulet', 'Football', 15,'Barcelona','spain')
s3 = classFootball(234123, 'Azamat', 'Football', 5,'Man city','England')
l = [s1,s2,s3]

for i in l:
    print(i)