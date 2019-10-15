import sys

print("How much % you want to be safe investments? (10% = 0.01)")
safe_invest = float(input())

risky_invest = 100 - safe_invest

print("How much $ you want to spend for investing?")
money = float(input())

safe_money = money * safe_invest / 100
risky_money = money - safe_money

print("\n You need to invest " + str(safe_money) + "$ in safe money")
print("\n You need to invest " + str(risky_money) + "$ in risky money")

def start_menu():
    print("\n What you need to know next?")
    print ("\n 1. Total investments in n years \n 2. Exit \n")
    
    try:
        p_choose = float(input())
        
    except ValueError:
        print("\n Invalid character! Try again \n")
        start_menu()
    
    if (p_choose == 1):
        Total_invest()
    elif (p_choose == 2):
        sys.exit()
    
            

def Total_invest():
    print("\n How many years you want to invest same amount? \n")
    years = float(input())
    res = years * (safe_money + risky_money)
    print(res)
    start_menu()

start_menu()



