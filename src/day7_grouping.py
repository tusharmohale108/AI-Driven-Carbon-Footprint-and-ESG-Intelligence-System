import pandas as pd

data = {
    "vendor": ["TATA", "SOLID", "HP", "RELIANCE", "BAJAJ", "INFOSYS", "PETROLOUUS", "INDIANGAS"],
    "industry": ["Steel", "Iron", "Fuel", "Electricity", "Finance", "Electricity", "Fuel", "Fuel"],
    "activity": [400, 200, 600, 500, 300, 700, 500, 550],
    "emission_factor": [2.5, 5, 3, 2, 1.2, 0.8, 2.1, 2.5]
}

df = pd.DataFrame(data)

print(df)
print("\n")
df["emission"] = df["activity"]*df["emission_factor"]

Total_emission = df["emission"].sum()
print("Total emission = ", Total_emission)

print("\nTotal emission by industry\n")

industry_emission = df.groupby("industry")["emission"].sum()
print(industry_emission)

print("\nAverage emission by industry\n")
average_emission = df.groupby("industry")["emission"].mean()
print(average_emission)

print("\nNumber of vendor in industry\n")
vendor_count = df.groupby("industry")["vendor"].count()
print(vendor_count)

print("\nsorted data by emission\n")
sorted_data = df.sort_values("emission", ascending=False)
print(sorted_data)

print("\nHighest emission vendor: \n")
highest = df.loc[df["emission"].idxmax()]
print(highest)