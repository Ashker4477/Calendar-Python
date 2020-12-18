import datetime

def calander():
    x = datetime.datetime.now()
    y = x.strftime("%A")
    print(x.strftime("%B"))
    day = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    for i in range(len(day)):
        if y == day[i]:
            '''#starting day'''
            stday=7-i+1
            print("Sun\tMon\tTue\tWed\tThu\tFri\tSat")
            for i in range (1,8,1):
                if i<stday:
                    print("","\t",end="")
                elif i>=stday:
                    print(i-stday+1,"\t",end="")
            print()
            for i in range(8,15,1):
                if i<stday:
                    print("","\t",end="")
                elif i>=stday:
                    print(i-stday+1,"\t",end="")
            print()
            for i in range(15,22,1):
                if i<stday:
                    print("","\t",end="")
                elif i>=stday:
                    print(i-stday+1,"\t",end="")
            print()
            for i in range(22,29,1):
                if i<stday:
                    print("","\t",end="")
                elif i>=stday:
                    print(i-stday+1,"\t",end="")
            print()
            lstday=calendar.monthrange(x.year,x.month)[1]
            lst=lstday+stday-1
            for i in range(29,lst,1):
               if i<stday:
                    print("","\t",end="")
               elif i>=stday:
                    print(i-stday+1,"\t",end="")
            print()
        
    
    
