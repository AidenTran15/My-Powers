import sys


weight = input("enter your weight: (kg or lbs)")

if " " not in weight:
    print("Please have space between the number and unit in your input")
    sys.exit()


weightArr = weight.split()
weightNum = float(weightArr[0])
unit = weight[1]



if "kg" in weightArr:
    weight_lbs = weightNum /  0.45359237
    print(str(weight_lbs) + " lbs")
elif "lbs" in weightArr:
    weight_kg = weightNum *  0.45359237
    print(str(weight_kg) + " kg")
else:
    print("please check your unit again ")

