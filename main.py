# assign a variable to the list of temperatures
temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]

# 1. Calculate the minimum of the list and print the value using print()
temp_min = min(temperatures_C)
print(temp_min)

# 2. Calculate the maximum of the list and print the value using print()
temp_max = max(temperatures_C)
print(temp_max)

# 3. Items in the list that are greater than 70ºC and print the result
for i in range(len(temperatures_C)):
    if temperatures_C[i] >= 70:
        print(temperatures_C[i])

# 4. Calculate the mean temperature throughout the day and print the result

average = sum(temperatures_C)/len(temperatures_C)
print(average)

# 5.1 Solve the fault in the sensor by estimating a value

estimated_value = sum(temperatures_C)/23

# 5.2 Update of the estimated value at 03:00 on the list

temperatures_C[3] = estimated_value

print(temperatures_C)

# Bonus: convert the list of ºC to ºFarenheit

aux = 0
temperatures_F = []

for i in range(len(temperatures_C)):
     aux = 1.8 * temperatures_C[i] + 32
     temperatures_F.append(aux)

print(temperatures_F)

# Print True or False depending on whether you would change the cooling system or not

sum_temp = 0
hours_greater_70 = 0
aux = False

for i in range(len(temperatures_C)):
    if temperatures_C[i] >= 70:
        hours_greater_70 += 1
    else:
        hours_greater_70 = 0

    if hours_greater_70 > 4 or temperatures_C[i] > 80:
        aux = True
        break

    sum_temp += temperatures_C[i]

if aux or sum_temp/len(temperatures_C) > 65:
    print("True")
else:
    print("False")



