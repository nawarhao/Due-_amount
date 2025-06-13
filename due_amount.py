def calculate_change(total_bill, amount_paid):
    change = amount_paid - total_bill
    return change

# Example usage
returned_amount = calculate_change(2.50, 4.00)
print("The shopkeeper should return $", returned_amount)
