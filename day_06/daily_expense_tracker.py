print("Welcome to the Daily Expense Tracker!")

print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")
expense_list = []
total_expense = 0
average_expense = 0
while True:
    choice = int(input())
   
    if choice == 1:
        another_choice = float(input())
        #expense_list += another_choice
        expense_list.append(another_choice)
        print("Expense added successfully!")
    elif choice == 2:
        if not expense_list:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for index, expense in enumerate(expense_list, start=1):
                print(f"{index}. {expense}")
    elif choice == 3:
        if not expense_list:
            print("No expenses recorded yet.")
        else:
            total_expense = sum(expense_list)
            average_expense = total_expense / len(expense_list)
            print(f"Total expense: {total_expense}")
            print(f"Average expense: {average_expense}")
    elif choice == 4:
        expense_list.clear()
        print("All expenses cleared.")
    elif choice == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")