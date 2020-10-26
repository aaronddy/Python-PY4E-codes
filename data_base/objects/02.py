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