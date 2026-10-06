import pandas as pd
import matplotlib.pyplot as plt

data = {
    "vendor": ["TATA", "SOLID", "HP", "RELIANCE",
               "BAJAJ", "INFOSYS", "WIPRO", "L&T"],

    "industry": ["Steel", "Iron", "Fuel", "Electricity",
                 "Finance", "IT", "IT", "Engineering"],

    "activity": [400, 200, 600, 500, 300, 700, 450, 550],

    "emission_factor": [2.5, 5, 3, 2, 1.2, 0.5, 0.6, 1.8]
}

df = pd.DataFrame(data)
df["emission"] = df["activity"]*df["emission_factor"]

print(df)

plt.bar(df["vendor"], df["emission"])
plt.xlabel("Vendor")
plt.ylabel("Total Emission")
plt.title("Vendor vs Emission")

for i in range(len(df)):
    plt.text(i, df["emission"].loc[i]+20, df["emission"].iloc[i])


plt.show()




industry_wise_emission = df.groupby("industry")["emission"].sum()
print(industry_wise_emission)

industry_wise_emission.plot(kind= "bar")
plt.xlabel("Industries")
plt.ylabel("Total Emission")
plt.title("Industry vs Emission")

for i in range(len(industry_wise_emission)):
    plt.text(i, industry_wise_emission.iloc[i]+20, industry_wise_emission.iloc[i])

plt.show()


plt.scatter(df["activity"], df["emission"])
plt.xlabel("Activities")
plt.ylabel("Emissions")
plt.title("Activities vs Emission")
for i in range(len(df)):
    plt.text(df["activity"].iloc[i], df["emission"][i] +10, df["emission"].iloc[i])

plt.show()