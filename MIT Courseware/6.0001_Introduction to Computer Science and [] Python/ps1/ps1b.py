# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:22:18 2023

@author: Green Office Exiled
"""
currentlyCalculating = True
while currentlyCalculating:
    
    total_cost = 0.0 #of dream home
    portion_down_payment = 0.0

    annual_salary = 0.0
    portion_saved = 0.0
    monthly_income = 0.0
    portion_saved = 0.0
    
    semi_annual_raise = 0.0

    current_savings = 0.0
    r = 0.04 #this is the annual rate that your investments increase
    months_to_save = 0 #in order to afford dream home
    
    print("So, you think you can buy a house? Let's see about that....")
    
    print("Please enter your annual salary:")
    annual_salary = float(input())
    monthly_income = (annual_salary/12)
    # print("monthly salary =",str(monthly_salary))
    monthly_income = int(monthly_income*100) / 100
    print("You make about $"+str(int(monthly_income))+" per month! (taxes not included)\n")
    
    #vvv adds your investments to monthly income
    
    
    print("Please enter the total cost of your dream home:")
    total_cost = float(input())
    portion_down_payment = int(total_cost*.25*100) / 100 #the *100) / 100 allows only 2 decimal places
    print("You will need to save up $"+str(portion_down_payment)+" to afford the down payment on this house!\nThis assumes that a down payment is 25% of the cost of the home.\n")

    print("Please enter the percent of your salary you want to save every year:")
    print("(as a decimal, ex: .10 for 10%)")
    portion_saved = float(input())
    
    print("\nPlease enter the percentage of your semi-annual raise as a decimal:")
    semi_annual_raise = float(input())
    
     
    #calculate how many months you would need to save
    # months_to_save = int((portion_down_payment/monthly_salary) * 100) / 100 #this doesnt work!
    months_to_save = 0
    saving = True
    while saving:
        months_to_save += 1
        current_savings += (annual_salary*portion_saved/12)
        if (months_to_save % 6) == 0:
            annual_salary += annual_salary * semi_annual_raise
        # print(current_savings)
        if current_savings > portion_down_payment:
            saving = False
        else:
            current_savings += (current_savings*r/12)
            
    print("\nYou will need to save for "+str(months_to_save)+" months to afford this house...")
    
    print("\nWant to play again? y/n")
    answer = input()
    if answer == "n" or answer == "N" or answer == "No" or answer == "no" or answer == "NO":
        currentlyCalculating = False
    print("\n")
    
