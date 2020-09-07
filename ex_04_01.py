def computePay(hours, rate):
    # print('in compute pay', hours, rate)

    if fh > 40 :
        reg  = hours * rate
        ovg = (hours-40) * rate * 1.5
        pay = reg + ovg
    else:
        pay = hours * rate
    # print("Returning ",pay)
    return pay    # 리턴값은 total 변수값으로 들어가서 마지막 프린트 문에서 출력

sh = input("Enter hours: ")
sr = input("Enter pay per hour: ")
fh = float(sh)
fr = float(sr)

total = computePay(fh, fr)
print("total pay: ",total)


