import cal,month
while True:
    ch=int(input("1.find week day\t\n2.the current month \t"))
    if ch==1:
        cal.day()
    elif ch==2:
        month.calander()
    else:
        break

