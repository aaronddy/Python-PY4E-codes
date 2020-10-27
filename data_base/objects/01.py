# simple example

class PartyAnimal:                     # class is a reserved word / PartyAnimal is a template for making PartiAnimal objects
    x = 0                              # Each PartyAnimal object has a bit of data == Attribute

    def party(self):                   # Method
        self.x +=1
        print('So far', self.x)        # Each PartyAnimal object has a bit of code.  클래스 생성

an = PartyAnimal()                     # Construct a PartyAnimal object and store it in 'an'    인스턴스 생성 


an.party()
an.party()                             # Tell the an object to run the party() code within
an.party()                             # == PartyAnimal.party(an)


print("Type", type(an))                # Type <class '__main__.PartyAnimal'>
print("Dir", dir(an))                  # Dir ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
                                       # 'party', 'x']  

                                       # '.' 은 객체를 들여다보는 연산자    