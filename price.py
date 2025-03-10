from datetime import datetime
from Stats import Stat

base = {
    "Paddy": 1945.5,
    "Bajra": 1475,
    "Barley": 980,
    "Cotton": 4200,
    "Gram": 3000,
    "Groundnut": 3600,
    "Jowar": 1520,
    "Maize": 1175,
    "Moong": 3500,
    "Soyabean": 2200,
    "Sugarcane": 1700,
    "Wheat": 1550,
    "Coconut": 6000,
    "Chillies": 9000,
    "Turmeric": 8500,
    "Peas": 3300,
    "Potato": 2000,
    "Onion": 1600,
}
annual_rain = [29, 21, 37.5, 30.7, 52.6, 150, 299, 251.7, 179.2, 70.5, 39.8, 10.9]
prev_rainn = [10, 24, 30.5, 25.7, 42.6, 130, 360, 351.7, 229.2, 50, 40, 13]

lst1 = [
    "Wheat",
    "Paddy",
    "Barley",
    "Bajra",
    "Chillies",
    "Coconut",
    "Cotton",
    "Gram",
    "Groundnut",
    "Jowar",
    "Maize",
    "Moong",
    "Onion",
    "Peas",
    "Soyabean",
    "Sugarcane",
    "Turmeric",
    "Potato",
]


