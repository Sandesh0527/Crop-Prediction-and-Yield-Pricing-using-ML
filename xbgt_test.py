import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle


class XgbtTest:

    def __init__(self):
        self.file1 = "RF_Crop.pkl"
        self.df = pd.read_csv('dataset/croppred.csv')
        self.cropsDict = dict()
        self.load_model()

    def get_key(self, val):
        for key, value in self.cropsDict.items():
            if val == value:
                return key

    def load_model(self):
        crops = self.df['Crop'].unique()
        crops = [crop for crop in crops]
        i = 0
        for crop in crops:
            i += 1
            self.cropsDict[crop] = i
        self.df['Crop'] = [self.cropsDict.get(crop) for crop in self.df['Crop']]

    def xgbt_Predict(self, rainfall, temp, ph):
        c1 = []
        model = pickle.load(open(self.file1, "rb"))
        print(rainfall, temp, ph)
        Xnew = np.array([[rainfall, temp, ph]]).reshape((1, -1))
        print(Xnew)
        predictions = model.predict(Xnew)
        pred1 = model.predict_proba(Xnew)
        pred2 = pred1
        pred2 = pred2[0].tolist()
        pred1[0].sort()
        pred1[0] = pred1[0][::-1]
        pred1 = pred1[0].tolist()

        print(pred1)
        print(predictions)
        print(pred2)

        for i in range(0, 3):
            a1 = pred2.index(pred1[i])
            a1 += 1
            c1.append(self.get_key(a1))
        print(c1)
        return c1


if __name__ == "__main__":
    crop = []
    rainfall = 550
    temperature = 15
    ph = 6
    model = XgbtTest()
    crop = model.xgbt_Predict(rainfall, temperature, ph)
    print("Best suitable top three crop is :", crop)
