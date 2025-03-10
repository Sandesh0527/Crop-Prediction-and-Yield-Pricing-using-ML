#importing all required packages
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle


file_name = "RF_Crop.pkl"

#Read the dataset
df = pd.read_csv('dataset/croppred.csv')

#Encoding Crop in dictionary Eg {'Bajra':1}
crops = df['Crop'].unique()
crops = [crop for crop in crops]
i=0
cropsDict = dict()
for crop in crops:
    i +=1
    cropsDict[crop] = i
df['Crop'] = [cropsDict.get(crop) for crop in df['Crop']]


#Creating x,y Variable x = [rainfall,temp,ph] y = [crop] from csv
x = df.iloc[:,[0,1,2]].values
y = df.iloc[:,3].values

#Creating training and testing dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.4, random_state = 12345)

#Creating xgboost model
# from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
# model = XGBClassifier(objective="multi:softprob", random_state=42)
model = RandomForestClassifier()
model = model.fit(x_train,y_train)
#Saving the model
pickle.dump(model, open(file_name, "wb"))

print("-------------------")
acc = accuracy_score(y_train,model.predict(x_train))
print(f" Accuracy over training data is : {acc*100} %")

acc = accuracy_score(y_test,model.predict(x_test))
print(f" Accuracy over testing data is : {acc*100} %")

