import numpy as np

activities = np.array([100, 200, 300, 400])
print(activities)

print(activities[0])
print(activities[1])
print(activities[-1])

print(activities[1:4])
print(activities[:3])
print(activities[2:])

print(activities*10)
print(activities+10)
print(activities/10)
print("\n")

print("Total sum =", np.sum(activities))
print("Average =", np.mean(activities))
print("Maximum =", np.max(activities))
print("Minimum =", np.min(activities))

print("\n")
print("====main====")
print("activities = ", activities)

emission_factor = 0.5

emission = activities * emission_factor

print("Total activities = ", np.sum(activities))
print("Emission = ", emission)
print("Total emission", np.sum(emission))
print("average emission = ", np.mean(emission))
print("\n")

print("\n=============1 year Data ============\n")

monthly_activities = np.array([230, 120, 200, 190, 290, 250, 300, 100, 150, 170, 270, 240])
monthly_emission = monthly_activities*emission_factor

print("Monthy activities =", monthly_activities)
print("monthly emission =", monthly_emission)
print("Total activities", np.sum(monthly_activities))
print("Total Emission=", np.sum(monthly_emission))
print("average activities =", np.mean(monthly_activities))
print("average emission = ", np.mean(monthly_emission))
print("maximum activite = ", np.max(monthly_activities))
print("maximum emission =", np.max(monthly_emission))
print("minimum activite = ", np.min(monthly_activities))
print("minimum emission =", np.min(monthly_emission))

print("\n=========END=========\n")