class price:
    def __init__(self):
        self.pred_list = []
        Wheat = Stat("dataset/Wheat.csv")
        self.pred_list.append(Wheat)
        Paddy = Stat("dataset/Paddy.csv")
        self.pred_list.append(Paddy)
        Barley = Stat("dataset/Barley.csv")
        self.pred_list.append(Barley)
        Bajra = Stat("dataset/Bajra.csv")
        self.pred_list.append(Bajra)
        Chilles = Stat("dataset/Chillies.csv")
        self.pred_list.append(Chilles)
        Coconut = Stat("dataset/Coconut.csv")
        self.pred_list.append(Coconut)
        Cotton = Stat("dataset/Cotton.csv")
        self.pred_list.append(Cotton)
        Gram = Stat("dataset/Gram.csv")
        self.pred_list.append(Gram)
        Groundnut = Stat("dataset/Groundnut.csv")
        self.pred_list.append(Groundnut)
        Jowar = Stat("dataset/Jowar.csv")
        self.pred_list.append(Jowar)
        Maize = Stat("dataset/Maize.csv")
        self.pred_list.append(Maize)
        Moong = Stat("dataset/Moong.csv")
        self.pred_list.append(Moong)
        Onion = Stat("dataset/Onion.csv")
        self.pred_list.append(Onion)
        Peas = Stat("dataset/Peas.csv")
        self.pred_list.append(Peas)
        Soyabean = Stat("dataset/Soyabean.csv")
        self.pred_list.append(Soyabean)
        Sugarcane = Stat("dataset/Sugarcane.csv")
        self.pred_list.append(Sugarcane)
        Turmeric = Stat("dataset/Turmeric.csv")
        self.pred_list.append(Turmeric)
        Potato = Stat("dataset/Potato.csv")
        self.pred_list.append(Potato)

    def cur_price(self, name):
        b = 0
        cur_month = datetime.now().month
        cur_year = datetime.now().year
        cur_rainfall = annual_rain[cur_month - 1]
        val = self.pred_list[0]
        b = lst1.index(name)
        val = self.pred_list[b]

        print("hi", val)
        cur_wpi = val.pred([float(cur_month), cur_year, cur_rainfall])
        cur_price = (base[name] * cur_wpi) / 100
        cur_price = round(cur_price, 2)
        # print(name)
        # print(self.pred_list)
        return cur_price

    def prevyear(self, name):
        b = 0
        cur_month = datetime.now().month
        cur_year = datetime.now().year
        cur_rainfall = prev_rainn[cur_month - 1]
        wpi1 = []
        crop1 = []
        month_year = []

        val = self.pred_list[0]
        b = lst1.index(name)
        val = self.pred_list[b]
        for i in range(1, 13):
            if cur_month - i >= 1:
                month_year.append(
                    (cur_month - i, cur_year, prev_rainn[cur_month - i - 1])
                )
            else:
                month_year.append(
                    (cur_month - i + 12, cur_year - 1, prev_rainn[cur_month - i + 11])
                )

        for m1, y1, r1 in month_year:
            cur_pred = val.pred([float(m1), y1, r1])
            wpi1.append(cur_pred)

        for i in range(0, len(wpi1)):
            m1, y1, r1 = month_year[i]
            x = datetime(y1, m1, 1)
            x = x.strftime("%b %y")
            crop1.append([x, round((wpi1[i] * base[name]) / 100, 2)])
        price1 = []
        for i in range(len(crop1) - 1, -1, -1):
            price1.append(crop1[i])
        return price1

    def priceyear(self, name):
        b = 0
        cur_month = datetime.now().month
        cur_rainfall = annual_rain[cur_month - 1]
        cur_year = datetime.now().year

        val = self.pred_list[0]
        b = lst1.index(name)
        val = self.pred_list[b]
        month_year = []
        for i in range(1, 13):
            if cur_month + i <= 12:
                month_year.append(
                    (cur_month + i, cur_year, annual_rain[cur_month + i - 1])
                )
            else:
                month_year.append(
                    (cur_month + i - 12, cur_year + 1, annual_rain[cur_month + i - 13])
                )

        min_v = 100000
        max_v = 0
        max1 = 0
        min1 = 0
        wpi1 = []
        bb = []

        cur_wpi = val.pred([float(cur_month), cur_year, cur_rainfall])

        for m, y, r in month_year:
            cur_predict = val.pred([float(m), y, r])
            if cur_predict > max_v:
                max_v = cur_predict
                max1 = month_year.index((m, y, r))
            if cur_predict < min_v:
                min_v = cur_predict
                min1 = month_year.index((m, y, r))
            wpi1.append(cur_predict)
            bb.append(((cur_predict - cur_wpi) * 100) / cur_wpi)

        max_m, max_y, r1 = month_year[max1]
        min_m, min_y, r2 = month_year[min1]
        min_v = min_v * base[name] / 100
        max_v = max_v * base[name] / 100
        crops_pr = []
        for i in range(0, len(wpi1)):
            m, y, r = month_year[i]
            x = datetime(y, m, 1)
            x = x.strftime("%b %y")
            crops_pr.append(
                [x, round((wpi1[i] * base[name]) / 100, 2), round(bb[i], 2)]
            )
        x = datetime(max_y, max_m, 1)
        x = x.strftime("%b %y")
        max_price = [x, round(max_v, 2)]
        x = datetime(min_y, min_m, 1)
        x = x.strftime("%b %y")
        min_price = [x, round(min_v, 2)]

        return max_price, min_price, crops_pr

    def firstfive(self):
        cur_month = datetime.now().month
        cur_year = datetime.now().year
        cur_rainfall = annual_rain[cur_month - 1]
        prev_month = cur_month - 1
        prev_rainfall = annual_rain[prev_month - 1]
        prev_month_pred = []
        cur_month_pred = []
        change1 = []

        for i in self.pred_list:
            cur_predict = i.pred([float(cur_month), cur_year, cur_rainfall])
            cur_month_pred.append(cur_predict)
            print(cur_predict)
            prev_predict = i.pred([float(prev_month), cur_year, prev_rainfall])
            prev_month_pred.append(prev_predict)
            change1.append(
                (
                    ((cur_predict - prev_predict) * 100 / prev_predict),
                    self.pred_list.index(i),
                )
            )
        sort1 = change1
        sort1.sort(reverse=True)
        top = []
        for j in range(0, 5):
            p, i = sort1[j]
            name = self.pred_list[i].returnName().split("/")[1]
            top.append(
                [name, round((cur_month_pred[i] * base[name]) / 100, 2), round(p, 2)]
            )

        return top

    def bottomfive(self):
        cur_month = datetime.now().month
        cur_year = datetime.now().year
        cur_rainfall = annual_rain[cur_month - 1]
        prev_month = cur_month - 1
        prev_rain = annual_rain[prev_month - 1]
        cur_month_pred = []
        prev_month_pred = []
        change1 = []

        for i in self.pred_list:
            cur_predict = i.pred([float(cur_month), cur_year, cur_rainfall])
            cur_month_pred.append(cur_predict)
            prev_predict = i.pred([float(prev_month), cur_year, prev_rain])
            prev_month_pred.append(prev_predict)
            change1.append(
                (
                    ((cur_predict - prev_predict) * 100 / prev_predict),
                    self.pred_list.index(i),
                )
            )
        sort1 = change1
        sort1.sort()
        bot = []
        for j in range(0, 5):
            p, i = sort1[j]
            name = self.pred_list[i].returnName().split("/")[1]
            bot.append(
                [name, round((cur_month_pred[i] * base[name]) / 100, 2), round(p, 2)]
            )
        # print(to_send)
        return bot

    def yeartopfive(self):
        # list = {"m1", "m2", "m3", "m4", "m5", "m6", "m7", "m8", "m9", "m10", "m11", "m12"}
        # m = (dict([(key, []) for key in list]))
        m = {}
        for i in range(1, 13):
            m["m{}".format(i)] = []
        for i in self.pred_list:
            crops = self.yeartopfive1(i.returnName())
            fr = 1
            for a in crops:
                time = a[0]
                price = a[1]
                change = a[2]

                m["m{}".format(fr)].append(
                    [change, price, i.returnName().split("/")[1], time]
                )
                fr += 1

        for a in range(1, 13):
            m["m{}".format(a)].sort()
        # print(m)
        # month_wise={
        #   'month_wise0' : [],
        #     'month_wise1': [],
        #     'month_wise2': [],
        #     'month_wise3': [],
        #     'month_wise4': []
        # }
        month_wise = []
        # 0 12 24 36 48

        for a in range(1, 13):
            month_wise.append(
                [
                    m["m{}".format(a)][0][3],
                    m["m{}".format(a)][len(m["m{}".format(a)]) - 1][2],
                    m["m{}".format(a)][len(m["m{}".format(a)]) - 1][0],
                    m["m{}".format(a)][len(m["m{}".format(a)]) - 1][1],
                    m["m{}".format(a)][len(m["m{}".format(a)]) - 2][2],
                    m["m{}".format(a)][len(m["m{}".format(a)]) - 2][0],
                    m["m{}".format(a)][len(m["m{}".format(a)]) - 2][1],
                    m["m{}".format(a)][len(m["m{}".format(a)]) - 3][2],
                    m["m{}".format(a)][len(m["m{}".format(a)]) - 3][0],
                    m["m{}".format(a)][len(m["m{}".format(a)]) - 3][1],
                    m["m{}".format(a)][len(m["m{}".format(a)]) - 4][2],
                    m["m{}".format(a)][len(m["m{}".format(a)]) - 4][0],
                    m["m{}".format(a)][len(m["m{}".format(a)]) - 4][1],
                    m["m{}".format(a)][len(m["m{}".format(a)]) - 5][2],
                    m["m{}".format(a)][len(m["m{}".format(a)]) - 5][0],
                    m["m{}".format(a)][len(m["m{}".format(a)]) - 5][1],
                    m["m{}".format(a)][0][2],
                    m["m{}".format(a)][0][0],
                    m["m{}".format(a)][0][1],
                    m["m{}".format(a)][1][2],
                    m["m{}".format(a)][1][0],
                    m["m{}".format(a)][1][1],
                    m["m{}".format(a)][2][2],
                    m["m{}".format(a)][2][0],
                    m["m{}".format(a)][2][1],
                    m["m{}".format(a)][3][2],
                    m["m{}".format(a)][3][0],
                    m["m{}".format(a)][3][1],
                    m["m{}".format(a)][4][2],
                    m["m{}".format(a)][4][0],
                    m["m{}".format(a)][4][1],
                ]
            )

        return month_wise

    def yeartopfive1(self, name):
        b = 0
        cur_month = datetime.now().month
        cur_year = datetime.now().year
        cur_rainfall = annual_rain[cur_month - 1]
        name = name.split("/")[1]
        val = self.pred_list[0]
        b = lst1.index(name)
        val = self.pred_list[b]
        month_year = []
        for i in range(1, 13):
            if cur_month + i <= 12:
                month_year.append(
                    (cur_month + i, cur_year, annual_rain[cur_month + i - 1])
                )
            else:
                month_year.append(
                    (cur_month + i - 12, cur_year + 1, annual_rain[cur_month + i - 13])
                )
        wpi1 = []
        cur_wpi = val.pred([float(cur_month), cur_year, cur_rainfall])
        bb = []

        for m, y, r in month_year:
            cur_predict = val.pred([float(m), y, r])
            wpi1.append(cur_predict)
            bb.append(((cur_predict - cur_wpi) * 100) / cur_wpi)

        cr_price = []
        for i in range(0, len(wpi1)):
            m, y, r = month_year[i]
            c = datetime(y, m, 1)
            c = c.strftime("%b %y")
            cr_price.append(
                [c, round((wpi1[i] * base[name]) / 100, 2), round(bb[i], 2)]
            )

        # print("Crop_Price: ", crop_price)
        # print(cr_price)
        return cr_price


# pr = price()
# data = pr.yeartopfive()
# print(data)
# for i in range(len(data)):
#         for j in range(len(data[i])):
#                 print(data[i][j])
