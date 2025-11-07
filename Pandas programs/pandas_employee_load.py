import pandas as pd;
# read data from a CSV file into a DataFrame
df = pd.read_csv('employees.csv');
# display the first few rows of the DataFrame
#print(df.head(10));
# display the last few rows of the DataFrame
#print(df.tail(10));
# display summary information about the DataFrame
#print(df.info());
# display basic statistical details of the DataFrame
#print(df[["SALARY"]].describe());
# apply condition to filter row with salary 
# high_salary = df[df["SALARY"] > 15000];
# print(high_salary);
#group by department and calculate average salary
# avg_salary_by_dept = df.groupby("DEPARTMENT_ID")["SALARY"].mean();
# sum_salary_by_dept = df.groupby("DEPARTMENT_ID")["SALARY"].sum()
# max_salary_by_dept = df.groupby("DEPARTMENT_ID")["SALARY"].max()
# min_salary_by_dept = df.groupby("DEPARTMENT_ID")["SALARY"].min()
# count_by_dept = df.groupby("DEPARTMENT_ID")["SALARY"].count()
# print("Average Salary by Department:\n", avg_salary_by_dept);
# print("Sum Salary by Department:\n", sum_salary_by_dept);
# print("Max Salary by Department:\n", max_salary_by_dept);
# print("Min Salary by Department:\n", min_salary_by_dept);
# print("Count by Department:\n", count_by_dept);

# group by department and calculate average without decimals values 
# avg_salary_by_dept_no_decimal = df.groupby("DEPARTMENT_ID")["SALARY"].mean().astype(int);
# print("Average Salary by Department (No Decimals):\n", avg_salary_by_dept_no_decimal);

# find the highest salary in the company
highest_salary = df[df["SALARY"] >= 13000];
#print("Highest Salary in the Company:\n", highest_salary);
# store this in a new CSV file
highest_salary.to_csv('highest_salary.csv', index=False);
