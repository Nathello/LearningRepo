import pandas as pd

query = "SELECT * FROM DWInternal.DimUser"

user_table = pd.read_sql_query(query, conn)

print(user_table.head())

age_range_count = dict()

unique_age_range = user_table["ageRange"].value_counts().index

for age in unique_age_range:
    user_count = user_table["dimUserId"][user_table["ageRange"] == age].count()
    age_range_count[age] = user_count
    

print(age_range_count)