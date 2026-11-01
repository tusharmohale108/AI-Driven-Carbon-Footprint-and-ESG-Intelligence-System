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

df["emission"] = df["activity"]*df["emission_factor"];
print(df)

print("current tatal emission = ", df["emission"].sum())

df["reduce_emission"]  = df["emission"]*0.8
print(df[["vendor", "emission", "reduce_emission"]])

df["emission_saved"] = df["emission"] - df["reduce_emission"]
print("Total emission saved = ", df["emission_saved"].sum())
print("new Total emission = ", df["reduce_emission"].sum())


priority_vendor = df.sort_values("emission_saved", ascending= False)

print(priority_vendor);

plt.bar(df["vendor"], df["emission"], label = "Before")
plt.bar(df["vendor"], df["reduce_emission"], label = "After")
plt.xlabel("Emission")
plt.ylabel("Vendor")
plt.title("Before vs After Reduction")
plt.legend()
plt.show()