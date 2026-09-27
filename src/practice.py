from carbon_calculator import emission_calculator

emission_calculator(300, 0.5)

def calculate_total(activities):
    sum = 0
     
    for act in activities:
        try:
            sum += act
        except:
            print("invalid activities")
    

    return sum

activitieslist = [100, 200, 'haribol', 300 , 400, 500]

total = calculate_total(activitieslist)
print("total activities = ", total)

def check_emission(emision):
    try :
        print("High emission") if emision > 400 else print("Low emission")
    except:
        print("Invalid output")

check_emission(300)
check_emission('haribol')
check_emission(400)
check_emission(500)

vendor = [
    {
        "name": "Tata steel",
        "size": "80",
        "industry": "Steel",
        "annual_spend": 1000000,
        "geography": "Pune"
    },
    {
        "name": "Adani",
        "size": "100",
        "industry": "iron",
        "annual_spend": 500000,
        "geography": "Mumbai"
    },
    {
        "name": "harekrishna",
        "size": "108",
        "industry": "packing",
        "annual_spend": 10000,
        "geography": "Pune"
    }
]
i = 0;
while(i < len(vendor)):
    for key in ['name', 'industry', 'annual_spend']:
        print(f"{key} : {vendor[i][key]}")
    i += 1
    print()