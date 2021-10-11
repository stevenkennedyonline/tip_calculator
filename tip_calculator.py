#assigned 'meal' variale to capture user input for subtotal of check
meal = float(input("What is the subtotal for the check? "))

#assigned 'tip' variable to capture user input for desired tip amount
tip = int(input("What is your desired tip percentage? "))

#assigned 'tax' variable a value of 10 percent
tax = .10

#assigned variable to capture user input for number of people splitting the check
number_of_people = int(input("How many people are splitting the check? "))

#assigned 'tip_amt' variable  a value equaling the meal amount times tip divided by 100
tip_amt = (meal * (tip/100))

#assigned 'tax_amt' variable a value equaling the meal amount times tax
tax_amt = meal * tax

#assigned 'total' variable a value equaling the meal amount plus tip amount plus tax amount
total = meal + tip_amt + tax_amt    

#assigned 'split_amt' variable a value equaling the total check amount divided by the numer of people splitting the check
split_amt = total/number_of_people

#printed a line break
print("\n")

#printed a summary of the total check
print(f"\nSince the subtotal amount is ${meal:.2f}, the tax amount is ${tax_amt:.2f}, and the tip amount is ${tip:.2f}, the total check with tax and tip is ${total:.2f}.\n")

#printed how much each person should contribute to the check
print(f"Assuming all people will split the check evenly, each person should contribute ${split_amt:.2f} to the check.\n")