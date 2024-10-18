# File: expense_tracker.py

import csv
from datetime import datetime

class Expense:
    def __init__(self, amount, description, category, date=None):
        self.amount = amount
        self.description = description
        self.category = category
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def __str__(self):
        return f"{self.date} | {self.category} | {self.description} | ${self.amount:.2f}"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description, category, date=None):
        expense = Expense(amount, description, category, date)
        self.expenses.append(expense)
        print("Expense added successfully.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        print("\nAll Expenses:")
        for expense in self.expenses:
            print(expense)

    def view_expenses_by_category(self, category):
        filtered_expenses = [exp for exp in self.expenses if exp.category == category]
        if not filtered_expenses:
            print(f"No expenses found in the '{category}' category.")
            return
        total = sum(exp.amount for exp in filtered_expenses)
        print(f"\nExpenses in category '{category}':")
        for expense in filtered_expenses:
            print(expense)
        print(f"Total for '{category}': ${total:.2f}")

    def export_expenses_to_csv(self, file_name="expenses.csv"):
        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])
            for expense in self.expenses:
                writer.writerow([expense.date, expense.category, expense.description, f"${expense.amount:.2f}"])
        print(f"Expenses exported to {file_name}")

# Command-Line Interface
def main_menu():
    tracker = ExpenseTracker()

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. Export Expenses to CSV")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                description = input("Enter description: ")
                category = input("Enter category: ")
                tracker.add_expense(amount, description, category)
            except ValueError:
                print("Invalid input. Amount should be a number.")
        
        elif choice == '2':
            tracker.view_expenses()
        
        elif choice == '3':
            category = input("Enter category: ")
            tracker.view_expenses_by_category(category)
        
        elif choice == '4':
            file_name = input("Enter the filename (default: expenses.csv): ") or "expenses.csv"
            tracker.export_expenses_to_csv(file_name)
        
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main_menu()
