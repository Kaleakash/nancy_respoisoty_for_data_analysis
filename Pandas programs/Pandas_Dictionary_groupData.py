import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Chanu", "David", "Eva", "Frank"],
    "Salary": [50000, 60000, 54000, 80000, 70000, 65000],
    "Department": ["HR", "Finance", "IT", "Finance", "Marketing", "IT"]
}
df = pd.DataFrame(data)
# grouped = df.groupby("Department")
# print(grouped)
groupedBySumSalary = df.groupby("Department")["Salary"].sum();
print(groupedBySumSalary)
groupedByAvgSalary = df.groupby("Department")["Salary"].mean();
print(groupedByAvgSalary)
groupedByMaxSalary = df.groupby("Department")["Salary"].max();
print(groupedByMaxSalary)
groupedByMinSalary = df.groupby("Department")["Salary"].min();
print(groupedByMinSalary)
groupedByCount = df.groupby("Department")["Salary"].count();
print(groupedByCount)