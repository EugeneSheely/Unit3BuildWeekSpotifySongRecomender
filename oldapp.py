from flask import Flask, render_template, request, url_for, redirect, session
#from model import newUser, oldUser
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import sys



app = Flask(__name__)
app.secret_key = "hello"

"""
@app.route('/')
def home():
    host = request.url_root
    return render_template("index.html")
"""
























@app.route("/login",methods = ["POST", "GET"])
def login():
    if request.method =="POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("login.html")

@app.route("/user",methods = ["POST", "GET"])
def user():
    if "user" in session:
        user = session["user"]
        return render_template("login.html", user=user)
    else:
        return redirect(url_for("login"))



@app.route("/",methods = ["POST", "GET"])
def home():
    topmessage1 = ""
    topmessage2 = ""
    bottommessage1 = ""
    bottommessage2 = ""
    status = ""
    user_name = ""
    #load Spotify Data:
    spotify_df = pd.read_csv("data.csv")
    spotify_df['artist_string'] = spotify_df['artists']
    df_groupby = spotify_df
    df_groupby['artists_str'] = df_groupby['artists'].str[1:-1]
    artists_list = df_groupby['artists_str'].str[1:-1].to_list()
    df_groupby['artists_str'] = df_groupby['artists_str'].str[1:-1]
    scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    users_gsheet = client.open("Lambda Unit 3 Project data server").worksheet("Sheet1")
    users_df = users_gsheet.get_all_values()
    headers = users_df.pop(0)
    users_df = pd.DataFrame(users_df, columns=headers)
    #print(users_df)
    usersK = users_df["User Name"].to_list()
    usersV = users_df["Password"].to_list()
    users = {}
    users_index = 0
    user_name = ""
    user = ""
    for key in usersK:
        users[key] = usersV[users_index]
        users_index = users_index +1


    #new user function:
    import request

    status = ""
    topmessage1 = "Are you a registered user? y/n? Press q to quit"

    if 1==1:
        topmessage1 = "Are you a registered user? y/n? Press q to quit"
        status = request.args['nm'] #form["nm"]

        return render_template("login.html", user=user, topmessage1 = topmessage1  , topmessage2 = topmessage2, bottommessage1 = bottommessage1, bottommessage2 = bottommessage2)
    topmessage1 = "Enter login name: "

    if status =="y":
        if 1==1:
            topmessage1 = "Enter login name: "
            return render_template("login.html", user=user, topmessage1 = topmessage1  , topmessage2 = topmessage2, bottommessage1 = bottommessage1, bottommessage2 = bottommessage2)
    return render_template("login.html", user=user, topmessage1 = topmessage1  , topmessage2 = topmessage2, bottommessage1 = bottommessage1, bottommessage2 = bottommessage2)




    while user_name == "":
        status = request.form["nm"]
        if status =="y":
            if 1==1:
                topmessage1 = "Enter login name: "
                return render_template("login.html", user=user, topmessage1 = topmessage1  , topmessage2 = topmessage2, bottommessage1 = bottommessage1, bottommessage2 = bottommessage2)

    if request.method =="POST":
        user = request.form["nm"]
        session["user"] = user
        return render_template("login.html", user=user, topmessage1 = topmessage1  , topmessage2 = topmessage2, bottommessage1 = bottommessage1, bottommessage2 = bottommessage2)
    else:
        return render_template("login.html")
    return render_template("login.html", user=user, topmessage1 = topmessage1  , topmessage2 = topmessage2, bottommessage1 = bottommessage1, bottommessage2 = bottommessage2)




if __name__ == "__main__":
    app.run(debug=True)


