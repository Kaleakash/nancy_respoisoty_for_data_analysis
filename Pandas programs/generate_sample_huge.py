# import pandas as pd
# import numpy as np

# np.random.seed(42)

# # create sample data 
# num_rows = 10000;
# data = {
#     "emp_id":range(1, num_rows + 1),
#     "emp_name": [f"Employee_{i}" for i in range(1, num_rows + 1)],
#     "age": np.random.randint(18, 65, size=num_rows),
#     "department": np.random.choice(["HR", "Finance", "Engineering", "Sales", "Marketing"], size=num_rows),
#     "salary": np.random.randint(30000, 120000, size=num_rows)
# }
# df = pd.DataFrame(data)
# #print(df.head(10))
# df.to_csv("sample_huge_employees.csv", index=False)

# import pandas as pd

# # Read the CSV file
# df = pd.read_csv("sample_huge_employees.csv")
# # Display the first few rows of the dataframe
# #print(df.head(10))
# # Display the sample data with condition as department = 'Engineering' 
# engineering_employees = df[df['department'] == 'Engineering']
# print(engineering_employees.head(10))


import pandas as pd
import numpy as np
from faker import Faker;
np.random.seed(42)
fake = Faker();
# # create sample data 
num_rows = 10000;
data = []
for i in range(1, num_rows + 1):
    name = fake.name()
    data.append({
        "emp_id": i,
        "emp_name": name,
        "emailId": name.replace(" ", "_").lower() + "@gmail.com",
        "age": np.random.randint(18, 65),
        "department": np.random.choice(["HR", "Finance", "Engineering", "Sales", "Marketing"]),
        "salary": np.random.randint(30000, 120000)
    })

df = pd.DataFrame(data)
#print(df.head(10))
df.to_csv("fake_employees.csv", index=False)