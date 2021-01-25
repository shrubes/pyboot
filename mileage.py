print("How many kilometers did you cycle today?")
kms = input()
miles = float(kms) / 1.609344
miles = round(miles, 2)
print(f"Ok, so you cycled {miles} miles")
