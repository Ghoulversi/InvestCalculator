import sys
import os

print("How much % you want to be safe investments?")
safe_invest = float(input())

risky_invest = 100 - safe_invest

print("How much $ you want to spend for investing?")
money = float(input())

safe_money = money * safe_invest / 100
risky_money = money - safe_money

print("\n You need to invest " + str(safe_money) + "$ in safe money")
print("\n You need to invest " + str(risky_money) + "$ in risky money")

def start_menu():
    print("\n What you want to know next?")
    print ("\n 1. Total investments in n months \n 2. How much time u need for a item \n 3. How many money you will make with n% revenue with risky or safety \n 4. Exit \n")
    
    try:
        p_choose = float(input())
        
    except ValueError:
        print("\n Invalid character! Try again \n")
        start_menu()
    
    if (p_choose == 1):
        Total_invest()
    elif (p_choose == 2):
        item_time()
    elif (p_choose == 3):
        revenue_procentage()
    elif (p_choose == 4):
        sys.exit()
    else:
        print("No such option")

def Total_invest():
    print("\n How many years you want to invest same amount? \n")
    years = float(input())
    res = years * (safe_money + risky_money)
    print(res)
    start_menu()
          
def item_time():
    try:
        print("\n How much your item costs? \n")
        item_cost = float(input())
        print("\n How many months you want to save? \n")
        s_months = float(input())
        
        
    except ValueError:
        print("\n Invalid character! Try again \n")
        item_time()
    
    res = item_cost / s_months
    print("\n You need to save " + str(res) + "$ every month to buy your item in " + str(s_months) + " months \n")
    start_menu()
    
def revenue_procentage():
    try:
        print("\n % you want of revenue? \n")
        r_procentage = float(input())
        
        print("\n Risky revenue or Safe revenue? \n [r/s]" )
        r_option = input()
        
        if (r_option == "r"):
            res = risky_money * (r_procentage / 100)
            print("You will learn: " + str(res))
        elif (r_option == "s"):
            res = safe_money *  (r_procentage / 100)
            print("You will learn: " + str(res))
        else:
            print("wrong answer, try again")
            revenue_procentage()
            
    except ValueError:
        print("\n Invalid character! Try again \n")
        revenue_procentage()
        
    start_menu()

start_menu()



