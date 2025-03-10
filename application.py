import datetime
from random import randint
from flask import *
from flask_mail import Mail, Message
from flask import Flask, request, render_template, url_for, flash, session, redirect
import mysql.connector
from filter import Filter
from Stats import Stat
from price import price
import crops
from xbgt_test import XgbtTest
from Rf_test import RFTest
from flask import jsonify, make_response
import math
from itsdangerous import URLSafeTimedSerializer, BadSignature
import json

application = app = Flask(__name__, template_folder="template")
app.secret_key = "the random string"
mail = Mail(app)
serializer = URLSafeTimedSerializer("crop_prediction")


app.config["MAIL_SERVER"] = ""
app.config["MAIL_PORT"] = 587
app.config["MAIL_USERNAME"] = ""
app.config["MAIL_PASSWORD"] = ""
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
mail = Mail(app)

sender_email = ""


def call_db():
    mydb = mysql.connector.connect(
        host="",
        user="",
        password="",
        database="",
        port=28175,
    )

    return mydb


@app.route("/")
def root():
    return render_template("login.html")


@app.route("/suggestedcrops", methods=["POST"])
def suggestedcrops():
    state = request.form["state"]
    crops = Filter()
    crops = crops.findCrops(state)
    return render_template("filtered.html", crops=crops)


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/cropsuggest")
def cropsuggestt():
    return render_template("cropsuggest.html")


@app.route("/success", methods=["POST"])
def success():
    email1 = request.form["email"]
    pass1 = request.form["password"]
    print(email1, pass1)
    mydb = call_db()
    mycursor = mydb.cursor()

    mycursor.execute(
        "SELECT * FROM login WHERE email = %s AND password = %s AND verified = 1",
        (
            email1,
            pass1,
        ),
    )
    checkUsername = mycursor.fetchone()
    print(checkUsername)
    if checkUsername != None:
        if checkUsername[3] == 0:
            flash("User not Verified , verify your email link sent to your email")
            send_verify_link(checkUsername[0])
            return render_template("login.html")
        else:
            return render_template("cropsuggest.html")
    else:
        flash("User Not Found")
        return render_template("login.html")


def send_verify_link(email):
    msg = Message("OTP", sender=sender_email, recipients=[email])
    verify_account_url = url_for("verify_account", email=email, _external=True)
    msg.body = f"Click the following link to verify your account: {verify_account_url}"
    mail.send(msg)


@app.route("/verify_account/<email>", methods=["GET", "POST"])
def verify_account(email):
    mydb = call_db()
    mycursor = mydb.cursor()
    if request.method == "POST":
        otp = request.form.get("otp")
        mycursor.execute("UPDATE login SET verified = 1 WHERE email = %s", (email,))
        mydb.commit()
    return render_template("verify_account.html", email=email)


@app.route("/send_otp", methods=["POST"])
def send_otp():
    mydb = call_db()
    mycursor = mydb.cursor()
    email2 = request.get_data().decode("utf-8")
    otp = randint(000000, 999999)
    sql = """INSERT INTO otp (email, otp_code) VALUES (%s, %s)
         ON DUPLICATE KEY UPDATE otp_code = VALUES(otp_code)"""

    # Execute the SQL statement with the provided values
    mycursor.execute(sql, (email2, otp))
    mydb.commit()
    mycursor.close()
    mydb.close()
    msg = Message("OTP", sender=sender_email, recipients=[email2])
    msg.body = str(otp)
    mail.send(msg)
    return jsonify(result={"status": "success"})


@app.route("/verified", methods=["POST"])
def verfied():
    mydb = call_db()
    data = request.get_data().decode("utf-8")
    print(data)
    email = json.loads(data)["email"]
    otp_recived = json.loads(data)["otp"]
    mycursor = mydb.cursor()
    mycursor.execute("SELECT otp_code from otp where email = %s", (email,))
    otp = mycursor.fetchone()
    print(otp)
    if otp[0] == otp_recived:
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE login SET verified = 1 WHERE email = %s", (email,))
        mydb.commit()
        return jsonify(result={"status": "success"})

    mycursor.close()
    mydb.close()
    return jsonify(result={"status": "failed"})


@app.route("/validate", methods=["POST"])
def validate():
    mydb = call_db()
    if request.method == "POST":
        data = request.get_data().decode("utf-8")
        print(data)
        login_data = data.split("|")
        mycursor = mydb.cursor()
        mycursor.execute(
            """INSERT INTO login (username,email,password) values(%s,%s,%s)""",
            (login_data[1], login_data[0], login_data[2]),
        )
        mydb.commit()
        mycursor.close()
        mydb.close()

        return jsonify(result={"status": "success"})


@app.route("/resetpass", methods=["POST"])
def reset_password():
    mydb = call_db()
    cemail = request.get_data().decode("utf-8")
    email = json.loads(cemail)["data"]
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM login WHERE email = %s", (email,))
    checkusername = mycursor.fetchone()[0]
    print(checkusername)
    if checkusername:
        # Generate a unique token and URL for password reset
        token = serializer.dumps(email, salt="password-reset-salt")
        reset_url = url_for("confirm_password_reset", token=token, _external=True)
        # Send a password reset email to the user
        msg = Message("Password Reset", sender=sender_email, recipients=[email])
        msg.body = f"Click the following link to reset your password: {reset_url}"
        mail.send(msg)
        return jsonify(result={"status": "success"})
    else:
        return jsonify(result={"status": "error", "message": "Email not found"})


