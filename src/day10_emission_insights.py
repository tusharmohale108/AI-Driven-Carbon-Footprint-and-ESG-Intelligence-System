import pandas as pd 


data = {
    "vendor": ["TATA", "SOLID", "HP", "RELIANCE",
               "BAJAJ", "INFOSYS", "WIPRO", "L&T"],

    "industry": ["Steel", "Iron", "Fuel", "Electricity",
                 "Finance", "IT", "IT", "Engineering"],

    "activity": [400, 200, 600, 500, 300, 700, 450, 550],

    "emission_factor": [2.5, 5, 3, 2, 1.2, 0.5, 0.6, 1.8]
}

print("\n data: \n")
df = pd.DataFrame(data)
print(df)

print("\n emission: \n")
df["emission"] = df["activity"]*df["emission_factor"]
print(df["emission"])

print("\n industry wise emission: \n")
industry_wise_emission = df.groupby("industry")["emission"].sum()
print(industry_wise_emission)

print("\n industry contributin percentage: \n")
total_emission = df["emission"].sum()
industry_contribution = (industry_wise_emission/total_emission)*100
print(industry_contribution.round(2)) 

print("\n Top 3 highest emission vendor : \n")
sort_df = df.sort_values("emission", ascending= False)
print(sort_df.head(3))

highest_idustry = industry_wise_emission.idxmax()
highest_emission = industry_wise_emission.max()
print("\n highest emission industry: ", highest_idustry)
print("\n highest industry emission: ", highest_emission)
