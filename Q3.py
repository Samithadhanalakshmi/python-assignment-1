
# Online Shopping Discount Eligibility

# Get order amount and membership status
amount = float(input("Enter order amount: "))
membership = input("Are you a member? (yes/no): ")

# Convert membership into lowercase
membership = membership.strip().lower()

# Validate order amount
if amount < 0 or amount > 100000:
    print("Invalid Order Amount")

elif membership != "yes" and membership != "no":
    print("Invalid Membership Status")

else:
    # Determine discount percentage
    if amount >= 5000:
        discount_percentage = 15

    elif amount >= 2000 and amount < 5000 and membership == "yes":
        discount_percentage = 10

    else:
        discount_percentage = 0

    # Calculate discount and final amount
    discount_amount = amount * discount_percentage / 100
    final_amount = amount - discount_amount

    # Display the results
    print("Original Amount: Rs.", amount)
    print("Discount Percentage:", discount_percentage, "%")
    print("Discount Amount: Rs.", discount_amount)
    print("Final Payable Amount: Rs.", final_amount)

    if discount_percentage > 0:
        print("Eligibility Status: Eligible for discount")
    else:
        print("Eligibility Status: Not eligible for discount")
