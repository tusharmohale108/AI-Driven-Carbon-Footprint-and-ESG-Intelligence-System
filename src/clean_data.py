import pandas as pd;

data = {
    "vendor" : ["TATA", "SOLID", "HP", "RELIANCE", "BAJAJ", "HP", "SOLID"],
    "industry" : ["steel", "iron", "Feul" , "electricity", "finace", "Feul", "iron"],
    "activites" : [400, None, 600, 500, None, 600, None ],
    "emission_factor": [2.5, 5, None, 2, 1.2, None, 5]
}

df = pd.DataFrame(data)

print(df)
print("\ninfo\n")
df.info()

print("\n")
print(df.isnull())
print("\n")
print(df.isnull().sum())

print("\n")

clean_df = df.dropna()
print(clean_df)
print("\n")

df["activites"] = df["activites"].fillna(0)
print(df)

print("\n")

df["emission_factor"] = df["emission_factor"].fillna(df["emission_factor"].mean())
print(df)
print()

df= df.drop_duplicates()
print(df)
print("\n")

df["emission"] = df["activites"]*df["emission_factor"]
print(df)

print("\nTotal emission = ", df["emission"].sum())
print(df.dtypes)

df.to_csv("clean_data.csv", index = False)