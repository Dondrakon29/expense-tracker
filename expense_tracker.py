import json
from datetime import datetime 

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

        return expenses

    except FileNotFoundError:
        return []


expenses = load_expenses()


def show_menu():
    print("1 - Add expense")
    print("2 - Show expenses")
    print("3 - Show by category")
    print("4 - Delete expense")
    print("5 - Clear all expenses")
    print("0 - Exit")

def is_valid_date(date):

    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
def clear_expenses(expenses):
    if not expenses:
        print("No expenses to clear")
        return

    confirm = input("Are you sure? yes/no: ").strip().lower()

    if confirm != "yes":
        print("Clear cancelled")
        return

    expenses.clear()
    save_expenses(expenses)

    print("All expenses cleared")    

def add_expense(expenses):
    title = input("Enter title: ").strip()

    if not title:
        print("Title cannot be empty")
        return
    
    try:
        amount = int(input("Enter amount: "))
    except ValueError:
        print("Amount must be a number")
        return

    if amount <= 0:
        print("Amount must be greater than zero")
        return    
    
    category = input("Enter category: ").strip().capitalize()

    if not category:
        print("Category cannot be empty")
        return
    
    date = input("Enter date: ").strip()

    if not date:
        print("Date cannot be empty")
        return
    
    if not is_valid_date(date):
        print("Date must be in format YYYY-MM-DD")
        return
    
    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": date
    }    
    
    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added")

def print_expense(index, expense):
    print(f"{index}. {expense['title']} | {expense['amount']} | {expense['category']} | {expense['date']}")

def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total 

def filter_by_category(expenses, category):
    
    filtered_expenses = []

    for expense in expenses:
        if expense["category"] == category:
            filtered_expenses.append(expense)

    return filtered_expenses        


def show_expenses(expenses):
    if not expenses:
        print("No expenses yet")
        return
    
    print("Expenses:")
    
    total = 0
        
    for index, expense in enumerate(expenses, start=1):
        print_expense(index, expense)
        
    total = calculate_total(expenses)

    print("-" * 20)
    print("Total:", total)

def show_by_category(expenses):

    category = input("Enter category: ").strip().capitalize()
    print("Selected category:", category)

    filtered_expenses = filter_by_category(expenses, category)

    if not filtered_expenses:
        print("No expenses in this category")
        return        

    print("Expenses:")

    for index, expense in enumerate(expenses, start=1):
            print_expense(index, expense)
            
    total = calculate_total(filtered_expenses)        

    print("-" * 20)
    print("Total:", total)

def delete_expense(expenses):

    if not expenses:
        print("No expenses to delete")
        return
    
    show_expenses(expenses)

    try:
        number = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Number must be a number")
        return
    
    if number < 1 or number > len(expenses):
        print("Invalid expense number")
        return
    
    index = number - 1 
    deleted_expense = expenses.pop(index)

    save_expenses(expenses)

    print("Deleted:", deleted_expense["title"])


def run_app():
    while True:
        show_menu()

        choice = input("Choose option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_by_category(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            clear_expenses(expenses)                    
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Wrong choice")

        print()


if __name__ == "__main__":
    run_app()