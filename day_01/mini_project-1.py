#Bill - Split Calculator
print("Bill Split Calculator")
bill_amount = float(input())
tip_percentage = float(input())
customer = int(input())
tip_amount = (tip_percentage / 100) * bill_amount
total = bill_amount + tip_amount
print(f"Total (including tip): ${total}")
amount_per_person = total / customer
print(f"Each person pays: ${amount_per_person}")
