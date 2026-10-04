import pandas as pd

data = {
    "vendor": ["TATA", "SOLID", "HP", "RELIANCE", "BAJAJ", "INFOSYS", "WIPRO", "L&T"],
    "industry": ["Steel", "Iron", "Fuel", "Electricity", "Finance", "IT", "IT", "Engineering"],
    "activity": [400, 200, 600, 500, 300, 700, 450, 550],
    "emission_factor": [2.5, 5, 3, 2, 1.2, 0.5, 0.6, 1.8]
}

df = pd.DataFrame(data)

df["emission"] = df["activity"] * df["emission_factor"]

print(df)

print("\nTotal emission = ", df["emission"].sum())

largest = df.loc[df["emission"].idxmax()]
print("\nlargest emisson : ")
print(largest)

smallest = df.loc[df["emission"].idxmin()]
print("\nsmallest emisson : ")
print(smallest)

sort_df = df.sort_values("emission", ascending= False)
print("\n sorted :\n", sort_df)

total = df["emission"].sum()
df["contribution"] = (df["emission"]/total)*100

print("\ncontribution: ")
print(df)

def classification(emission):
    if(emission > 1000):
        return "High"
    elif(emission < 500):
        return "Low"
    else:
        return "Medium"



print("\nemission level addded")
df["emission_lvl"] = df["emission"].apply(classification)
print(df)

print("\n vendor count per emission level")
vendor_count = df.groupby("emission_lvl")["vendor"].count()
print(vendor_count)