@app.route("/confirm-password-reset/<token>", methods=["GET", "POST"])
def confirm_password_reset(token):
    try:
        mydb = call_db()
        mycursor = mydb.cursor()
        email = serializer.loads(token, salt="password-reset-salt", max_age=3600)
        if request.method == "POST":
            new_password = request.form.get("new_password")
            print(new_password)
            mycursor.execute(
                "UPDATE login SET password = %s WHERE email = %s",
                (
                    new_password,
                    email,
                ),
            )

            mydb.commit()
            flash("Password reset successful")
            # return redirect(url_for('root'))
        return render_template("confirm_password_reset.html", email=email)
    except BadSignature:
        flash("Invalid or expired token,Please Reset pass Again")
        # return redirect(url_for('root'))


@app.route("/index")
def index():
    states = Filter()
    states = states.findStates()
    seasons = Filter()
    seasons = seasons.findSeason()
    # districts = Filter()
    # districts = districts.findDistrict()
    return render_template("input.html", states=states, seasons=seasons)


@app.route("/predict", methods=["POST"])
def predict():
    crop_d = []
    crop_d1 = []
    crop_fr = []
    rainfall = float(request.form["rainfall"])
    temperature = float(request.form["temperature"])
    ph = float(request.form["ph"])
    area = float(request.form["area"])
    area = area * 0.000404686
    state = request.form["state"]
    season = request.form["season"]
    district = request.form["district"]
    season = season.strip()
    print(state)
    # print(season, "Hii")
    print(temperature, rainfall, ph, area, season)

    model = XgbtTest()
    crop = model.xgbt_Predict(rainfall, temperature, ph)
    model = RFTest()
    yeild = model.RF_Predict(state, crop, season, district, area)
    for i in range(0, 3):
        crop_d.append(crops.cropdes(crop[i])[crop[i]])
        crop_d1.append(crops.cropss(crop[i]))
        crop_fr.append(crops.fert(crop[i]))

    print(crop_d)
    # print(crop_d1)
    print(crop_fr)
    result = {
        "crop": crop,
        "yeild": yeild,
        "crop_des1": crop_d,
        "crop_d1": crop_d1,
        "crop_d2": crop_d1,
        "crop_fr": crop_fr,
    }
    return render_template("result.html", result=result)


# @app.context_processor
@app.route("/index1", methods=["POST", "GET"])
def index1():
    global text


@app.route("/send")
def senddis():
    dis3 = Filter()
    dis3 = dis3.findDistrict()
    return jsonify(result=dis3)


@app.route("/stats")
def stats():
    crops = [
        "Wheat",
        "Paddy",
        "Barley",
        "Groundnut",
        "Cotton",
        "Coconut",
        "Maize",
        "Soyabean",
        "Moong",
        "Bajra",
        "Chillies",
        "Gram",
        "Jowar",
        "Potato",
        "Peas",
        "Sugarcane",
        "Turmeric",
        "Onion",
    ]
    n = len(crops)
    num = n // 6 + math.ceil(n // 6 - n / 6)
    a = n // 6
    b = [[]]
    for i in range(num):
        if i == num - 1:
            b.append(range(n % 6))
        else:
            b.append(range(6))
    if num == 1:
        pass
    else:
        num = num + 1
    param = {
        "size": 6,
        "range1": range(num),
        "range": range(6),
        "names": crops,
        "range2": range(1),
        "cnt": n,
    }
    return render_template("stats.html", param=param)


pr = price()


@app.route("/stats/<name>")
def statview(name):
    param = {"name": name, "range1": range(2), "range": range(6)}

    cur_price = pr.cur_price(name)
    max_price, min_price, full_year = pr.priceyear(name)
    prev_year = pr.prevyear(name)
    crop_d = crops.cropss(name)
    x_cord = [i[0] for i in full_year]
    y_cord = [i[1] for i in full_year]
    p_x_cord = [i[0] for i in prev_year]
    p_y_cord = [i[1] for i in prev_year]

    crops_dat = {
        "name": name,
        "cur_price": cur_price,
        "exports": crop_d[2],
        "Majorl": crop_d[0],
        "season": crop_d[1],
        "max_p": max_price,
        "min_p": min_price,
        "full_year": full_year,
        "x_cord": x_cord,
        "y_cord": y_cord,
        "p_x_cord": p_x_cord,
        "p_y_cord": p_y_cord,
    }
    return render_template("statview.html", param=param, crops_dat=crops_dat)


@app.route("/trend")
def trend():
    top = pr.firstfive()
    bot = pr.bottomfive()
    topyear = pr.yeartopfive()

    data1 = {"top": top, "bot": bot, "topyear": topyear}
    return render_template("/trend.html", data1=data1)


app.run(host="127.0.0.1", port=4000, debug=True)
