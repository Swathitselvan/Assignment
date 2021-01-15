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
    if int(bmi_value)<=int(18.4):
        print("Underweight with bmi value as {} ".format(bmi_value))
    elif int(bmi_value)>=int(18.5) and int(bmi_value)<=int(24.9):
        print("Normalweight with bmi value as {} ".format(bmi_value))
    elif int(bmi_value)>=int(25) and int(bmi_value)<=int(29.9):
        count+=1
        print("Overweight with bmi value as {} ".format(bmi_value))
    elif int(bmi_value)>=int(30) and int(bmi_value)<=int(34.9):
        print("Moderately obese with bmi value as {} ".format(bmi_value))
    elif int(bmi_value)>=int(35) and int(bmi_value)<=int(39.9):
        print("Severely obese with bmi value as {} ".format(bmi_value))
    elif int(bmi_value)>=int(40):
        print("Very severely obese with bmi value as {} ".format(bmi_value))
print("{} people are available in the range of overweight category".format(count))