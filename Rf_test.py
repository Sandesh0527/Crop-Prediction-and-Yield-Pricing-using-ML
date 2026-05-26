import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle


class RFTest:

    def __init__(self):
        self.filename = "RF_model.h5"
        self.df = pd.read_csv('dataset/1.csv',converters={'Season': str.strip})
        self.cropsDict = dict()
        self.seasonDict = dict()
        self.state1Dict = dict()
        self.dist1Dict = dict()
        self.load_model()

    def load_model(self):
        crops = self.df['Crop'].unique()
        crops = [crop for crop in crops]
        i = 0
        for crop in crops:
            i += 1
            self.cropsDict[crop] = i
        self.df['Crop'] = [self.cropsDict.get(crop) for crop in self.df['Crop']]
        # print(self.df['Crop'])

        season1 = self.df['Season'].unique()
        season1 = [season for season in season1]
        i = 0

        for season in season1:
            i += 1
            self.seasonDict[season] = i
        print("hi")
        self.df['Season'] = [self.seasonDict.get(season) for season in self.df['Season']]
        print(self.df['Season'])

        state1 = self.df['State_Name'].unique()
        state1 = [state for state in state1]
        i = 0
        for state in state1:
            i += 1
            self.state1Dict[state] = i

        self.df['State_Name'] = [self.state1Dict.get(state) for state in self.df['State_Name']]

        district1 = self.df['District_Name'].unique()
        district1 = [s1 for s1 in district1]
        i = 0
        for s1 in district1:
            i += 1
            self.dist1Dict[s1] = i

        self.df['District_Name'] = [self.dist1Dict.get(s1) for s1 in self.df['District_Name']]


    def RF_Predict(self, state, crop, season, district,area ):
        predictions=[]
        index = self.state1Dict.get(state)
        index2 = self.seasonDict.get(season)
        index3 = self.dist1Dict.get(district)
        model = joblib.load(self.filename)
        for i in range(0,3):
            print(crop[i])
            index1 = self.cropsDict.get(crop[i])
            print(index1)
            print(index, index1, index2, index3)

            Xnew = np.array([[index, index1, index2, index3, area]]).reshape((1, -1))
            #int(Xnew)
            prediction1 = model.predict(Xnew)
            prediction1 = prediction1.tolist()
            predictions.append(round(prediction1[0] * 1000000, 2))
            print(predictions)
        return predictions


if __name__ == "__main__":
    # Values taken from dataset/rainTempPh
    yeild=[]
    state = "Andhra Pradesh"
    crop = ['Bajra', 'Cowpea', 'Groundnut']
    season = "Kharif"
    district = "GUNTUR"
    # convert area to per 1000 hectare
    # 1 acre = 0.404686 ha
    # 1 acre = 0.000404686 per 1000 hectare
    area = 0.000404686

    model = RFTest()
    yeild = 0
    yeild = model.RF_Predict(state, crop, season, district, area)
    print(yeild)
    # print("kg", yeild)
    # print("Quintal", yeild / 100)
