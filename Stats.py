import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import random
import numpy as np

class Stat:

    def __init__(self, file2):
        self.name = file2
        df = pd.read_csv(file2)
        self.X = df.iloc[:, :-1].values
        self.y = df.iloc[:, 3].values
        self.reg = DecisionTreeRegressor(max_depth=random.randrange(7, 18))
        self.reg.fit(self.X, self.y)

    def pred(self,values):
        pp = np.array(values).reshape(1, 3)
        return self.reg.predict(pp)[0]

    def returnName(self):
        a = self.name.split('.')
        return a[0]


    # a = Stat('dataset/Wheat.csv')
    # a = a.pred()

