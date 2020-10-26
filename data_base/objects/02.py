# object lifecycle
# 객체를 생성하고 파괴하는 활동 주기        


class PartyAnimal:
    x = 0

    def __init__(self):
        print("I am constructed")
    
    def party(self):
        self.x += 1
        print("So far", self.x)

    def __del__(self):
        print("I am destructed", self.x)

 # ============== constructing a Class ================

an = PartyAnimal()         # I am constructed    <= executing __init___
an.party()                 # 1
an.party()                 # 2
an = 42                    # I am descturcted 2  <= an에 새로운 값을 대입하면서 an 인스턴스의 실행이 끝이 나기 전에 executing __del__ 후, 끝. 원래의 객체는 날아감
print('an contains', an)   # an contains 42      <= 새로운 대입 값 42가 출력 


class PartyName:
    x = 0
    name = ""

    def __init__(self, n):    
        # Constructors can have additional parameters. These can be used to set up instance variables for the particular instance of the class
        self.name = n      # n = self.name 변수 설정이 안됨. 출력값이 ""
        print(n,"variable constructed", self.name, "self variable constructed")    # n, self.name 둘 다 불러올 수 있음

    def party(self):
        self.x += 1
        print(self.name, "party count", self.x)

s = PartyName("Sally")
s.party()

j = PartyName("James")
j.party()
j.party()
j.party()
s.party()

print(s.x)  # 2
print(j.x)  # 3