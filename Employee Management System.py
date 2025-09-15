#Employee Management System.py

employees = []  # List to store employee dictionaries

def add_employee():
    """Add a new employee."""
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    dept = input("Enter Department: ")
    salary = input("Enter Salary: ")

    employee = {
        'id': emp_id,
        'name': name,
        'department': dept,
        'salary': salary
    }

    employees.append(employee)
    print("\n Employee added successfully!\n")


def view_employees():
    """View all employees."""
    if not employees:
        print("\n No employees found.\n")
        return

    print("\n--- Employee List ---")
    for emp in employees:
        print(f"ID: {emp['id']}, Name: {emp['name']}, Department: {emp['department']}, Salary: {emp['salary']}")
    print()


def search_employee():
    """Search for an employee by ID."""
    emp_id = input("Enter Employee ID to search: ")
    for emp in employees:
        if emp['id'] == emp_id:
            print(f"\nEmployee Found: ID: {emp['id']}, Name: {emp['name']}, Department: {emp['department']}, Salary: {emp['salary']}\n")
            return
    print("\nEmployee not found.\n")


def delete_employee():
    """Delete an employee by ID."""
    emp_id = input("Enter Employee ID to delete: ")
    for emp in employees:
        if emp['id'] == emp_id:
            employees.remove(emp)
            print("\nEmployee deleted successfully!\n")
            return
    print("\nEmployee not found.\n")


def menu():
    """Display the main menu."""
    while True:
        print("--- Employee Management System ---")
        print("1. Add New Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            print("\nExiting Employee Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")



