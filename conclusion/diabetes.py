import pandas as pd
from sklearn.ensemble import RandomForestRegressor
diabetes_path = "C:/Users/Harshith/OneDrive/Desktop/python internship/conclusion/data/diabetes.csv" #add path here

diabetes_data = pd.read_csv(diabetes_path)
#diabetes_data.describe()

#defining the parameters to be considered to make a prediction
attributes = ['Age', 'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin'] #ADD BMI AT THE END
y = diabetes_data.Outcome
X = diabetes_data[attributes]

#defining and fitting the model
diabetes_model = RandomForestRegressor(random_state=1)
diabetes_model.fit(X,y)

Val = [] #empty list to input values

#inputting age
while True:
    age = input("Enter age: ")
    if age.isdigit():
        break
    else:
        print("Invalid input")
print(f"Age: {age}")
Val.append(age)

#checking for pregnancy and number of pregnancies
while True:
    pregnancy = input("Did you have any pregnancies: ")
    if pregnancy.isalpha() and pregnancy.lower() == "yes":
        while True:
            pregnancy_count = input("Number of times: ")

            if pregnancy_count.isdigit():
                #number = float(user_input)
                break
            else:
                print("Invalid input, Try again")
        break
    elif pregnancy.lower() == "no":
        pregnancy_count = 0
        break
    print("invalid input")
print(f"Pregnancy: {pregnancy.lower()}")
print(f"pregnancy count: {pregnancy_count}")

Val.append(pregnancy_count)

#inputting glucose level
while True:
    glucose_level = input("Enter your glucose level: ")
    if glucose_level.isdigit():
        break
    else:
        print("Invalid input")
print(f"glucose level: {glucose_level}")
Val.append(glucose_level)

#inputting Blood pressure
while True:
    Blood_pressure = input("Enter your blood pressure: ")
    if Blood_pressure.isdigit():
        break
    else:
        print("Invalid input")
print(f"Blood pressure: {Blood_pressure}")
Val.append(Blood_pressure)

#inputting skin thickness
while True:
    Skin_thickness = input("Enter skin thickness: ")
    if Skin_thickness.isdigit():
        break
    else:
        print("invalid input")
print(f"Skin thickness: {Skin_thickness}")
Val.append(Skin_thickness)

#inputting insulin level
while True: 
    insulin = input("Enter insuling level: ")
    if insulin.isdigit():
        break
    else:
        print("Invalid input")
print(f"Insuling level: {insulin}")
Val.append(insulin)

#BMI VALUES TO BE ADDED HERE AND APPENDED
#Val.append(BMI)

val_df = pd.DataFrame({'Age': [int(Val[0])],
                       'Pregnancies': [int(Val[1])],
                       'Glucose': [int(Val[2])],
                       'BloodPressure': [int(Val[3])], 
                       'SkinThickness': [int(Val[4])],
                       'Insulin': [int(Val[5])]
                       #,'BMI': [int(Val[6])] uncomment when BMI has been added
                       })

pred_diab = float(diabetes_model.predict(val_df))
print(f"presence percentage of Diabetes {pred_diab*100} %")