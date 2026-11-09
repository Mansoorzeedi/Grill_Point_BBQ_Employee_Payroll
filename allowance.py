# Allowance Allocation for Employees

def calculate_allowance(employee_id):
    if employee_id in ["GP001", "GP002"]:

        rent = 5000
        transport = 3000
        medical = 30000

    else:
        rent = 3000
        transport = 2000
        medical = 2000

        total = rent + transport + medical

        return {
            "Rent Allowance": rent,
            "Transport Allowance": transport,
            "Medical Allowance": medical,
            "Total": total
        }