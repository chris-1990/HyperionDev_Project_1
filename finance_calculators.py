import math

#Request user input to select either Investment or Bond
print("investment 	- to calculate the amount of interest you'll earn on your investment")
print("bond 		- to caluclate the amount you'll have to pay on a home loan")
loan = input("Choose either 'investment' or 'bond' from the menu below to proceed: ")

#Variable declared for total
total = 0

if loan.lower() == "investment":
	amount = float(input("Please enter the amount you are depositing: "))
	interest_rate = float(input("Please enter the interest rate %: "))
	num_of_years = float(input("Please enter the number of years you plan on saving: "))
	interest = input("Would you like Simple or Compound interest: ")	
	if interest.lower() == "simple":
		interest_percent = interest_rate / 100
		total = amount*(1+interest_percent*num_of_years)
		print(f"The total amount when Simple interest is applied is R{round(total,2)}")
	elif interest.lower() == "compound":
		interest_percent = interest_rate / 100
		total = amount*math.pow((1+ interest_percent),num_of_years)
		print(f"The total amount when compound interest is applied is R{round(total, 2)}")
	else:
		print("Please enter a correct value")

elif loan.lower() == "bond":
	house_value = float(input("Please enter present Value of your house: "))
	interest_rate = float(input("Please enter the interest rate %: "))
	months = int(input("Please enter the number of months you plan to make repayments: "))
	monthly_interest = interest_rate / 12
	
	total = (monthly_interest*house_value)/(1-(1+monthly_interest)**(-months))
	print(f"You will need to repay each month: R{round(total,2)}")

else:
	print("Please enter a correct value")
		
		