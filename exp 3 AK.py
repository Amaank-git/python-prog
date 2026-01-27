basic_salary = int(input("enter the basic salary:"))
DA = basic_salary*0.70
TA = basic_salary*0.30
HRA = basic_salary*0.10
gross_salary = basic_salary + DA + TA + HRA
print("*****salary details*****")
print(f"dearness allowance is (DA)")
print(f"travel allowance is (TA)")
print(f"house rent allowance (HRA)")
print(f"gross salary is : (gross_salary)")
