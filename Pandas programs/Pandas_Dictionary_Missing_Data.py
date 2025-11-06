import pandas as pd
data = {
    "Name": ["Alice", "Bob", None, "David", "Eva", "Frank"],
    "Age": [24, None, 22, 35, 28, 40],
    "City": ["New York", "Los Angeles", "Chicago", None, "Phoenix", "Philadelphia"],
    "Score": [85.5, 90.0, None, 88.0, 92.5, 80.0],
    "status": ["Single", "Married", "Single", "Married", None, "Married"]
}
#print(data)
df = pd.DataFrame(data)    # Convert dictionary to DataFrame
print("Original DataFrame:")
print(df)
# Check for missing data
#print("\nMissing Data in DataFrame:")
#print(df.isnull())
# Handling missing data by filling with a specific value
print("---------------------------------------------")
df_filled = df.fillna({
    "Name": "Unknown",
    "Age": df["Age"].sum() / df["Age"].count(),
    "City": "Unknown",
    "Score": df["Score"].sum()/ df["Score"].count(),
    "status": "Unknown"
})
print("\nDataFrame after filling missing values:")
print(df_filled)
print("---------------------------------------------")
# Handling missing data by dropping rows with any missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped)