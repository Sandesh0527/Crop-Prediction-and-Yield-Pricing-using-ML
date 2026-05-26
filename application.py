import datetime
import sqlite3
import os
from random import randint
from flask import *
from flask_mail import Mail, Message
from flask import Flask, request, render_template, url_for, flash, session, redirect
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
app.secret_key = "crop_prediction_dev_key_2024"

# Mail config — sending is suppressed in dev (OTPs printed to console instead)
app.config["MAIL_SERVER"] = "localhost"
app.config["MAIL_PORT"] = 25
app.config["MAIL_USERNAME"] = ""
app.config["MAIL_PASSWORD"] = ""
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_SUPPRESS_SEND"] = True
mail = Mail(app)

serializer = URLSafeTimedSerializer("crop_prediction")

DB_PATH = os.path.join(os.path.dirname(__file__), "crop_app.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS login (
            email TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            verified INTEGER DEFAULT 0
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS otp (
            email TEXT PRIMARY KEY,
            otp_code TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


init_db()


@app.route("/")
def root():
    return render_template("login.html")


@app.route("/suggestedcrops", methods=["POST"])
def suggestedcrops():
    state = request.form["state"]
    crop_filter = Filter()
    crop_list = crop_filter.findCrops(state)
    return render_template("filtered.html", crops=crop_list)


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
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM login WHERE email = ? AND password = ?",
        (email1, pass1),
    )
    checkUsername = cursor.fetchone()
    conn.close()
    if checkUsername is not None:
        if checkUsername["verified"] == 0:
            flash("User not verified. Check the console for your OTP.")
            return render_template("login.html")
        else:
            return render_template("cropsuggest.html")
    else:
        flash("User Not Found")
        return render_template("login.html")


def send_verify_link(email):
    # In dev mode, print verification link to console instead of emailing
    verify_account_url = url_for("verify_account", email=email, _external=True)
    print(f"[DEV] Verify account link for {email}: {verify_account_url}")


@app.route("/verify_account/<email>", methods=["GET", "POST"])
def verify_account(email):
    conn = get_db()
    cursor = conn.cursor()
    if request.method == "POST":
        cursor.execute("UPDATE login SET verified = 1 WHERE email = ?", (email,))
        conn.commit()
    conn.close()
    return render_template("verify_account.html", email=email)


@app.route("/send_otp", methods=["POST"])
def send_otp():
    conn = get_db()
    cursor = conn.cursor()
    email2 = request.get_data().decode("utf-8")
    otp = randint(100000, 999999)
    cursor.execute(
        "INSERT OR REPLACE INTO otp (email, otp_code) VALUES (?, ?)",
        (email2, str(otp)),
    )
    conn.commit()
    conn.close()
    # Print OTP to console instead of sending email
    print(f"[DEV] OTP for {email2}: {otp}")
    return jsonify(result={"status": "success"})


@app.route("/verified", methods=["POST"])
def verfied():
    conn = get_db()
    data = request.get_data().decode("utf-8")
    email = json.loads(data)["email"]
    otp_received = json.loads(data)["otp"]
    cursor = conn.cursor()
    cursor.execute("SELECT otp_code FROM otp WHERE email = ?", (email,))
    otp_row = cursor.fetchone()
    if otp_row and str(otp_row["otp_code"]) == str(otp_received):
        cursor.execute("UPDATE login SET verified = 1 WHERE email = ?", (email,))
        conn.commit()
        conn.close()
        return jsonify(result={"status": "success"})
    conn.close()
    return jsonify(result={"status": "failed"})


@app.route("/validate", methods=["POST"])
def validate():
    conn = get_db()
    if request.method == "POST":
        data = request.get_data().decode("utf-8")
        login_data = data.split("|")
        cursor = conn.cursor()
        try:
            # Auto-verify users on registration (no email required in dev)
            cursor.execute(
                "INSERT INTO login (username, email, password, verified) VALUES (?,?,?,1)",
                (login_data[1], login_data[0], login_data[2]),
            )
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return jsonify(result={"status": "error", "message": "Email already registered"})
        conn.close()
        return jsonify(result={"status": "success"})


@app.route("/resetpass", methods=["POST"])
def reset_password():
    conn = get_db()
    cemail = request.get_data().decode("utf-8")
    email = json.loads(cemail)["data"]
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM login WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    if user:
        token = serializer.dumps(email, salt="password-reset-salt")
        reset_url = url_for("confirm_password_reset", token=token, _external=True)
        print(f"[DEV] Password reset link for {email}: {reset_url}")
        return jsonify(result={"status": "success"})
    else:
        return jsonify(result={"status": "error", "message": "Email not found"})


@app.route("/confirm-password-reset/<token>", methods=["GET", "POST"])
def confirm_password_reset(token):
    try:
        conn = get_db()
        cursor = conn.cursor()
        email = serializer.loads(token, salt="password-reset-salt", max_age=3600)
        if request.method == "POST":
            new_password = request.form.get("new_password")
            cursor.execute(
                "UPDATE login SET password = ? WHERE email = ?",
                (new_password, email),
            )
            conn.commit()
            flash("Password reset successful")
        conn.close()
        return render_template("confirm_password_reset.html", email=email)
    except BadSignature:
        flash("Invalid or expired token. Please reset your password again.")
        return redirect(url_for("root"))


@app.route("/index")
def index():
    states = Filter()
    states = states.findStates()
    seasons = Filter()
    seasons = seasons.findSeason()
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

    model = XgbtTest()
    crop = model.xgbt_Predict(rainfall, temperature, ph)
    model = RFTest()
    yeild = model.RF_Predict(state, crop, season, district, area)
    for i in range(0, 3):
        crop_d.append(crops.cropdes(crop[i])[crop[i]])
        crop_d1.append(crops.cropss(crop[i]))
        crop_fr.append(crops.fert(crop[i]))

    result = {
        "crop": crop,
        "yeild": yeild,
        "crop_des1": crop_d,
        "crop_d1": crop_d1,
        "crop_d2": crop_d1,
        "crop_fr": crop_fr,
    }
    return render_template("result.html", result=result)


@app.route("/index1", methods=["POST", "GET"])
def index1():
    return redirect(url_for("index"))


@app.route("/send")
def senddis():
    dis3 = Filter()
    dis3 = dis3.findDistrict()
    return jsonify(result=dis3)


@app.route("/stats")
def stats():
    crop_names = [
        "Wheat", "Paddy", "Barley", "Groundnut", "Cotton", "Coconut",
        "Maize", "Soyabean", "Moong", "Bajra", "Chillies", "Gram",
        "Jowar", "Potato", "Peas", "Sugarcane", "Turmeric", "Onion",
    ]
    n = len(crop_names)
    num = n // 6 + math.ceil(n // 6 - n / 6)
    b = [[]]
    for i in range(num):
        if i == num - 1:
            b.append(range(n % 6))
        else:
            b.append(range(6))
    if num != 1:
        num = num + 1
    param = {
        "size": 6,
        "range1": range(num),
        "range": range(6),
        "names": crop_names,
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


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4000, debug=True)
