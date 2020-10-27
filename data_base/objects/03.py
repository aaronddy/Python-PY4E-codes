# Inheritance
# 코드 재사용의 한 형태 객체 지향 프로그래밍의 고급 주제 중 하나    

class PartyName:
    x = 0
    name = ""

    def __init__(self, n):    
        self.name = n      
        print(self.name, "self variable constructed")    

    def party(self):
        self.x += 1
        print(self.name, "party count", self.x)

# ================= extending this clsas ===================

class FootBallFan(PartyName):         # PartyName 클래스를 상속하는 새로운 클래스 
    points = 0
    
    def touchdown(self):
        self.points += 7
        self.party()                  # ParyName의 capability를 그대로 사용
        print(self.name, "points", self.points)

j = FootBallFan("Robbin")
j.party()
j.party()
j.touchdown()

'''
Robbin self variable constructed    <= executing PartyName constructor
Robbin party count 1                <= executing PartyName party()
Robbin party count 2                <= executing PartyName party()
Robbin party count 3                <<= executing FootBallFan touchdown --> PartyName party()
Robbin points 7

Inheritance: the ability to extend a class to make a new class
'''