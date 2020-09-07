hours = input("Enter hours: ")
pay = input("Enter pay per hour: ")

try:
    fh = float(hours)
    fp = float(pay)
except:
    print("Error, please enter numeric input.")
    quit()
    
print(fh,fp)

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