import pandas as pd


class Filter:
    def __init__(self):
        self.df = pd.read_csv("dataset/mainDBB1.csv")
        self.df2 = pd.read_csv("dataset/state.csv")

    def findCrops(self, stateName):
        new = self.df
        tmp = new[new["State_Name"] == stateName]
        return tmp["Crop"].unique()

    def findStates(self):
        new1 = self.df
        tmp1 = new1["State_Name"].unique()
        return tmp1

    def findSeason(self):
        new2 = self.df
        tmp2 = new2["Season"].unique()
        return tmp2

    # def findDistrict(self):
    #     new2 = self.df
    #     tmp3 = new2['District_Name'].unique()
    #     return tmp3

    def findDistrict(self):
        dv = self.df2
        # tmp1 = new2[new2['State_Name'] == text]
        # print(tmp1['District_Name'].unique())
        # return tmp1['District_Name'].unique()

        d = {}
        for i in dv["State_Name"].unique():
            d[i] = [dv["District_Name"][j] for j in dv[dv["State_Name"] == i].index]
        print(d)
        return d
