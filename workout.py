jsondata=[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
{"Gender": "Female", "HeightCm": 191, "WeightKg": 52},
{"Gender": "Female", "HeightCm": 101, "WeightKg": 30}]
count=0
for data in jsondata:
    meterval=data['HeightCm']/100.0
    bmi_value=data['WeightKg']/meterval
    print(bmi_value)
    if int(bmi_value)<=int(18.4):
        print("Underweight")
    elif int(bmi_value)>=int(18.5) and int(bmi_value)<=int(24.9):
        print("Normalweight")
    elif int(bmi_value)>=int(25) and int(bmi_value)<=int(29.9):
        count+=1
        print("Overweight")
    elif int(bmi_value)>=int(30) and int(bmi_value)<=int(34.9):
        print("Moderately obese")
    elif int(bmi_value)>=int(35) and int(bmi_value)<=int(39.9):
        print("Severely obese")
    elif int(bmi_value)>=int(40):
        print("Very severely obese")
print("{} people are available in the range of overweight category".format(count))