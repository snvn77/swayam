# Smart Discount Calculator:

# A retail store introduces a Smart Discount Calculator to ensure that discounts are applied in a consistent and predictable manner. Every bill is processed by following a fixed logical sequence. Once a condition is satisfied, the system proceeds forward without revisiting previous checks.

# Purchase Amount Based Discount  
# If the total purchase amount is less than ₹1,000, no discount is applied.
# If the total purchase amount is ₹1,000 or more, a 10% purchasebased discount becomes eligible.
# Only one purchase-amount condition is checked. After this step, the system moves to customer evaluation.

# Customer Type Based Discount 
# If the customer is a regular customer, no customer-type discount is considered.
# If the customer is a premium customer, the system checks whether the purchase amount is at least ₹2,000.
# If the customer is premium and the purchase amount is below ₹2,000, the premium discount is ignored.
# If the customer is premium and the purchase amount is ₹2,000 or more, a 5% premium discount becomes eligible. 

# Final Discount Selection Rule
# If no discount is eligible from either scheme, the final payable amount remains equal to the purchase amount.
# If exactly one discount is eligible, that discount is applied.
# If both purchase-based and premium discounts are eligible, the system compares the discount values and applies only the one that results in the higher benefit.
# At no point are both discounts applied together.

# Safety Rules 
# If the calculated discount exceeds the purchase amount, the discount is limited to the purchase amount.
# If the final payable amount becomes negative, it is reset to zero.

# Output Generation
# The system displays the original purchase amount, the selected discount, and the final payable amount.
# The calculator always produces the same output for the same input, ensuring fairness and transparency in billing. 


# A customer is a regular customer and makes a purchase of ₹850. Which code fragment correctly represents the discount logic applied by the calculator?
    # discount = 0
    # if amount>=1000:                  (Right Answer)
    #     discount = amount*0.10

    # if amount<1000:
    #     discount=amount*0.10
    # else:
    #     discount=0 

    # discount=amount*0.10 

    # if amount>1000:
    #     discount=0


# A premium customer makes a purchase of ₹1,500.
# Which discount will the system finally apply?
#  5% premium discount
#  No discount
#  10% purchase-based discount  (Right Answer)
#  Both 10% and 5% discounts


# A premium customer makes a purchase of ₹2,500.
# Which logic ensures that only one discount is applied?
    # discount=amount*0.10+amount*0.05
    
    # discount = max(amount*0.10,amount*0.05)     (Right Answer)
    
    # if premium:
    #     discount = amount*0.05
    # discount=amount*0.10

    # if premium and amount>2000:
    #     discount = amount*0.05


# A premium customer makes a purchase of ₹2,000 exactly.
# Which discount amount is applied?
#  ₹100
#  ₹200 (Right Answer)
#  ₹300
#  ₹0


# A premium customer makes a purchase of ₹1,800.
# Which of the following code fragments correctly produces the
# discount applied by the Smart Discount Calculator?
 # if premium:
    #     discount = amount*0.05

    # if amount>=2000:
    #     discount = amount*0.10

    # if premium and amount>=2000:
    #     discount = amount*0.05
    # else:
    #     discount = 0
    
    # if premium and amount>=2000:
    #     discount = amount*0.05
    # elif amount>=1000:                   (Right Answer)
    #     discount = amount*0.10
 