# Write your code here!
def employee_print(employee_info):
    copiae= employee_info.copy()

    name = copiae.pop("Name", "N/A")
    salry = copiae.pop("Salary", "N/A")
    role = copiae.pop("Role", "N/A")
    print(f"Name: {name}")
    print(f"Salary: {salry}")
    print(f"Role: {role}")
    if copiae:
        for key,value in copiae.items():
            print(f"{key}: {value}")
    else:
        print("No other info!")
