# Practice

class PayPerHour:
    rate = 20000
    hour = 0
    pay = 0

    def __init__(self, p):
        self.pay = p
        print("기본급:", self.pay)

    def working(self):
        self.hour += 8
        self.pay += self.hour*self.rate
        print("일급:", self.pay)

money = PayPerHour(30000)
money.working()

class PayPerWeek(PayPerHour):
    week = 7

    def aWeek(self):
        self.working()                             # PayPerHour.working() 이 실행되면서 일급 계산
        self.pay = self.pay*self.week              # PayPerHour.working()으로 나온 self.pay에 7을 곱해서 주급 계산
        print("주급:", self.pay, "시간:", self.hour*self.week)
        
money2 = PayPerWeek(30000)
money2.aWeek()

