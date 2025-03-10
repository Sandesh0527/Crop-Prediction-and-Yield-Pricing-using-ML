# importing all required packages
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import r2_score
import pickle

# Read the dataset
df = pd.read_csv('dataset/1.csv', index_col='Crop_Year', converters={'Season': str.strip})
df = df.drop(['Unnamed: 0'], axis=1)
df = df[df['Production'].notna()]

# Encoding Crop in dictionary Eg {'Bajra':1}
crops = df['Crop'].unique()
crops = [crop for crop in crops]
i = 0
cropsDict = dict()
for crop in crops:
    i += 1
    cropsDict[crop] = i

df['Crop'] = [cropsDict.get(crop) for crop in df['Crop']]

season1 = df['Season'].unique()
season1 = [s for s in season1]
i = 0
seasonDict = dict()
for s in season1:
    i += 1
    seasonDict[s] = i

df['Season'] = [seasonDict.get(s) for s in df['Season']]

state1 = df['State_Name'].unique()
state1 = [s1 for s1 in state1]
i = 0
state1Dict = dict()
for s1 in state1:
    i += 1
    state1Dict[s1] = i

df['State_Name'] = [state1Dict.get(s1) for s1 in df['State_Name']]
#
district1 = df['District_Name'].unique()
district1 = [s1 for s1 in district1]
i = 0
dist1Dict = dict()
for s1 in district1:
    i += 1
    dist1Dict[s1] = i

df['District_Name'] = [dist1Dict.get(s1) for s1 in df['District_Name']]

X = df.drop("Production", axis=1)
y = df[["Production"]]
print(X)
print(y)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Creating xgboost model
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()
model.fit(X_train, y_train.values.ravel())
preds = model.predict(X_test)
# Saving the model
filename = 'RF_model.h5'
joblib.dump(model, filename)

print("-------------------")

r = r2_score(y_test, preds)
print("R2score when we predict using Randomn forest is ", r)
