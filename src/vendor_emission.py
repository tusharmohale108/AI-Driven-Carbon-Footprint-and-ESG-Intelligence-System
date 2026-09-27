from carbon_calculator import emission_calculator

vendor = [
    {
        "name" : "Tata steel",
        "size" : "large",
        "industry" : "steel",
        "annual_spend" : 100000,
        "activity": 400,
        "emission_factor": 2.5
    },

    {
        "name" : "SOLID",
        "size" : "medium",
        "industry" : "iron",
        "annual_spend" : 10000,
        "activity": 500,
        "emission_factor": 1.5
    },
    
    {
        "name" : "HP",
        "size" : "large",
        "industry" : "fuel",
        "annual_spend" : 500000,
        "activity": 800,
        "emission_factor": 5
    },
     
]

i =0 
while(i<len(vendor)):
    for key in ["name", "industry", "activity"]:
        print(f"{key}:{vendor[i][key]}")
    emission = emission_calculator(vendor[i]["activity"], vendor[i]["emission_factor"])
    print("emission = ", emission)
    i += 1
    print("____________________________________________") 