def emission_calculator(activity, factor):
    return activity*factor

act = int(input("Activity : "))
factor = float(input("Emission factor : "))
Emission = emission_calculator(act, factor)

print("\nEstimated emission  = ", Emission, "kg CO2")