import pandas as pd;
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Age": [24, 30, 22, 35, 28, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "Score": [85.5, 90.0, 78.5, 88.0, 92.5, 80.0],
    "status": ["Single", "Married", "Single", "Married", "Single", "Married"],
    "Height_cm": [165, 180, 175, 170, 160, 185],
    "Weight_kg": [55, 80, 70, 75, 50, 90],
    "Occupation": ["Engineer", "Doctor", "Artist", "Lawyer", "Scientist", "Teacher"],
    "Experience_years": [2, 10, 1, 8, 5, 15],
    "Department": ["R&D", "Medical", "Arts", "Legal", "Research", "Education"]
}
# print(data)
# print(type(data))
df = pd.DataFrame(data);    # Convert dictionary to DataFrame
#print(df)               # Display the DataFrame 
#print(type(df))        # Display the type of df
#print(df.head())      # Display the first few rows of the DataFrame
#print(df.head(3))   # Display the first 3 rows of the DataFrame
#print(df.tail())      # Display the last few rows of the DataFrame
#print(df.tail(2))   # Display the last 2 rows of the DataFrame

#df.info()               # Display concise summary of the DataFrame

#print(df.describe())        # Display statistical summary of numerical columns

# adding new columns to the dataframe
#df["Country"] = ["USA", "USA", "USA","India","India","India"];
#print(df)

# adding new column with maths operations 
#df["Total_Score"]= df["Score"] + 5;
#print(df)

# dropping a existing column from dataframe
# df = df.drop("status", axis=1);
# print(df)


# filter with conditions. 
# filtered_df = df[df["Age"] > 25];
# print(filtered_df)

# filter with string values 
# filtered_status_df = df[(df["status"] == "Married")];
# print(filtered_status_df)

# multiple conditions filter
#multi_filtered_df = df[(df["Age"] > 25) & (df["City"] == "Los Angeles")];
# multi_filtered_df = df[(df["Age"] > 25) | (df["City"] == "Los Angeles")];
# print(multi_filtered_df)

# selecting specific columns like select id,name from Employees;
# selected_columns_df = df[["Name", "Age", "City"]];
# print(selected_columns_df)

# sorting the dataframe based on a column
# sorted_df = df.sort_values(by="Score", ascending=True);
# print("Ascending order by Score ",sorted_df)

# selected_columns_df = df[["Name", "Age", "Score"]];
# sorted_df = selected_columns_df.sort_values(by="Score", ascending=False);
# print("Descending order by Score \n",sorted_df)


