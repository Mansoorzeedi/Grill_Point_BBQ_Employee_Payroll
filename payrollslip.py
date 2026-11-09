# Payroll Calculation for Grill Point BBQ Employees

from allowance import calculate_allowance

def calculate_salary(Employees):
    basic = Employees["Basic Salary"]
    allowance = calculate_allowance(Employees["Employee ID"])
    tax = basic * 0.05
    gross_salary = basic + allowance["Total"]
    net_salary = gross_salary - tax

    return {
        "Basic" : basic,
        "Allowance" : allowance,
        "Gross Salary" : gross_salary,
        "Tax" : tax,
        "Net Salary" : net_salary
    }
