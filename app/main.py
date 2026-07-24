from employee import Employee

employees = []

jake = Employee("Jake", "Doe", 25, 1234, "Manager")
jill = Employee("Jill", "Doe", 25, 1235, "Assistant Manager")
employees.append(jake)
employees.append(jill)


# search employee by id
def search_employee_by_id(employee_id):
    for employee in employees:
        if employee.employee_id == employee_id:
            return employee
    return None


# clock in employee
def clock_in_employee():
    employee_id = int(input("Enter the employee ID: "))
    searched_employee = search_employee_by_id(employee_id)

    if not searched_employee:
        print("Employee not found.")
        return

    searched_employee.clock_in()


# clock out employee
def clock_out_employee():
    employee_id = int(input("Enter the employee ID: "))
    searched_employee = search_employee_by_id(employee_id)

    if not searched_employee:
        print("Employee not found.")
        return

    searched_employee.clock_out()


def call_off_employee():
    employee_id = int(input("Enter the employee ID: "))
    searched_employee = search_employee_by_id(employee_id)

    if not searched_employee:
        print("Employee not found.")
        return

    searched_employee.call_off()


def display_menu():
    print("==== Zoo Ops Menu ====")
    print("1. Clock In Employee")
    print("2. Clock Out Employee")
    print("3. Call Off Employee")
    print("4. Employee List")
    print("5. Exit")


display_menu()

choice = input("Choose an option: ")
if choice == "1":
    clock_in_employee
elif choice == "2":
    clock_out_employee
elif choice == "3":
    call_off_employee
elif choice == "4":
    print("Employee List:")

    print(employees.full_name())

elif choice == "5":
    print("Exiting Zoo Ops")

else:
    print("Invalid Input")
