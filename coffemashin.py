drink="on"
print("Welcom to the coffe machine program ☕")
print(''' .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.   
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |  
| |     ______   | || |     ____     | || |  _________   | || |  _________   | || |  _________   | || |  _________   | |  
| |   .' ___  |  | || |   .'    `.   | || | |_   ___  |  | || | |_   ___  |  | || | |_   ___  |  | || | |_   ___  |  | |  
| |  / .'   \_|  | || |  /  .--.  \  | || |   | |_  \_|  | || |   | |_  \_|  | || |   | |_  \_|  | || |   | |_  \_|  | |  
| |  | |         | || |  | |    | |  | || |   |  _|      | || |   |  _|      | || |   |  _|  _   | || |   |  _|  _   | |  
| |  \ `.___.'\  | || |  \  `--'  /  | || |  _| |_       | || |  _| |_       | || |  _| |___/ |  | || |  _| |___/ |  | |  
| |   `._____.'  | || |   `.____.'   | || | |_____|      | || | |_____|      | || | |_________|  | || | |_________|  | |  
| |              | || |              | || |              | || |              | || |              | || |              | |  
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |  
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   ''')
machine={"water":500,"milk":300,"coffee":60,"money":12}
requirments={ 
    "latte":{"water":200,"milk":150,"coffee":24,"money":2.5}
    ,"espresso":{"water":50,"milk":0,"coffee":24,"money":1.5}
    ,"cappuccino":{"water":250,"milk":100,"coffee":18,"money":3}
}
def printReport():
    print(f"Water: {machine['water']}\nMilk: {machine['milk']}\nCoffee: {machine['coffee']}\nMoney: {machine['money']}")
def checkReq(drink):
    if machine["water"]>= requirments[drink]["water"]:
        
        if machine["milk"]>= requirments[drink]["milk"]:
            if machine["coffee"]>= requirments[drink]["coffee"]:
                return True
            else:
                print("the machine ran out of coffe sorry!☕")
        else:
            print( "the machine ran out of milk sorry!🥛")
    else:
        return print("the machine ran out of water sorry!🫗")

def calculate(paide,drink):
    if paide<requirments[drink]["money"]:
        return 0
    else:
        return paide-requirments[drink]["money"]
def sub(drink):
    machine["water"]=machine["water"]-requirments[drink]["water"]
    machine["milk"]=machine["milk"]-requirments[drink]["milk"]
    machine["coffee"]=machine["coffee"]-requirments[drink]["coffee"]
def insertCash(drink):
    pay=[]
    cash=input( "press how much of each do you want to pay quarter,dimes, nickel,pennies :💵 ")
 
    for mony in cash:
        pay.append(int(mony))
        
    payment=pay[0]*0.25+pay[1]*0.10+pay[2]*0.05+pay[3]*0.01
    change=round(calculate(payment,drink),2)
    if change!=0:
         if machine["money"]>=change:
             print(f"Thank you! your change:{change}$🪙 ")
         else:
             print("the machine ran out of change sorry!💰")
    else :
        print("you paied less than what is required!💸, you got a refound!")
        return 0
    machine["money"]=machine["money"]+payment-change
while True:
    drink=input("What would you like? (espresso/latte/cappuccino):🍵")
    if(drink=="off"):
        break
    
    if drink=="report":
        printReport()
        continue
    req=checkReq(drink)
    if req==True:
       if insertCash(drink)!=0:
          sub(drink)
          print(f"Here is your {drink}🧋. Enjoy!💆🏽‍♀️")
    else:
        continue
    