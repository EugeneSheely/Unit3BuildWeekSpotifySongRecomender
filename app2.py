from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)
app.secret_key = "hello"





@app.route("/",methods = ["POST", "GET"])
def home():
    import time
    m1 = ""
    m2 = ""
    m3 = ""
    m4 = ""
    m5 = ""
    m6 = ""
    m7 = ""


    account = ""
    user = ""
    password = ""
    newuser = ""
    newpassword = ""






    user = ""
    topmessage1 = ""
    topmessage2 = ""
    bottommessage1 = ""
    bottommessage2 = ""
    quit = False
    index = 0
    account = ""
    time = time.time()
    m1 = "Do you have a username? y/n"

    if   index == 0:
        m1 = "Do you have a username? y/n"
        if request.method =="POST":

            account = request.form["account"]
            session["account"] = account
            if account == "y":
                m1 = ""
                index = 1

            if account == "n":
                m1 = ""
                index = 1



    if  account == "y" and index == 1:
        m2 = "what's your username?"
        if request.method =="POST":

                user = request.form["username"]
                session["user"] = user
                account = "y"




                if user != "":

                    m2 = ""
                    index =2

        if account == "y" and  index == 2:
            m3 = "what's your password?"
            if request.method =="POST":


                password = request.form["password"]
                session["password"] = password

                if password != "":
                    index = 3

        if index == 3:
            m4 = "pending"
        m5 = "hi"








    '''    
    if request.method =="POST" and index == 0:
        topmessage1 = "Do you have a username? y/n"
        account = request.form["nm"]
        session["account"] = account

    if account == "y":
        index = 1
    if account == "n":
        index = 1
    #log in:
    while account == "y" and index == 1:
        if  request.method =="POST" and account == "y" and index == 1:
            topmessage1 = "what's your username?"
            user = request.form["nm"]
            session["user"] = user
            if user != "":
                index =2






    #create account
    if request.method =="POST" and account == "n" and index == 1:
        topmessage1 = "Create a username:"
        newuser = request.form["nm"]
        session["newuser"] = newuser
        index = 2

    if request.method =="POST" and account == "n" and index == 2:
        topmessage1 = "Create a password:"
        newpassword = request.form["nm"]
        session["newpassword"] = newpassword
        user = newuser
        index = 3
    '''











    return render_template("login.html", m1 = m1, m2=m2, m3=m3, m4=m4, m5=m5, m6=m6, m7=m7)




if __name__ == "__main__":
    app.run(debug=True)