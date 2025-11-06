import pandas as pd
# Create the first DataFrame
employees = {
    'EmployeeID': [101, 102, 103, 104,105,106],
    'Name': ['Alice', 'Bob', 'Charlie', 'David','Eve','Frank'],
    'Department': ['HR', 'IT', 'Finance', 'IT','Sales',None]
}
departments = {
    'DepartmentID': [1, 2, 3,4,5],
    'DepartmentName': ['HR', 'IT', 'Finance',"Marketing","Sales"]
}
df_employees = pd.DataFrame(employees)
df_departments = pd.DataFrame(departments)  
print("Employees DataFrame:")
print(df_employees)
print("\nDepartments DataFrame:")
print(df_departments)
# Merge the two DataFrames on the Department column
merged_df_inner_join = pd.merge(df_employees, df_departments, left_on='Department', right_on='DepartmentName', how='inner')
print("-----------------------------------------------")
print("\nMerged DataFrame:")
print(merged_df_inner_join)
# Perform different types of joins
merged_df_left_join = pd.merge(df_employees, df_departments, left_on='Department', right_on='DepartmentName', how='left')
print("-----------------------------------------------")
print("\nLeft Join DataFrame:")
print(merged_df_left_join)
merged_df_right_join = pd.merge(df_employees, df_departments, left_on='Department', right_on='DepartmentName', how='right')
print("-----------------------------------------------")
print("\nRight Join DataFrame:")
print(merged_df_right_join)