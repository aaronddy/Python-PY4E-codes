hours = input("Enter hours: ")
pay = input("Enter pay per hour: ")
fh = float(hours)
fp = float(pay)

if fh > 40 :
    # print("Overtime")
    reg  = fh * fp
    ovg = (fh-40) * fp * 1.5
    # print(reg, ovg)
    total = reg + ovg
else:
    # print("Regular")
    total = fh * fp

print("total pay: ",total)