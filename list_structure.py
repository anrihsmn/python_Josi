
# create a list food that safe for your patients.
#at least 5 items
safe_food =['tomato','tofu','meat','cabbage','coffee']

print(safe_food)
safe_food.insert(1,'rice')
# safe_food.remove('cabbage')
# safe_food.remove(safe_food[1])
print(safe_food)

# create 3 dictionaries with patient information
# 3 entries

patient_information1 = {'name':'Anri','age':30,'disease':'diabetes_mellitus'}
patient_information2 = {'name':'Josiah','age':27,'disease':'heartattack'}
patient_information3 = {'name':'Tomomi','age':35,'disease':'kidney_failure'}

print(patient_information1)
print(patient_information2)
print(patient_information3)

patient_information1 = {'name':'Josiah','age':27}
patient_information2 = {'name':'Anri','age':30}
# patient_information3 = {}

# print(patient_information1['name'],patient_information1['age'])
# print(patient_information2['name'],patient_information2['age'])
print(patient_information1)

# modify or add
patient_information1['name'] = 'Tsukuru'
patient_information1['age'] = 29
patient_information1['room']= "32B"
patient_information1['allergen'] = "flowers"

# delete
del patient_information1['allergen']

print(patient_information1)
# print(patient_information1['name'],patient_information1['age'])
# print(patient_information2['name'],patient_information2['age'])