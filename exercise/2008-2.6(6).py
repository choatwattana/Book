"""
Program: taxform.py
Project 2.6
Compute a person's income tax.
1. Significant constants
       tax rate
       standard deduction
       deduction per dependent
2. The inputs are
       gross income
       number of dependents
3. Computations:
       net income = gross income - the standard deduction -
                    a deduction for each dependent
       income tax = is a fixed percentage of the net income
4. The outputs are
       the income tax, rounded to two figures
"""

# Initialize the constants
Tax_Rate = 0.20
Standard_Deduction = 10000.0
Dependent_Dependent = 3000.0

# Request the inputs
Gross_Income = float(input("Enter the gross income: "))
Number_Dependents = int(input("Enter the number of dependents: "))

# Compute the income tax
net_income = Gross_Income - Standard_Deduction - (Dependent_Dependent * Number_Dependents)
Income_Tax = net_income * Tax_Rate

# Display the income tax
print("The income tax is ฿" + str(round(Income_Tax, 2)))