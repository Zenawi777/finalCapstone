import math

# This program allows a customer or user to access financial calculators that will work out the return of an investmetn and a repayment plan for a home loan.
# User inputs either investment or bond to choose between the calculators
# The program will also request the user to choose between a simple and compound interest
  
user_input = input("Please enter either bond or investment to choose the type of work the software should do for you: ")

user_input = user_input.lower()


if user_input == "investment":
    
    deposit_money = float(input("Please enter the amount of money you want to deposit: "))
    
    investment_time = int(input("Please enter the length of investment time in years: "))
    
    interest_rate = float(input("Please enter only the number of the interest rate without the percent sign: "))
    
    interest_rate = interest_rate / 100
    
    user_investment = input("Do you want compound or simple interest? Enter simple_interest for simple interest or compound_interets for compound interest. ")
    
    
    if user_investment == "simple_interest":
        
        
        simple_interest = deposit_money * ( 1 + interest_rate * investment_time)
        
        print("------------------------------------------------------------------------------------------------\n\n")
        
        print(f"The return of your {deposit_money} investment for {investment_time} years is:  ", simple_interest, "\n\n")
        
        print("------------------------------------------------------------------------------------------------")
        
        
    elif user_investment == "compound_interest":
        
        compound_interest = deposit_money * math.pow( (1 + interest_rate), investment_time)
        
        print("------------------------------------------------------------------------------------------------\n\n")
        
        print(f"The return of your {deposit_money} investment for a compound interest for {investment_time} years is: ", compound_interest, "\n\n")
        
        print("------------------------------------------------------------------------------------------------")
        
        
    else:
        
        print("Please enter either simple_interest or compound_interest")
        
        
elif user_input == "bond":
    
    property_value = int(input("Please enter the current value of the property: "))
    
    repayment_time = int(input("Please enter the length of the plan in months: "))
    
    interest_rate = float(input("Enter the interest rate: "))
    
    interest_rate = (interest_rate / 100) / 12
    
    repayment = (interest_rate * property_value) / (1 - (1+interest_rate)**(-repayment_time))
    
    print("------------------------------------------------------------------------------------------------\n\n")
    
    print("The amount that you will have to repay each month on your home loan is: ", repayment, "\n\n")
    
    print("------------------------------------------------------------------------------------------------")
    

else:
    
    print("Please either enter investment or bond!")