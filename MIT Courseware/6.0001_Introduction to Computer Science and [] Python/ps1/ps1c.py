# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:22:18 2023

@author: Green Office Exiled
"""
currentlyCalculating = True
while currentlyCalculating:
    
    downPaymentPercentage = .25
    houseCost = 1000000 #1M!
    downPayment = houseCost*downPaymentPercentage
    
    annualSalary= 0.0
    semiAnnualRaiseRate = .07
    investmentRate = .04
    
    lower = 0
    upper = 10000
    savingsRate = (lower+upper)/2; #the starting savings rate is always right in the middle in bisection search
    guess = savingsRate
    
    print("So, you want to save up for a $1M house in 3 years? Lets see if that is possible...")
    annualSalary = float(input("Enter the starting salary:"))
    annualSalarySimulated = 0;
    
    months = 0
    bisectionStep = 1
    
    while (savingsRate < 9999.9):
        
        currentSavings = 0.0
        annualSalarySimulated = annualSalary
        months = 0
        
        #TESTERS v
        # print("Simulation attempt:",str(bisectionStep))
        # print("Savings rate: "+str(int(savingsRate/10000*100))+"%")
        
        for months in range(37):
            if (months % 6) == 0:
                annualSalarySimulated += annualSalarySimulated * semiAnnualRaiseRate
  
            currentSavings += (annualSalarySimulated*(savingsRate/10000)/12)
            currentSavings += (currentSavings*investmentRate/12)
            #TESTERS v
            # print("Current Savings =",str(currentSavings*100/100),"on month",str(months))
            
            if (currentSavings > downPayment - 100):
                break
            
        #TESTERS v
        # print("upper bound",upper)
        # print("lower bound",lower)
        # print("savingsRate",savingsRate)
        # print("guess",guess)
        
        guess = int(guess*100)/100
        
        if currentSavings > (downPayment - 100) and currentSavings < (downPayment + 100) or currentSavings == downPayment:
            print("\nSuccess! We reached a down payment of about $"+str(int(downPayment)),"in exactly 36 months at a savings rate of",str(int(savingsRate/10000*100))+"%!")
            break
        elif currentSavings > downPayment + 100: 
            #if we end up with more than the down payment after 36 months, we can save less every month
            upper = int(guess)
        elif currentSavings < downPayment - 100:
            #if we end up with less than the down payment after 36 months, we need to save more every month
            lower = guess
        guess = (upper+lower)/2
        savingsRate = guess;
        
        bisectionStep += 1
        
        #TESTER to prevent infinite loops early on in development
        # if (bisectionStep >= 16):
        #     break
        
        #TESTERS!! VV
        # print("upper bound",upper)
        # print("lower bound",lower)
        # print("savingsRate",savingsRate)
        # print("guess",guess)
        # input("Press enter to keep going:")

    if (savingsRate >= 9999):
        print("\nIt is not possible to pay the down payment in three years at your current salary..")
    else:
        print("Best savings rate: "+str(savingsRate/10000))
        print("Steps in bisection search: "+str(bisectionStep))
    
    
    print("\nWant to play again? y/n")
    answer = input()
    if answer == "n" or answer == "N" or answer == "No" or answer == "no" or answer == "NO":
        currentlyCalculating = False
    print("\n")
    
