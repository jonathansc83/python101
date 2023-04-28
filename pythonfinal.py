import csv

# create a dictionary to store departments and their expenses
department_expenses = {}

# open the csv file and read the data
with open('city-of-seattle-2012-expenditures-dollars.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    # loop through the data and add expenses to the corresponding department's list
    for row in reader:
        department = row[0]
        expense_str = row[3]

        if expense_str:
            try:
                expenses = float(expense_str)
            except ValueError:
                if department == "Department":
                    print(f"Error: Could not convert {expense_str} to float for department {department}")
                    expenses = 0
                else:
                    print(f"Warning: Could not convert {expense_str} to float for department {department}")
                    expenses = 0
        else:
            expenses = 0
            print(f"Warning: Expense value missing for department {department}")

        if department not in department_expenses:
            department_expenses[department] = [expenses]
        else:
            department_expenses[department].append(expenses)

# iterate through the dictionary and sum up the expenses for each department
for department, expenses in department_expenses.items():
    total_expenses = sum(expenses)
    formatted_expenses = "${:.2f}".format(total_expenses)
    print(f"{department}: {formatted_expenses}")


import zipfile

# create a ZipFile object with a new zip file
with zipfile.ZipFile('city-of-seattle-2012-expenditures-dollars.zip', 'w') as zip_file:
    # add the csv file to the zip file
    zip_file.write('city-of-seattle-2012-expenditures-dollars.csv')
