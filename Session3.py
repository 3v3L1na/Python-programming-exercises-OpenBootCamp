def bodymassindex(height, weight):
    return round ((weight/height**2),2)

height=float (input('Enter your height in meters:'))
weight=float (input ('Enter your weight in kilos:'))

print('Welcome to the BMI calculator')

bmi=bodymassindex (height, weight)
print ('Your BMI is:', bmi)

if bmi <=18.5:
    print ('You are underweight.')
elif 18.5 < bmi <=24.9:
    print ('You have normal weight.')
else:
    print ('You are obese.')