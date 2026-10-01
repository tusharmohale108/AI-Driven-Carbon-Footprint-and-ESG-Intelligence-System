import pandas as pd

data = {
    "vendor": ["TATA", "SOLID", "HP", "RELIANCE"],
    "industry": ["Steel", "Iron", "Fuel", "Electricity"],
    "activity" : [400, 200 , 800, 1200],
    "emission_factor" : [0.5, 1.2, 2.5, 0.8]
}

df = pd.DataFrame(data)

print("DATA\n")
print(df)


df["emission"] = df["activity"]*df["emission_factor"]

print("\nEmission")
print(df["emission"])

print("\nTotal activity = ", df["activity"].sum())
print("\nAverage activity = ", df["activity"].mean())
print("\nTotal emission = ", df["emission"].sum())

contraint = df[df["activity"] > 300]

print("\n activites > 300", contraint)

df.to_csv("vendor_data.csv", index= False)