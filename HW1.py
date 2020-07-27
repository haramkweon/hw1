"""
Description : This program takes number of packages from user and calculate the total price which includes
discount rates.

Author: Haram Kweon
"""
# Creates while loop that is True , this makes the infinite while loop and it keeps asking user to enter right value.
while True:
    try:
        # Get the number of package from a user.
        number_of_package = float(input("Enter the number of packages ordered: "))

        # End while loop.
        break
    except ValueError:
        # print Error message
        print("Enter an integer for number of packages ordered. ")
        # continues to get right celsius value
        continue

# if number of packages is less than 10 discount rate is 0.
if number_of_package < 10:
    discount = 0
# if number of packages is between 10 to 19, the discount rate is 10%.
elif 10 <= number_of_package < 20:
    discount = 0.1
# if number of packages is between 20 to 49, the discount rate is 20%.
elif 20 <= number_of_package < 50:
    discount = 0.2
# if number of packages is between 50 to 99, the discount rate is 30%.
elif 50 <= number_of_package < 100:
    discount = 0.3
# if number of packages is not belong to any .
else :
    discount = 0.4

# Calculate the total cost of packages ordered.
total_cost = (100.00 * number_of_package)*(1-discount)

# Calculate the discount cost of packages ordered.
discount_cost = (100.00 * number_of_package) * discount

# Print the total cost of user purchased and discounts it shows until second digit of decimal point.
print("The total cost of your purchase was ", "$%0.02f" % total_cost, "with a discount of $", "$%0.02f" % discount_cost)